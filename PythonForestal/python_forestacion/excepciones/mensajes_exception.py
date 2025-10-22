# python_forestacion/excepciones/mensajes_exception.py
from python_forestacion.excepciones.forestacion_exception import ForestacionException


class MensajesException(ForestacionException):
    """
    Excepción para errores relacionados con mensajes y comunicaciones del sistema.
    """
    
    def __init__(self, user_message: str, technical_message: str = None):
        super().__init__(user_message, technical_message or user_message)
