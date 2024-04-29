import random

class Bank:
    def __init__(self,name):
        self.name = name
        self.users = {}
        self.admin_password = "admin123"
        self.loan_feature = True
        self.total_balance = 0
        self.total_loan_amount = 0

    def create_account(self, name, email, address, account_type):
        account_number = random.randint(10000, 99999)
        if account_number not in self.users:
            self.users[account_number] = {'name': name, 'email': email, 'address': address, 'account_type': account_type, 'balance': 0, 'loan_taken': 0, 'transaction_history': []}
            print("Account created successfully! Your account number is:", account_number)
        else:
            print("Account number already exists. Please try again.")

    def deposit(self, account_number, amount):
        if account_number in self.users:
            if amount > 0:
                self.users[account_number]['balance'] += amount
                self.total_balance += amount
                self.users[account_number]['transaction_history'].append(f"Deposited ${amount}")
                print("Amount deposited successfully.")
            else:
                print("Invalid amount for deposit.")
        else:
            print("Account does not exist.")


    def withdraw(self, account_number, amount):
        if account_number in self.users:
            if amount <= self.users[account_number]['balance']:
                self.users[account_number]['balance'] -= amount
                self.total_balance -= amount
                self.users[account_number]['transaction_history'].append(f"Withdrew ${amount}")
                print("Amount withdrawn successfully.")
            else:
                print("Withdrawal amount exceeded.")
        else:
            print("Account does not exist.")

    def check_balance(self, account_number):
        if account_number in self.users:
            return self.users[account_number]['balance']
        else:
            print("Account does not exist.")

    def check_transaction_history(self, account_number):
        if account_number in self.users:
            return self.users[account_number]['transaction_history']
        else:
            print("Account does not exist.")

    def take_loan(self, account_number, amount):
        if account_number in self.users:
            if self.users[account_number]['loan_taken'] < 2 and self.loan_feature:
                self.users[account_number]['balance'] += amount
                self.users[account_number]['loan_taken'] += 1
                self.total_loan_amount += amount
                self.users[account_number]['transaction_history'].append(f"Took a loan of ${amount}")
                print("Loan taken successfully.")
            else:
                print("You have already taken maximum loans or the loan feature is turned off.")
        else:
            print("Account does not exist.")

    def transfer(self, from_account, to_account, amount):
        if from_account in self.users and to_account in self.users:
            if amount <= self.users[from_account]['balance']:
                self.users[from_account]['balance'] -= amount
                self.users[to_account]['balance'] += amount
                self.users[from_account]['transaction_history'].append(f"Transferred ${amount} to account {to_account}")
                self.users[to_account]['transaction_history'].append(f"Received ${amount} from account {from_account}")
                print("Amount transferred successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Account does not exist.")
    
    def __repr__(self) -> str:
        return f"'{self.name}'"