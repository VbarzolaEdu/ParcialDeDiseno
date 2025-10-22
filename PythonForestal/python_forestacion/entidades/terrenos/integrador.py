"""
Archivo integrador generado automaticamente
Directorio: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/terrenos
Fecha: 2025-10-21 22:24:05
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/terrenos/__init__.py
# ================================================================================

# python_forestacion/entidades/terrenos/__init__.py


# ================================================================================
# ARCHIVO 2/4: plantacion.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/terrenos/plantacion.py
# ================================================================================

# python_forestacion/entidades/terrenos/plantacion.py
from dataclasses import dataclass, field
from typing import List
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException

@dataclass
class Plantacion:
    nombre: str
    superficie_max: float
    agua_disponible: int = 500
    cultivos: List[Cultivo] = field(default_factory=list)
    trabajadores: List = field(default_factory=list)

    def add_cultivo(self, cultivo: Cultivo) -> None:
        ocupada = sum(c.get_superficie() for c in self.cultivos)
        superficie_requerida = ocupada + cultivo.get_superficie()
        if superficie_requerida > self.superficie_max:
            raise SuperficieInsuficienteException(
                superficie_requerida=superficie_requerida,
                superficie_disponible=self.superficie_max
            )
        self.cultivos.append(cultivo)

    def consumir_agua(self, cantidad: int) -> None:
        if cantidad < 0:
            raise ValueError("Cantidad negativa no permitida")
        if self.agua_disponible < cantidad:
            raise AguaAgotadaException(
                agua_requerida=cantidad,
                agua_disponible=self.agua_disponible
            )
        self.agua_disponible -= cantidad


# ================================================================================
# ARCHIVO 3/4: registro_forestal.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/terrenos/registro_forestal.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/4: tierra.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/entidades/terrenos/tierra.py
# ================================================================================

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


