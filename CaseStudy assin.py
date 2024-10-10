import datetime

class Account:
    def __init__(self, acc_no, name, initial_deposit):
        self.acc_no = acc_no
        self.name = name
        self.balance = initial_deposit
        self.transactions = []
        self.transactions.append(
            {"type": "Deposit", "amount": initial_deposit, "date": datetime.datetime.now(), "balance": self.balance})

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(
            {"type": "Deposit", "amount": amount, "date": datetime.datetime.now(), "balance": self.balance})
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.transactions.append(
                {"type": "Withdraw", "amount": amount, "date": datetime.datetime.now(), "balance": self.balance})
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def transfer(self, recipient, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            recipient.balance += amount
            self.transactions.append(
                {"type": "Transfer to " + recipient.name, "amount": amount, "date": datetime.datetime.now(), "balance": self.balance})
            recipient.transactions.append(
                {"type": "Transfer from " + self.name, "amount": amount, "date": datetime.datetime.now(), "balance": recipient.balance})
            print(f"Transferred {amount} to {recipient.name}. Your new balance: {self.balance}")

    def print_transactions(self):
        for transaction in self.transactions:
            print(f"{transaction['date']} - {transaction['type']}: {transaction['amount']}, Balance: {transaction['balance']}")

    def get_account_details(self):
        print(f"Account Number: {self.acc_no}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_no, name, initial_deposit):
        if acc_no in self.accounts:
            print("Account number already exists.")
        else:
            account = Account(acc_no, name, initial_deposit)
            self.accounts[acc_no] = account
            print(f"Account created for {name} with account number {acc_no}.")

    def view_account(self, acc_no):
        if acc_no in self.accounts:
            self.accounts[acc_no].get_account_details()
        else:
            print("Account not found.")

    def withdraw(self, acc_no, amount):
        if acc_no in self.accounts:
            self.accounts[acc_no].withdraw(amount)
        else:
            print("Account not found.")

    def deposit(self, acc_no, amount):
        if acc_no in self.accounts:
            self.accounts[acc_no].deposit(amount)
        else:
            print("Account not found.")

    def transfer_funds(self, from_acc_no, to_acc_no, amount):
        if from_acc_no in self.accounts and to_acc_no in self.accounts:
            self.accounts[from_acc_no].transfer(self.accounts[to_acc_no], amount)
        else:
            print("One or both account numbers not found.")

    def print_transactions(self, acc_no):
        if acc_no in self.accounts:
            self.accounts[acc_no].print_transactions()
        else:
            print("Account not found.")

    def exit(self):
        print("Exiting the application.")
        exit()


# Driver code for the bank app
bank = Bank()

while True:
    print("\n----- Bank App Menu -----")
    print("1. Create Account")
    print("2. View Account Details")
    print("3. Withdraw")
    print("4. Deposit")
    print("5. Fund Transfer")
    print("6. Print Transactions")
    print("7. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        acc_no = input("Enter Account Number: ")
        name = input("Enter Account Holder's Name: ")
        initial_deposit = float(input("Enter Initial Deposit: "))
        bank.create_account(acc_no, name, initial_deposit)
    
    elif choice == '2':
        acc_no = input("Enter Account Number: ")
        bank.view_account(acc_no)
    
    elif choice == '3':
        acc_no = input("Enter Account Number: ")
        amount = float(input("Enter Amount to Withdraw: "))
        bank.withdraw(acc_no, amount)
    
    elif choice == '4':
        acc_no = input("Enter Account Number: ")
        amount = float(input("Enter Amount to Deposit: "))
        bank.deposit(acc_no, amount)
    
    elif choice == '5':
        from_acc_no = input("Enter Your Account Number: ")
        to_acc_no = input("Enter Recipient Account Number: ")
        amount = float(input("Enter Amount to Transfer: "))
        bank.transfer_funds(from_acc_no, to_acc_no, amount)
    
    elif choice == '6':
        acc_no = input("Enter Account Number: ")
        bank.print_transactions(acc_no)
    
    elif choice == '7':
        bank.exit()
    
    else:
        print("Invalid choice. Please try again.")


import datetime

class Account:
    def __init__(self, acc_no, name, initial_deposit):
        self.acc_no = acc_no
        self.name = name
        self.balance = initial_deposit
        self.transactions = []
        self.transactions.append(
            {"type": "Deposit", "amount": initial_deposit, "date": datetime.datetime.now(), "balance": self.balance})

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(
            {"type": "Deposit", "amount": amount, "date": datetime.datetime.now(), "balance": self.balance})
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.transactions.append(
                {"type": "Withdraw", "amount": amount, "date": datetime.datetime.now(), "balance": self.balance})
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def transfer(self, recipient, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            recipient.balance += amount
            self.transactions.append(
                {"type": "Transfer to " + recipient.name, "amount": amount, "date": datetime.datetime.now(), "balance": self.balance})
            recipient.transactions.append(
                {"type": "Transfer from " + self.name, "amount": amount, "date": datetime.datetime.now(), "balance": recipient.balance})
            print(f"Transferred {amount} to {recipient.name}. Your new balance: {self.balance}")

    def print_transactions(self):
        for transaction in self.transactions:
            print(f"{transaction['date']} - {transaction['type']}: {transaction['amount']}, Balance: {transaction['balance']}")

    def get_account_details(self):
        print(f"Account Number: {self.acc_no}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_no, name, initial_deposit):
        if acc_no in self.accounts:
            print("Account number already exists.")
        else:
            account = Account(acc_no, name, initial_deposit)
            self.accounts[acc_no] = account
            print(f"Account created for {name} with account number {acc_no}.")

    def view_account(self, acc_no):
        if acc_no in self.accounts:
            self.accounts[acc_no].get_account_details()
        else:
            print("Account not found.")

    def withdraw(self, acc_no, amount):
        if acc_no in self.accounts:
            self.accounts[acc_no].withdraw(amount)
        else:
            print("Account not found.")

    def deposit(self, acc_no, amount):
        if acc_no in self.accounts:
            self.accounts[acc_no].deposit(amount)
        else:
            print("Account not found.")

    def transfer_funds(self, from_acc_no, to_acc_no, amount):
        if from_acc_no in self.accounts and to_acc_no in self.accounts:
            self.accounts[from_acc_no].transfer(self.accounts[to_acc_no], amount)
        else:
            print("One or both account numbers not found.")

    def print_transactions(self, acc_no):
        if acc_no in self.accounts:
            self.accounts[acc_no].print_transactions()
        else:
            print("Account not found.")

    def exit(self):
        print("Exiting the application.")
        exit()


# Driver code for the bank app
bank = Bank()

while True:
    print("\n----- Bank App Menu -----")
    print("1. Create Account")
    print("2. View Account Details")
    print("3. Withdraw")
    print("4. Deposit")
    print("5. Fund Transfer")
    print("6. Print Transactions")
    print("7. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        acc_no = input("Enter Account Number: ")
        name = input("Enter Account Holder's Name: ")
        initial_deposit = float(input("Enter Initial Deposit: "))
        bank.create_account(acc_no, name, initial_deposit)
    
    elif choice == '2':
        acc_no = input("Enter Account Number: ")
        bank.view_account(acc_no)
    
    elif choice == '3':
        acc_no = input("Enter Account Number: ")
        amount = float(input("Enter Amount to Withdraw: "))
        bank.withdraw(acc_no, amount)
    
    elif choice == '4':
        acc_no = input("Enter Account Number: ")
        amount = float(input("Enter Amount to Deposit: "))
        bank.deposit(acc_no, amount)
    
    elif choice == '5':
        from_acc_no = input("Enter Your Account Number: ")
        to_acc_no = input("Enter Recipient Account Number: ")
        amount = float(input("Enter Amount to Transfer: "))
        bank.transfer_funds(from_acc_no, to_acc_no, amount)
    
    elif choice == '6':
        acc_no = input("Enter Account Number: ")
        bank.print_transactions(acc_no)
    
    elif choice == '7':
        bank.exit()
    
    else:
        print("Invalid choice. Please try again.")
