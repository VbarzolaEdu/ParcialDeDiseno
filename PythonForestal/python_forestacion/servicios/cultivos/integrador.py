"""
Archivo integrador generado automaticamente
Directorio: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/cultivos
Fecha: 2025-10-21 22:24:05
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: __init__.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/cultivos/__init__.py
# ================================================================================

# python_forestacion/servicios/cultivos/__init__.py


# ================================================================================
# ARCHIVO 2/8: arbol_service.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/cultivos/arbol_service.py
# ================================================================================

# python_forestacion/servicios/cultivos/arbol_service.py
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.constantes import CRECIMIENTO_PINO_POR_RIEGO, CRECIMIENTO_OLIVO_POR_RIEGO
from datetime import date


class ArbolService(CultivoService):
    """
    Servicio base para gestion de arboles.
    Los arboles tienen la capacidad adicional de crecer en altura.
    """
    
    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        super().__init__(estrategia_absorcion)
    
    def crecer(self, arbol, incremento: float) -> None:
        """
        Hace crecer un arbol en altura.
        
        Args:
            arbol: Arbol que crecera
            incremento: Cantidad de metros a crecer
        """
        if hasattr(arbol, 'crecer'):
            arbol.crecer(incremento)


# ================================================================================
# ARCHIVO 3/8: cultivo_service.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/cultivos/cultivo_service.py
# ================================================================================

# python_forestacion/servicios/cultivos/cultivo_service.py
from datetime import date
from typing import Optional
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class CultivoService:
    def __init__(self, estrategia: AbsorcionAguaStrategy):
        self._estrategia = estrategia

    def absorver_agua(self, cultivo, fecha: date, temperatura: float, humedad: float) -> int:
        cantidad = self._estrategia.calcular_absorcion(fecha, temperatura, humedad, cultivo)
        cultivo.set_agua(cultivo.get_agua() + cantidad)
        # comportamiento por tipo (ej.: crecimiento) será delegado por servicios concretos si corresponde
        return cantidad


# ================================================================================
# ARCHIVO 4/8: cultivo_service_registry.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ================================================================================

# python_forestacion/servicios/cultivos/cultivo_service_registry.py
from threading import Lock
from typing import Dict, Type, Callable
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.entidades.cultivos.pino import Pino
from python_forestacion.entidades.cultivos.olivo import Olivo
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

class CultivoServiceRegistry:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._init_internal()
        return cls._instance

    def _init_internal(self):
        # diccionarios de dispatch por tipo
        self._absorber_agua_handlers: Dict[Type, Callable] = {}
        self._mostrar_datos_handlers: Dict[Type, Callable] = {}
        # registrar handlers por defecto
        self._pino_service = CultivoService(AbsorcionSeasonalStrategy())
        self._olivo_service = CultivoService(AbsorcionSeasonalStrategy())
        self._lechuga_service = CultivoService(AbsorcionConstanteStrategy(1))
        self._zanahoria_service = CultivoService(AbsorcionConstanteStrategy(2))

        self.register_handler(Pino, self._pino_service)
        self.register_handler(Olivo, self._olivo_service)
        self.register_handler(Lechuga, self._lechuga_service)
        self.register_handler(Zanahoria, self._zanahoria_service)

    @classmethod
    def get_instance(cls):
        return cls()

    def register_handler(self, tipo: Type, service: CultivoService):
        self._absorber_agua_handlers[tipo] = service

    def absorber_agua(self, cultivo, fecha, temperatura, humedad) -> int:
        tipo = type(cultivo)
        if tipo not in self._absorber_agua_handlers:
            raise ValueError(f"Tipo no registrado: {tipo}")
        service: CultivoService = self._absorber_agua_handlers[tipo]
        return service.absorver_agua(cultivo, fecha, temperatura, humedad)

    def mostrar_datos(self, cultivo):
        # Implementación simple de muestra por tipo (puedes ampliar)
        tipo = type(cultivo)
        if tipo == Pino:
            print(f"Cultivo: Pino\nSuperficie: {cultivo.superficie} m²\nAgua: {cultivo.agua} L\nID: {cultivo.id}\nAltura: {cultivo.altura} m\nVariedad: {cultivo.variedad}")
        elif tipo == Olivo:
            print(f"Cultivo: Olivo\nSuperficie: {cultivo.superficie} m²\nAgua: {cultivo.agua} L\nID: {cultivo.id}\nAltura: {cultivo.altura} m\nTipo aceituna: {cultivo.tipo_aceituna}")
        elif tipo == Lechuga:
            print(f"Cultivo: Lechuga\nSuperficie: {cultivo.superficie} m²\nAgua: {cultivo.agua} L\nID: {cultivo.id}\nVariedad: {cultivo.variedad}\nInvernadero: {cultivo.invernadero}")
        elif tipo == Zanahoria:
            print(f"Cultivo: Zanahoria\nSuperficie: {cultivo.superficie} m²\nAgua: {cultivo.agua} L\nID: {cultivo.id}\nIs baby: {cultivo.is_baby}")
        else:
            raise ValueError("Tipo desconocido para mostrar_datos")


# ================================================================================
# ARCHIVO 5/8: lechuga_service.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/cultivos/lechuga_service.py
# ================================================================================

# python_forestacion/servicios/cultivos/lechuga_service.py
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy


class LechugaService(CultivoService):
    """
    Servicio especifico para gestion de lechugas.
    Usa absorcion constante de 1L (Strategy Pattern).
    """
    
    def __init__(self):
        # Inyectar estrategia constante: lechugas absorben 1L siempre
        super().__init__(AbsorcionConstanteStrategy(1))


# ================================================================================
# ARCHIVO 6/8: olivo_service.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/cultivos/olivo_service.py
# ================================================================================

# python_forestacion/servicios/cultivos/olivo_service.py
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy


class OlivoService(ArbolService):
    """
    Servicio especifico para gestion de olivos.
    Usa absorcion estacional (Strategy Pattern).
    """
    
    def __init__(self):
        # Inyectar estrategia estacional para arboles
        super().__init__(AbsorcionSeasonalStrategy())


# ================================================================================
# ARCHIVO 7/8: pino_service.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/cultivos/pino_service.py
# ================================================================================

# python_forestacion/servicios/cultivos/pino_service.py
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy


class PinoService(ArbolService):
    """
    Servicio especifico para gestion de pinos.
    Usa absorcion estacional (Strategy Pattern).
    """
    
    def __init__(self):
        # Inyectar estrategia estacional para arboles
        super().__init__(AbsorcionSeasonalStrategy())


# ================================================================================
# ARCHIVO 8/8: zanahoria_service.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/cultivos/zanahoria_service.py
# ================================================================================

# python_forestacion/servicios/cultivos/zanahoria_service.py
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy


class ZanahoriaService(CultivoService):
    """
    Servicio especifico para gestion de zanahorias.
    Usa absorcion constante de 2L (Strategy Pattern).
    """
    
    def __init__(self):
        # Inyectar estrategia constante: zanahorias absorben 2L siempre
        super().__init__(AbsorcionConstanteStrategy(2))


