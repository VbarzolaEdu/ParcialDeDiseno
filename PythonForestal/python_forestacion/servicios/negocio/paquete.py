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
