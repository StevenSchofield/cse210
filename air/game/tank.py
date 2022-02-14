class Tank:
    def __init__(self, max_volume_L):
        self._volume_L = 0
        self._max_volume_L = max_volume_L
    
    def get_max_volume(self):
        return self._max_volume_L

    def release(self, volume_ml):
        amount = volume_ml/1000
        if amount <= self._volume_L:
            self._volume_L -= amount
        else:
            amount = self._volume_L
            self._volume_L = 0
        return amount * 1000

    def fill(self):
        self._volume_L = self._max_volume_L
    
    def checkVolume(self):
        return self._volume_L > 0
