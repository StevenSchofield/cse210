from game.tank import Tank

class AirTank(Tank):
    def __init__(self, air_type):
        self._air_type = air_type
        super().__init__(25)

    def release_air(self, volume_ml):
        return super().release(volume_ml)