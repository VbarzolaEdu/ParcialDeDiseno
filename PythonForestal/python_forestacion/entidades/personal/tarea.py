# python_forestacion/entidades/personal/tarea.py
from dataclasses import dataclass
from datetime import date


@dataclass
class Tarea:
    """
    Representa una tarea asignada a un trabajador.
    
    Attributes:
        id_tarea: ID unico de la tarea
        fecha: Fecha programada para la tarea
        descripcion: Descripcion de la tarea
        completada: Estado de la tarea (False = pendiente, True = completada)
    """
    id_tarea: int
    fecha: date
    descripcion: str
    completada: bool = False
    
    def get_id_tarea(self) -> int:
        return self.id_tarea
    
    def get_fecha(self) -> date:
        return self.fecha
    
    def get_descripcion(self) -> str:
        return self.descripcion
    
    def is_completada(self) -> bool:
        return self.completada
    
    def marcar_completada(self) -> None:
        self.completada = True
