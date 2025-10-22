"""
Archivo integrador generado automaticamente
Directorio: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/riego/sensores
Fecha: 2025-10-21 22:24:05
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/riego/sensores/__init__.py
# ================================================================================

# python_forestacion/riego/sensores/__init__.py
# python_forestacion/riego/sensores/__init__.py

from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask

__all__ = ['TemperaturaReaderTask', 'HumedadReaderTask']


# ================================================================================
# ARCHIVO 2/3: humedad_reader_task.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/riego/sensores/humedad_reader_task.py
# ================================================================================

# python_forestacion/riego/sensores/humedad_reader_task.py
import threading
import time
import random
from typing import Optional
from python_forestacion.patrones.observer.observable import Observable

class HumedadReaderTask(Observable[float], threading.Thread):
    """
    Sensor simulado de humedad (%).
    Notifica valores 0..100 cada intervalo (segundos).
    """
    def __init__(self, intervalo: float = 5.0, min_hum: float = 0.0, max_hum: float = 100.0):
        Observable.__init__(self)
        threading.Thread.__init__(self, daemon=True)
        self.intervalo = intervalo
        self._stop_event = threading.Event()
        self.min_hum = min_hum
        self.max_hum = max_hum

    def run(self):
        while not self._stop_event.is_set():
            hum = round(random.uniform(self.min_hum, self.max_hum), 2)
            self.notificar_observadores(hum)
            time.sleep(self.intervalo)

    def stop(self):
        self._stop_event.set()


# ================================================================================
# ARCHIVO 3/3: temperatura_reader_task.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/riego/sensores/temperatura_reader_task.py
# ================================================================================

# python_forestacion/riego/sensores/temperatura_reader_task.py
import threading
import time
import random
from typing import Optional
from python_forestacion.patrones.observer.observable import Observable

class TemperaturaReaderTask(Observable[float], threading.Thread):
    """
    Sensor simulado de temperatura.
    Hereda de Observable[float] y de Thread.
    Notifica la temperatura como float a sus observadores cada intervalo (segundos).
    """
    def __init__(self, intervalo: float = 5.0, min_temp: float = 0.0, max_temp: float = 40.0):
        Observable.__init__(self)
        threading.Thread.__init__(self, daemon=True)
        self.intervalo = intervalo
        self._stop_event = threading.Event()
        self.min_temp = min_temp
        self.max_temp = max_temp

    def run(self):
        while not self._stop_event.is_set():
            # Aquí se simula la lectura; en integración real reemplazar por lectura del sensor
            temp = round(random.uniform(self.min_temp, self.max_temp), 2)
            # notificar a observadores
            self.notificar_observadores(temp)
            time.sleep(self.intervalo)

    def stop(self):
        self._stop_event.set()


