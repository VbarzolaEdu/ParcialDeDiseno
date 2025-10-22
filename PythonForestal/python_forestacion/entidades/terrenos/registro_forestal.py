# python_forestacion/entidades/terrenos/registro_forestal.py
from dataclasses import dataclass
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion


@dataclass
class RegistroForestal:
    """
    Registro forestal que vincula terreno, plantacion, propietario y avaluo.
    
    Attributes:
        id_padron: ID del padron catastral
        tierra: Terreno asociado
        plantacion: Plantacion asociada
        propietario: Nombre del propietario
        avaluo: Avaluo fiscal del terreno
    """
    id_padron: int
    tierra: Tierra
    plantacion: Plantacion
    propietario: str
    avaluo: float
    
    def get_id_padron(self) -> int:
        return self.id_padron
    
    def get_tierra(self) -> Tierra:
        return self.tierra
    
    def get_plantacion(self) -> Plantacion:
        return self.plantacion
    
    def get_propietario(self) -> str:
        return self.propietario
    
    def get_avaluo(self) -> float:
        return self.avaluo
