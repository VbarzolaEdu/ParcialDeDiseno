# python_forestacion/excepciones/persistencia_exception.py
from python_forestacion.excepciones.forestacion_exception import ForestacionException


class PersistenciaException(ForestacionException):
    """
    Excepcion para errores de persistencia de datos.
    Proporciona informacion detallada sobre el error.
    
    Attributes:
        nombre_archivo: Nombre del archivo involucrado
        tipo_operacion: Tipo de operacion (LECTURA o ESCRITURA)
    """
    
    def __init__(
        self,
        user_message: str,
        technical_message: str,
        nombre_archivo: str = "",
        tipo_operacion: str = "DESCONOCIDA"
    ):
        super().__init__(user_message, technical_message)
        self.nombre_archivo = nombre_archivo
        self.tipo_operacion = tipo_operacion
    
    def get_nombre_archivo(self) -> str:
        """Retorna el nombre del archivo involucrado"""
        return self.nombre_archivo
    
    def get_tipo_operacion(self) -> str:
        """Retorna el tipo de operacion"""
        return self.tipo_operacion
