import time

class Wallet:
    class Transaction:
        def __init__(self, amount=0) -> None:
            self._amount = amount
            self._timestamp = time.time()
        
        def get_amount(self):
            return self._amount

        def __str__(self) -> str:
            return(f"{self._timestamp} --- {self._amount}")

    def __init__(self, initial_amount) -> None:
        self._transactions = []
        self._transactions.append(Wallet.Transaction(initial_amount))
    
    def add_transaction(self, tx_amount):
        self._transactions.append(Wallet.Transaction(tx_amount))
    
    def get_balance(self):
        # Return the sum of transaction amounts
        total = 0
        for tx in self._transactions:
            total  += tx.get_amount()
        
        return total
    
    def get_transactions(self):
        for tx in self._transactions:
            print(tx)