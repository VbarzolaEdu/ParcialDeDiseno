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
