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
