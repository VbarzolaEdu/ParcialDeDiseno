"""
Archivo integrador generado automaticamente
Directorio: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/observer/eventos
Fecha: 2025-10-21 22:24:05
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/observer/eventos/__init__.py
# ================================================================================

# python_forestacion/patrones/observer/eventos/__init__.py


# ================================================================================
# ARCHIVO 2/3: evento_plantacion.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/observer/eventos/evento_plantacion.py
# ================================================================================

# python_forestacion/patrones/observer/eventos/evento_plantacion.py
from dataclasses import dataclass
from typing import Optional


@dataclass
class EventoPlantacion:
    """
    Evento relacionado con operaciones de plantacion.
    Puede ser usado para notificar plantacion, riego, fumigacion, etc.
    """
    tipo: str  # "PLANTACION", "RIEGO", "FUMIGACION", etc.
    descripcion: str
    cantidad: Optional[int] = None
    superficie: Optional[float] = None


# ================================================================================
# ARCHIVO 3/3: evento_sensor.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/patrones/observer/eventos/evento_sensor.py
# ================================================================================

# python_forestacion/patrones/observer/eventos/evento_sensor.py
from dataclasses import dataclass
from datetime import datetime


@dataclass
class EventoSensor:
    """
    Evento generado por un sensor.
    Contiene el valor leido y metadata adicional.
    """
    tipo_sensor: str  # "TEMPERATURA" o "HUMEDAD"
    valor: float
    timestamp: datetime
    unidad: str  # "°C" o "%"


