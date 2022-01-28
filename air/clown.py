from air_tank import Tank
from balloon import Balloon
import random

class Clown:
    def __init__(self):
        self.tank = Tank("Helium")
        self.money = 0

    def buy_balloon(self, cost):
        color_options = ["Red", "Green", "Blue", "Yellow"]
        balloon = Balloon(color_options[random.randint(0, len(color_options)-1)])

        balloon.fill(self.tank.release_air(500))
        balloon.seal()
        self.money += cost
        return balloon

