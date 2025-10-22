# python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
from datetime import date
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """
    Estrategia de absorcion constante para hortalizas.
    Absorbe siempre la misma cantidad independiente de la temporada.
    Lechuga: 1L
    Zanahoria: 2L
    """
    
    def __init__(self, cantidad_constante: int):
        self._cantidad = cantidad_constante

    def calcular_absorcion(self, fecha: date, temperatura: float, humedad: float, cultivo) -> int:
        return self._cantidad
