# python_forestacion/excepciones/forestacion_exception.py

class ForestacionException(Exception):
    """
    Excepcion base para todas las excepciones del sistema de gestion forestal.
    Proporciona mensajes separados para usuario y tecnico.
    
    Attributes:
        user_message: Mensaje amigable para el usuario
        technical_message: Mensaje tecnico detallado para debugging
    """
    
    def __init__(self, user_message: str, technical_message: str = ""):
        self.user_message = user_message
        self.technical_message = technical_message or user_message
        super().__init__(self.user_message)
    
    def get_user_message(self) -> str:
        """Retorna el mensaje para el usuario"""
        return self.user_message
    
    def get_technical_message(self) -> str:
        """Retorna el mensaje tecnico"""
        return self.technical_message
