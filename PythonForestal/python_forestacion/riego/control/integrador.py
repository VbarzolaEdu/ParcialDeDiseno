"""
Archivo integrador generado automaticamente
Directorio: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/riego/control
Fecha: 2025-10-21 22:24:05
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/riego/control/__init__.py
# ================================================================================

# python_forestacion/riego/control/__init__.py


# ================================================================================
# ARCHIVO 2/2: control_riego_task.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/riego/control/control_riego_task.py
# ================================================================================

# python_forestacion/riego/control/control_riego_task.py
import threading
import time
from datetime import datetime, timedelta
from typing import Any
from python_forestacion.patrones.observer.observer import Observer
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.constantes import TEMP_MIN_RIEGO, TEMP_MAX_RIEGO, HUMEDAD_MAX_RIEGO

class ControlRiegoTask(Observer[Any]):
    """
    Observador que recibe lecturas de sensores (temperatura y humedad).
    Cuando las condiciones de riego se cumplen llama a PlantacionService.regar(plantacion).
    Uso:
      control = ControlRiegoTask(plantacion)
      temp_sensor.agregar_observador(control)
      hum_sensor.agregar_observador(control)
    """

    def __init__(self, plantacion, cooldown_seconds: int = 60):
        # plantacion: instancia de Plantacion (donde se realizan los riegos)
        self.plantacion = plantacion
        self._plantation_service = PlantacionService()
        self._lock = threading.Lock()
        self._last_temp: float | None = None
        self._last_hum: float | None = None
        self._last_riego_time: datetime | None = None
        self.cooldown = timedelta(seconds=cooldown_seconds)

    def actualizar(self, evento: Any) -> None:
        """
        Este método es llamado por los sensores.
        El evento puede ser temperatura (float) o humedad (float).
        Distinguir por rango: temperatura típicamente -50..+60, humedad 0..100.
        """
        try:
            val = float(evento)
        except Exception:
            return

        # Heurística simple para distinguir: si 0 <= val <= 100 puede ser ambos; usamos nombrado por sensores idealmente.
        # En este diseño los sensores envían valores float sin metadata; asumimos que los sensores se registran en control con contexto.
        # Para evitar ambigüedad, el pattern recomendado es que los sensores envíen tuplas (tipo, valor).
        # Pero aquí, y para compatibilidad con los Observable actuales, distinguimos por si val in [0,100] -> lo tratamos como humedad
        # y si fuera fuera de ese rango lo tratamos como temperatura. Esto funciona en la mayoría de casos simulados.
        if 0.0 <= val <= 100.0:
            # posible humedad o temperatura; preferimos tratar como humedad si ya tenemos temperatura reciente
            # política simple:
            if self._last_temp is None:
                # asumimos que es temperatura (si no hay temp previa)
                self._last_temp = val
            else:
                self._last_hum = val
        else:
            # temperatura fuera de 0..100 -> temperatura
            self._last_temp = val

        # mejor enfoque: ejecutar evaluación cuando tengamos ambos valores
        if self._last_temp is not None and self._last_hum is not None:
            self._evaluar_y_regar(self._last_temp, self._last_hum)
            # reset simple para siguiente ciclo
            self._last_temp = None
            self._last_hum = None

    def _puede_regar(self) -> bool:
        if self._last_riego_time is None:
            return True
        return datetime.now() - self._last_riego_time >= self.cooldown

    def _evaluar_y_regar(self, temperatura: float, humedad: float):
        """
        Lógica de decisión:
         - temperatura dentro de [TEMP_MIN_RIEGO, TEMP_MAX_RIEGO]
         - humedad <= HUMEDAD_MAX_RIEGO
         - y cooldown respetado
        """
        with self._lock:
            if not self._puede_regar():
                return

            condiciones_temp = TEMP_MIN_RIEGO <= temperatura <= TEMP_MAX_RIEGO
            condiciones_hum = humedad <= HUMEDAD_MAX_RIEGO

            if condiciones_temp and condiciones_hum:
                try:
                    # llamar al servicio de plantacion
                    resultados = self._plantation_service.regar(self.plantacion, temperatura=temperatura, humedad=humedad)
                    self._last_riego_time = datetime.now()
                    # opcional: imprimir resumen
                    print(f"[{datetime.now().isoformat()}] Riego ejecutado. Temperatura={temperatura}, Humedad={humedad}")
                    for cultivo, amt in resultados:
                        print(f"  - ID {cultivo.id} absorbió {amt} L")
                    print(f"  Agua restante en plantacion: {self.plantacion.agua_disponible} L")
                except Exception as e:
                    print(f"[{datetime.now().isoformat()}] Error al regar: {e}")
            else:
                # condiciones no cumplidas; solo log para debug
                print(f"[{datetime.now().isoformat()}] No riega: Temp={temperatura} (req {TEMP_MIN_RIEGO}-{TEMP_MAX_RIEGO}), Hum={humedad} (req <={HUMEDAD_MAX_RIEGO})")


