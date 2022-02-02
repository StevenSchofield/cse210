from game.air_tank import Tank
from game.wallet import Wallet
from game.balloon import Balloon
import random

class Clown:
    def __init__(self) -> None:
        self._tank = Tank("Helium")
        self._wallet = Wallet(25)

        self._tank.fill()

    def buy_balloon(self, cost) -> Balloon:
        color_options = ["Red", "Green", "Blue", "Yellow"]
        balloon = Balloon(color_options[random.randint(0, len(color_options)-1)])

        balloon.fill(self._tank.release_air(500))
        balloon.seal()

        self._wallet.add_transaction(cost)

        return balloon
    
    def __str__(self) -> str:
        if self._tank.checkVolume():
            return f"Clown (${self._wallet.get_balance():.2f}) with a full tank"
        else:
            return f"Clown (${self._wallet.get_balance():.2f}) with an empty tank"

