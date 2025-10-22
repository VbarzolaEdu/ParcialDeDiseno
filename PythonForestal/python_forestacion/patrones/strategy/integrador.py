"""
Archivo integrador generado automaticamente
Directorio: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/strategy
Fecha: 2025-10-21 22:24:05
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/strategy/__init__.py
# ================================================================================

# python_forestacion/patrones/strategy/__init__.py


# ================================================================================
# ARCHIVO 2/2: absorcion_agua_strategy.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/strategy/absorcion_agua_strategy.py
# ================================================================================

# python_forestacion/patrones/strategy/absorcion_agua_strategy.py
from abc import ABC, abstractmethod
from datetime import date

class AbsorcionAguaStrategy(ABC):
    @abstractmethod
    def calcular_absorcion(self, fecha: date, temperatura: float, humedad: float, cultivo) -> int:
        ...


