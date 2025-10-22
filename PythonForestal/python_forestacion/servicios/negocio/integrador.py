"""
Archivo integrador generado automaticamente
Directorio: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/negocio
Fecha: 2025-10-21 22:24:05
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/negocio/__init__.py
# ================================================================================

# python_forestacion/servicios/negocio/__init__.py


# ================================================================================
# ARCHIVO 2/3: fincas_service.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/negocio/fincas_service.py
# ================================================================================

# python_forestacion/servicios/negocio/fincas_service.py
from typing import Dict, Type, TypeVar
from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.cultivos.cultivo import Cultivo
from python_forestacion.servicios.negocio.paquete import Paquete

T = TypeVar('T', bound=Cultivo)


class FincasService:
    """
    Servicio para gestion de multiples fincas.
    Proporciona operaciones de alto nivel como fumigacion y cosecha.
    """
    
    def __init__(self):
        self._registros: Dict[int, RegistroForestal] = {}
    
    def add_finca(self, registro: RegistroForestal) -> None:
        """
        Agrega una finca al servicio.
        
        Args:
            registro: Registro forestal de la finca
        """
        self._registros[registro.get_id_padron()] = registro
    
    def buscar_finca(self, id_padron: int) -> RegistroForestal:
        """
        Busca una finca por su ID de padron.
        
        Args:
            id_padron: ID del padron catastral
            
        Returns:
            RegistroForestal: Registro de la finca
            
        Raises:
            KeyError: Si no existe finca con ese padron
        """
        if id_padron not in self._registros:
            raise KeyError(f"No existe finca con padron {id_padron}")
        return self._registros[id_padron]
    
    def fumigar(self, id_padron: int, plaguicida: str) -> None:
        """
        Fumiga todos los cultivos de una finca.
        
        Args:
            id_padron: ID del padron de la finca a fumigar
            plaguicida: Tipo de plaguicida a aplicar
        """
        registro = self.buscar_finca(id_padron)
        print(f"Fumigando plantacion con: {plaguicida}")
        # En una implementacion real, aqui se aplicaria el plaguicida a cada cultivo
    
    def cosechar_yempaquetar(self, tipo_cultivo: Type[T]) -> Paquete[T]:
        """
        Cosecha todos los cultivos de un tipo especifico de todas las fincas
        y los empaqueta en un Paquete generico tipo-seguro.
        
        Args:
            tipo_cultivo: Clase del tipo de cultivo a cosechar
            
        Returns:
            Paquete[T]: Paquete con los cultivos cosechados
        """
        paquete: Paquete[T] = Paquete()
        
        for registro in self._registros.values():
            plantacion = registro.get_plantacion()
            cultivos_a_cosechar = [
                c for c in plantacion.cultivos
                if isinstance(c, tipo_cultivo)
            ]
            
            # Remover de la plantacion y agregar al paquete
            for cultivo in cultivos_a_cosechar:
                plantacion.cultivos.remove(cultivo)
                paquete.agregar_item(cultivo)
        
        cantidad = paquete.get_cantidad()
        print(f"\nCOSECHANDO {cantidad} unidades de {tipo_cultivo}")
        
        return paquete


# ================================================================================
# ARCHIVO 3/3: paquete.py
# Ruta: /home/valentin/escritorio/diseñoDeSistemas/parcialDiseño/ParcialMendoza/PythonForestal/python_forestacion/servicios/negocio/paquete.py
# ================================================================================

# python_forestacion/servicios/negocio/paquete.py
from typing import Generic, TypeVar, List

T = TypeVar('T')


class Paquete(Generic[T]):
    """
    Paquete generico tipo-seguro para empaquetar cultivos cosechados.
    Usa Generics para garantizar type-safety.
    
    Type Parameters:
        T: Tipo de cultivo en el paquete
    
    Attributes:
        items: Lista de cultivos del mismo tipo
        id_paquete: ID unico del paquete
    """
    
    _counter = 0
    
    def __init__(self):
        Paquete._counter += 1
        self.id_paquete = Paquete._counter
        self.items: List[T] = []
    
    def agregar_item(self, item: T) -> None:
        """Agrega un cultivo al paquete"""
        self.items.append(item)
    
    def get_items(self) -> List[T]:
        """Retorna lista de cultivos en el paquete"""
        return self.items.copy()
    
    def get_cantidad(self) -> int:
        """Retorna cantidad de cultivos en el paquete"""
        return len(self.items)
    
    def get_id_paquete(self) -> int:
        """Retorna ID del paquete"""
        return self.id_paquete
    
    def mostrar_contenido_caja(self) -> None:
        """Muestra el contenido del paquete de forma detallada"""
        if not self.items:
            print("\nContenido de la caja:")
            print("  Caja vacia")
            return
        
        tipo_nombre = self.items[0].__class__.__name__
        print(f"\nContenido de la caja:")
        print(f"  Tipo: {tipo_nombre}")
        print(f"  Cantidad: {self.get_cantidad()}")
        print(f"  ID Paquete: {self.id_paquete}")


