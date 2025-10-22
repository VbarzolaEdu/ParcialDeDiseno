# python_forestacion/entidades/terrenos/tierra.py
from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


@dataclass
class Tierra:
    """
    Representa un terreno con su padron catastral y superficie.
    
    Attributes:
        id_padron_catastral: Numero de padron unico
        superficie: Superficie en metros cuadrados
        domicilio: Direccion del terreno
        finca: Plantacion asociada al terreno
    """
    id_padron_catastral: int
    superficie: float
    domicilio: str
    finca: Optional['Plantacion'] = None
    
    def __post_init__(self):
        if self.superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
    
    def get_id_padron_catastral(self) -> int:
        return self.id_padron_catastral
    
    def get_superficie(self) -> float:
        return self.superficie
    
    def set_superficie(self, superficie: float) -> None:
        if superficie <= 0:
            raise ValueError("La superficie debe ser mayor a cero")
        self.superficie = superficie
    
    def get_domicilio(self) -> str:
        return self.domicilio
    
    def set_domicilio(self, domicilio: str) -> None:
        self.domicilio = domicilio
    
    def get_finca(self) -> Optional['Plantacion']:
        return self.finca
    
    def set_finca(self, finca: 'Plantacion') -> None:
        self.finca = finca
