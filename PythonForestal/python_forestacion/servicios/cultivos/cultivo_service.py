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
