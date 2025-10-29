class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance   # __balance is private (Encapsulation)

    # Public method to deposit money (Abstraction)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}.")
        else:
            print("Invalid deposit amount.")

    # Public method to withdraw money (Abstraction)
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}.")
        else:
            print("Insufficient balance or invalid amount.")

    # Public method to check balance (Abstraction)
    def get_balance(self):
        return f"Available balance: ₹{self.__balance}"

# -------------------------
# Real-world usage
# -------------------------
naveen_account = BankAccount("Naveen", 1000)

naveen_account.deposit(500)
naveen_account.withdraw(300)

# Trying to access private data directly (won't work)
# print(naveen_account.__balance)  ❌

# Access through public method
print(naveen_account.get_balance())
