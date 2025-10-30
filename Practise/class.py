class BankAccount:
    # Class variable: shared by all accounts
    bank_name = "Global Trust Bank"
    interest_rate = 4.5  # same for all accounts (in percentage)

    def __init__(self, account_holder, balance):
        # Instance variables: unique for each account
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.account_holder} deposited ₹{amount}. New balance: ₹{self.balance}")

    def display_details(self):
        print(f"Bank: {BankAccount.bank_name}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ₹{self.balance}")
        print(f"Interest Rate: {BankAccount.interest_rate}%")


acc1 = BankAccount("Alice", 10000)
acc2 = BankAccount("Bob", 5000)

acc1.deposit(2000)
acc2.deposit(1000)

# Change class variable
BankAccount.interest_rate = 5.0

print("\nAccount 1 Details:")
acc1.display_details()

print("\nAccount 2 Details:")
acc2.display_details()
