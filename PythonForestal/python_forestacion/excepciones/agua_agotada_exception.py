# python_forestacion/excepciones/agua_agotada_exception.py
from python_forestacion.excepciones.forestacion_exception import ForestacionException


class AguaAgotadaException(ForestacionException):
    """
    Excepción lanzada cuando no hay suficiente agua disponible para regar.
    
    Attributes:
        agua_requerida: Cantidad de agua necesaria
        agua_disponible: Cantidad de agua disponible
    """
    
    def __init__(
        self,
        agua_requerida: int,
        agua_disponible: int,
        user_message: str = None,
        technical_message: str = None
    ):
        if user_message is None:
            user_message = f"No hay suficiente agua. Requerida: {agua_requerida}L, Disponible: {agua_disponible}L"
        
        if technical_message is None:
            technical_message = f"AguaAgotadaException: requerida={agua_requerida}, disponible={agua_disponible}"
        
        super().__init__(user_message, technical_message)
        self.agua_requerida = agua_requerida
        self.agua_disponible = agua_disponible
    
    def get_agua_requerida(self) -> int:
        return self.agua_requerida
    
    def get_agua_disponible(self) -> int:
        return self.agua_disponible
