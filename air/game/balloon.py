class Balloon:
    def __init__(self, color):
        self.popped = False
        self.sealed = False
        self.color = color
        self.volume_ml = 0
        self.max_volume_ml = 1000
        self.update_time_ms = 0
    
    def pop(self):
        self.popped = True
        self.volume_ml = 0

    def decrease_air(self, delta_ms):
        self.volume_ml -= (self.volume_ml/2) * delta_ms
    
    def fill(self, volume_ml):
        if not self.popped:
            self.volume_ml += volume_ml

    def seal(self):
        self.sealed = True

    def update(self, time_ms):
        delta_ms = time_ms - self.update_time_ms

        if self.popped:
            self.volume_ml = 0
        elif not self.sealed and self.volume_ml > 0:
            self.decrease_air(delta_ms)
        elif self.volume_ml > self.max_volume_ml:
            self.pop()

        self.update_time_ms = time_ms

    def __str__(self):
        if self.popped:
            return "<A mess of " + self.color + " elastic shreds>"
        else:
            return self.color + ": " + str(self.volume_ml)

