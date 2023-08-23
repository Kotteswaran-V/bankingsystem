class BankAccount:
    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount:.2f} units. New balance: {self.balance:.2f}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrew {amount:.2f} units. New balance: {self.balance:.2f}"
        else:
            return "Insufficient funds"

    def get_balance(self):
        return f"Current balance: {self.balance:.2f}"

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, owner, initial_balance=0.0):
        if account_number in self.accounts:
            return "Account number already exists"
        account = BankAccount(account_number, owner, initial_balance)
        self.accounts[account_number] = account
        return "Account created successfully"

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            return "Account not found"


bank = Bank()

while True:
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        account_number = input("Enter account number: ")
        owner = input("Enter account owner's name: ")
        initial_balance = float(input("Enter initial balance: "))
        result = bank.create_account(account_number, owner, initial_balance)
        print(result)
    
    elif choice == "2":
        account_number = input("Enter account number: ")
        amount = float(input("Enter deposit amount: "))
        account = bank.get_account(account_number)
        if isinstance(account, BankAccount):
            result = account.deposit(amount)
            print(result)
        else:
            print(account)
    
    elif choice == "3":
        account_number = input("Enter account number: ")
        amount = float(input("Enter withdrawal amount: "))
        account = bank.get_account(account_number)
        if isinstance(account, BankAccount):
            result = account.withdraw(amount)
            print(result)
        else:
            print(account)
    
    elif choice == "4":
        account_number = input("Enter account number: ")
        account = bank.get_account(account_number)
        if isinstance(account, BankAccount):
            result = account.get_balance()
            print(result)
        else:
            print(account)
    
    elif choice == "5":
        print("Exiting...")
        break
    
    else:
        print("Invalid choice, please select a valid option.")
