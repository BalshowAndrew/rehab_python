"""Smart Wallet"""

class Wallet:
    """Class Wallet"""
    def __init__(self, name, balance=0):
        self.name = name
        self._balance = balance
    
    def info(self):
        print(f"{self.name}, баланс: {self._balance}")
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Сумма должна быть положительной")        
    
    def spend(self, amount):
        if amount < 0:
            print("Сумма должна быть положительной")
            return
        
        if self._balance >= amount:
            self._balance -= amount
            print(f"Потрачено {amount}")
        else:
            print("Недостаточно средств")
                


my_wallet = Wallet('Andrew', 100_000)

my_wallet.info()
my_wallet.deposit(250)
my_wallet.info()
my_wallet.deposit(-390)
my_wallet.info()
my_wallet.spend(500)
my_wallet.info()
my_wallet.spend(200_000)
my_wallet.info()
my_wallet.spend(-1500)
my_wallet.info()
