class Balloon:
    def __init__(self, color):
        self._popped = False
        self._sealed = False
        self._color = color
        self._volume_ml = 0
        self._max_volume_ml = 1000
        self._update_time_ms = 0
    
    def pop(self):
        self._popped = True
        self._volume_ml = 0

    def decrease_air(self, delta_ms):
        self._volume_ml -= (self._volume_ml/2) * delta_ms
    
    def fill(self, volume_ml):
        if not self._popped:
            self._volume_ml += volume_ml

    def seal(self):
        self._sealed = True

    def update(self, time_ms):
        delta_ms = time_ms - self._update_time_ms

        if self._popped:
            self._volume_ml = 0
        elif not self._sealed and self._volume_ml > 0:
            self.decrease_air(delta_ms)
        elif self._volume_ml > self._max_volume_ml:
            self.pop()

        self._update_time_ms = time_ms

    def __str__(self):
        if self._popped:
            return "<A mess of " + self._color + " elastic shreds>"
        else:
            return self._color + ": " + str(self._volume_ml)

