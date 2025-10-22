# python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
from datetime import date
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.constantes import (
    ABSORCION_SEASONAL_VERANO,
    ABSORCION_SEASONAL_INVIERNO,
    MES_INICIO_VERANO,
    MES_FIN_VERANO
)

class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """
    Estrategia de absorcion estacional para arboles.
    Verano (marzo-agosto): 5L
    Invierno (septiembre-febrero): 2L
    """
    
    def calcular_absorcion(self, fecha: date, temperatura: float, humedad: float, cultivo) -> int:
        mes = fecha.month
        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO
        return ABSORCION_SEASONAL_INVIERNO
