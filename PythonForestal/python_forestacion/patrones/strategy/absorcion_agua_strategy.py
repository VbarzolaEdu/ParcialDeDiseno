# python_forestacion/patrones/strategy/absorcion_agua_strategy.py
from abc import ABC, abstractmethod
from datetime import date

class AbsorcionAguaStrategy(ABC):
    @abstractmethod
    def calcular_absorcion(self, fecha: date, temperatura: float, humedad: float, cultivo) -> int:
        ...
