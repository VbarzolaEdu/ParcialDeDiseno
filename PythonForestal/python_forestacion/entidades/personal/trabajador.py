# python_forestacion/entidades/personal/trabajador.py
from dataclasses import dataclass, field
from typing import List, Optional
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.apto_medico import AptoMedico


@dataclass
class Trabajador:
    """
    Representa un trabajador agricola con sus tareas y apto medico.
    
    Attributes:
        dni: DNI unico del trabajador
        nombre: Nombre completo del trabajador
        tareas: Lista de tareas asignadas
        apto_medico: Apto medico del trabajador (opcional)
    """
    dni: int
    nombre: str
    tareas: List[Tarea] = field(default_factory=list)
    apto_medico: Optional[AptoMedico] = None
    
    def get_dni(self) -> int:
        return self.dni
    
    def get_nombre(self) -> str:
        return self.nombre
    
    def get_tareas(self) -> List[Tarea]:
        # Defensive copy
        return self.tareas.copy()
    
    def set_tareas(self, tareas: List[Tarea]) -> None:
        # Defensive copy
        self.tareas = tareas.copy()
    
    def agregar_tarea(self, tarea: Tarea) -> None:
        self.tareas.append(tarea)
    
    def get_apto_medico(self) -> Optional[AptoMedico]:
        return self.apto_medico
    
    def set_apto_medico(self, apto_medico: AptoMedico) -> None:
        self.apto_medico = apto_medico
