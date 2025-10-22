# python_forestacion/entidades/personal/apto_medico.py
from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class AptoMedico:
    """
    Representa el apto medico de un trabajador.
    
    Attributes:
        apto: Estado de aptitud (True = apto, False = no apto)
        fecha_emision: Fecha de emision del apto
        observaciones: Observaciones medicas opcionales
    """
    apto: bool
    fecha_emision: date
    observaciones: Optional[str] = None
    
    def esta_apto(self) -> bool:
        return self.apto
    
    def get_fecha_emision(self) -> date:
        return self.fecha_emision
    
    def get_observaciones(self) -> Optional[str]:
        return self.observaciones
