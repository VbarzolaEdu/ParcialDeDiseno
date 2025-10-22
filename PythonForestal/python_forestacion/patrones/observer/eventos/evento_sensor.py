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
