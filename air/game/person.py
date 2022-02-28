from game.wallet import Wallet

class Person():
    def __init__(self, initialWalletAmount=0) -> None:
        self._wallet = Wallet(initialWalletAmount)
    
    def speak(self):
        return "Hello world"