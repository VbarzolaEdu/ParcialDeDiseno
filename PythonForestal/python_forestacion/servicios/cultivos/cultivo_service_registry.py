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
