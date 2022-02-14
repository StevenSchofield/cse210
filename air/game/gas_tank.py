import imp
from mimetypes import init
from game.tank import Tank

class GasTank(Tank):
    def __init__(self):
        super().__init__(50)