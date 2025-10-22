# python_forestacion/riego/sensores/temperatura_reader_task.py
import threading
import time
import random
from typing import Optional
from python_forestacion.patrones.observer.observable import Observable

class TemperaturaReaderTask(Observable[float], threading.Thread):
    """
    Sensor simulado de temperatura.
    Hereda de Observable[float] y de Thread.
    Notifica la temperatura como float a sus observadores cada intervalo (segundos).
    """
    def __init__(self, intervalo: float = 5.0, min_temp: float = 0.0, max_temp: float = 40.0):
        Observable.__init__(self)
        threading.Thread.__init__(self, daemon=True)
        self.intervalo = intervalo
        self._stop_event = threading.Event()
        self.min_temp = min_temp
        self.max_temp = max_temp

    def run(self):
        while not self._stop_event.is_set():
            # Aquí se simula la lectura; en integración real reemplazar por lectura del sensor
            temp = round(random.uniform(self.min_temp, self.max_temp), 2)
            # notificar a observadores
            self.notificar_observadores(temp)
            time.sleep(self.intervalo)

    def stop(self):
        self._stop_event.set()
