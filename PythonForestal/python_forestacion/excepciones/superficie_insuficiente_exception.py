# python_forestacion/excepciones/superficie_insuficiente_exception.py
from python_forestacion.excepciones.forestacion_exception import ForestacionException


class SuperficieInsuficienteException(ForestacionException):
    """
    Excepción lanzada cuando no hay suficiente superficie disponible para plantar.
    
    Attributes:
        superficie_requerida: Superficie necesaria
        superficie_disponible: Superficie disponible
    """
    
    def __init__(
        self,
        superficie_requerida: float,
        superficie_disponible: float,
        user_message: str = None,
        technical_message: str = None
    ):
        if user_message is None:
            user_message = f"No hay suficiente superficie. Requerida: {superficie_requerida}m², Disponible: {superficie_disponible}m²"
        
        if technical_message is None:
            technical_message = f"SuperficieInsuficienteException: requerida={superficie_requerida}, disponible={superficie_disponible}"
        
        super().__init__(user_message, technical_message)
        self.superficie_requerida = superficie_requerida
        self.superficie_disponible = superficie_disponible
    
    def get_superficie_requerida(self) -> float:
        return self.superficie_requerida
    
    def get_superficie_disponible(self) -> float:
        return self.superficie_disponible
