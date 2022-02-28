from game.gas_tank import GasTank

class ClownCar():
    def __init__(self) -> None:
        self._tank = GasTank()
    
    def fill_tank(self) -> None:
        self._tank.fill()