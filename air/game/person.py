from wallet import Wallet

class Person():
    def __init__(self, initialWalletAmount) -> None:
        self._wallet = Wallet(initialWalletAmount)