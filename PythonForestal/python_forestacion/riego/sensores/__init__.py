# python_forestacion/riego/sensores/__init__.py
# python_forestacion/riego/sensores/__init__.py

from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask

__all__ = ['TemperaturaReaderTask', 'HumedadReaderTask']
