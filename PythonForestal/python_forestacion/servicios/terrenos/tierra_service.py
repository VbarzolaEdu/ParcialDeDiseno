# python_forestacion/servicios/terrenos/tierra_service.py
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion


class TierraService:
    """
    Servicio para gestion de terrenos.
    Proporciona metodos para crear y gestionar tierras con plantaciones.
    """
    
    def crear_tierra(self, id_padron_catastral: int, superficie: float, domicilio: str) -> Tierra:
        """
        Crea un nuevo terreno.
        
        Args:
            id_padron_catastral: Numero de padron unico
            superficie: Superficie en metros cuadrados
            domicilio: Direccion del terreno
            
        Returns:
            Tierra: Terreno creado
            
        Raises:
            ValueError: Si la superficie es <= 0
        """
        return Tierra(
            id_padron_catastral=id_padron_catastral,
            superficie=superficie,
            domicilio=domicilio
        )
    
    def crear_tierra_con_plantacion(
        self,
        id_padron_catastral: int,
        superficie: float,
        domicilio: str,
        nombre_plantacion: str,
        agua_disponible: int = 500
    ) -> Tierra:
        """
        Crea un terreno con una plantacion asociada.
        
        Args:
            id_padron_catastral: Numero de padron unico
            superficie: Superficie en metros cuadrados
            domicilio: Direccion del terreno
            nombre_plantacion: Nombre de la plantacion
            agua_disponible: Agua disponible inicial (default: 500L)
            
        Returns:
            Tierra: Terreno con plantacion asociada
        """
        tierra = self.crear_tierra(id_padron_catastral, superficie, domicilio)
        
        plantacion = Plantacion(
            nombre=nombre_plantacion,
            superficie_max=superficie,
            agua_disponible=agua_disponible
        )
        
        tierra.set_finca(plantacion)
        return tierra
