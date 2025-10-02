class BankAccount:
    def __init__(self, initial_account = 0):
        self.account_balance = initial_account

    def deposit(self, amount):
        self.account_balance += amount
        return (f"deposited {amount} successfully!. New Balance = {self.account_balance}")

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return  True
        else:
            return False

    def display_balance(self):
        print(f'current Balance: ${self.account_balance}')

