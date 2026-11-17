class BankAccount:

    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self.__balance = 0
def credit(self, amount):
        self.__balance += amount
        print("Credited:", amount)
def debit(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Debited:", amount)
        else:
            print("Insufficient balance")

def show_balance(self):
        print("Balance:", self.__balance)
acc = BankAccount("Kaif", "12345")
acc.credit(5000)
acc.debit(2000)
acc.show_balance()