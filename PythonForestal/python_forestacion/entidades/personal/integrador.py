"""
Archivo integrador generado automaticamente
Directorio: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/personal
Fecha: 2025-10-21 22:24:05
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/personal/__init__.py
# ================================================================================

# python_forestacion/entidades/personal/__init__.py


# ================================================================================
# ARCHIVO 2/5: apto_medico.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/personal/apto_medico.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/5: herramienta.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/personal/herramienta.py
# ================================================================================

# python_forestacion/entidades/personal/herramienta.py
from dataclasses import dataclass


@dataclass
class Herramienta:
    """
    Representa una herramienta certificada para uso en tareas agricolas.
    
    Attributes:
        id_herramienta: ID unico de la herramienta
        nombre: Nombre de la herramienta
        certificado_hys: Certificacion de higiene y seguridad
    """
    id_herramienta: int
    nombre: str
    certificado_hys: bool
    
    def get_id_herramienta(self) -> int:
        return self.id_herramienta
    
    def get_nombre(self) -> str:
        return self.nombre
    
    def is_certificado_hys(self) -> bool:
        return self.certificado_hys


# ================================================================================
# ARCHIVO 4/5: tarea.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/personal/tarea.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/5: trabajador.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/personal/trabajador.py
# ================================================================================

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


