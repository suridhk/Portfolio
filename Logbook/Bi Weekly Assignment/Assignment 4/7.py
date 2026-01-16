'''
7.Write a class called BankAccount with methods:
deposit(amount)
withdraw(amount)
get_balance()
Handle the case where a withdrawal exceeds the available balance using exception
handling.
'''

# BankAccount class program

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    # Withdraw money with exception handling
    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise ValueError("Insufficient balance!")
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        except ValueError as e:
            print("Error:", e)

    # Get current balance
    def get_balance(self):
        return self.balance


# Example usage
account = BankAccount()

account.deposit(1000)
account.withdraw(500)
account.withdraw(600)  # This will raise an exception
print("Current Balance:", account.get_balance())
