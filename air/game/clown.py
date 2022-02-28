from game.air_tank import AirTank
from game.wallet import Wallet
from game.balloon import Balloon
from game.clown_car import ClownCar
from game.person import Person
import random

class Clown(Person):
    def __init__(self) -> None:
        super().__init__(25)
        self.__helium_tank = AirTank("Helium")
        self.__car = ClownCar()

        self.__helium_tank.fill()
        self.__car.fillTank()

    def buy_balloon(self, cost) -> Balloon:
        color_options = ["Red", "Green", "Blue", "Yellow"]
        balloon = Balloon(color_options[random.randint(0, len(color_options)-1)])

        balloon.fill(self.__helium_tank.release_air(500))
        balloon.seal()

        super()._wallet.add_transaction(cost)

        return balloon
    
    def __str__(self) -> str:
        if self.__helium_tank.checkVolume():
            return f"Clown (${self._wallet.get_balance():.2f}) with a full tank"
        else:
            return f"Clown (${self._wallet.get_balance():.2f}) with an empty tank"

