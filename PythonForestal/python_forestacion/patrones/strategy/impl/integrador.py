"""
Archivo integrador generado automaticamente
Directorio: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/strategy/impl
Fecha: 2025-10-21 22:24:05
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/strategy/impl/__init__.py
# ================================================================================

# python_forestacion/patrones/strategy/impl/__init__.py


# ================================================================================
# ARCHIVO 2/3: absorcion_constante_strategy.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/3: absorcion_seasonal_strategy.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
# ================================================================================

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


