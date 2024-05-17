class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Your balance is:", self.balance)

class User:
    def __init__(self, name, account):
        self.name = name
        self.account = account

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    def display_details(self):
        print("User name:", self.name)
        self.account.display_balance()

# Create a BankAccount object
account = BankAccount(1000)

# Create a User object associated with the BankAccount object
user = User("John Doe", account)

# Display user details
user.display_details()

# Deposit money
user.account.deposit(500)

# Display user details after deposit
user.display_details()

# Withdraw money
user.account.withdraw(200)

# Display user details after withdrawal
user.display_details()