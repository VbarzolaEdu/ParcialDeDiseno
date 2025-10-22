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
