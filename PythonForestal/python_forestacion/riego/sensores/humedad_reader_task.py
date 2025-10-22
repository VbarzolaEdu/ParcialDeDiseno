# python_forestacion/riego/sensores/humedad_reader_task.py
import threading
import time
import random
from typing import Optional
from python_forestacion.patrones.observer.observable import Observable

class HumedadReaderTask(Observable[float], threading.Thread):
    """
    Sensor simulado de humedad (%).
    Notifica valores 0..100 cada intervalo (segundos).
    """
    def __init__(self, intervalo: float = 5.0, min_hum: float = 0.0, max_hum: float = 100.0):
        Observable.__init__(self)
        threading.Thread.__init__(self, daemon=True)
        self.intervalo = intervalo
        self._stop_event = threading.Event()
        self.min_hum = min_hum
        self.max_hum = max_hum

    def run(self):
        while not self._stop_event.is_set():
            hum = round(random.uniform(self.min_hum, self.max_hum), 2)
            self.notificar_observadores(hum)
            time.sleep(self.intervalo)

    def stop(self):
        self._stop_event.set()
