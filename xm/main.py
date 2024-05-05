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


class User:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email, address, account_type):
        self.bank.create_account(name, email, address, account_type)

    def deposit(self, account_number, amount):
        self.bank.deposit(account_number, amount)

    def withdraw(self, account_number, amount):
        self.bank.withdraw(account_number, amount)

    def check_balance(self, account_number):
        return self.bank.check_balance(account_number)

    def check_transaction_history(self, account_number):
        return self.bank.check_transaction_history(account_number)

    def take_loan(self, account_number, amount):
        self.bank.take_loan(account_number, amount)

    def transfer(self, from_account, to_account, amount):
        self.bank.transfer(from_account, to_account, amount)


class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email, address, account_type):
        self.bank.create_account(name, email, address, account_type)

    def delete_account(self, account_number):
        if account_number in self.bank.users:
            del self.bank.users[account_number]
            print("Account deleted successfully.")
        else:
            print("Account does not exist.")

    def view_all_accounts(self):
        return self.bank.users

    def check_total_balance(self):
        return self.bank.total_balance

    def check_total_loan_amount(self):
        return self.bank.total_loan_amount

    def toggle_loan_feature(self):
        self.bank.loan_feature = not self.bank.loan_feature
        status = "enabled" if self.bank.loan_feature else "disabled"
        print(f"Loan feature {status}.")

bank = Bank('Dutch Bangla Bank')

while True:
    print('*** Welcome to ', bank,' ***')
    print('1. Customer')
    print('2. Admin')
    print('3. Exit')

    choice = int(input('Enter your choice: '))
    if choice == 1:
        user = User(bank)
        while True:
            print('1. Deposit')
            print('2. Withdraw')
            print('3. Transfer')
            print('4. Take Loan')
            print('5. Check Balance')
            print('6. Check Transaction History')
            print('7. Exit')

            choice = int(input('Enter your choice: '))
            if choice == 1:
                amount = float(input('Enter amount to deposit: '))
                account_number = int(input('Enter your account number: '))
                user.deposit(account_number, amount)
            elif choice == 2:
                amount = float(input('Enter amount to withdraw: '))
                account_number = int(input('Enter your account number: '))
                user.withdraw(account_number, amount)
            elif choice == 3:
                amount = float(input('Enter amount to transfer: '))
                from_account = int(input('Enter your account number: '))
                to_account = int(input('Enter recipient account number: '))
                user.transfer(from_account, to_account, amount)
            elif choice == 4:
                amount = float(input('Enter amount to take as loan: '))
                account_number = int(input('Enter your account number: '))
                user.take_loan(account_number, amount)
            elif choice == 5:
                account_number = int(input('Enter your account number: '))
                balance = user.check_balance(account_number)
                print('Your balance:', balance)
            elif choice == 6:
                account_number = int(input('Enter your account number: '))
                history = user.check_transaction_history(account_number)
                print('Transaction History:')
                for transaction in history:
                    print(transaction)
            elif choice == 7:
                break
            else:
                print('Invalid choice')
    elif choice == 2:
        admin = Admin(bank)
        while True:
            print('1. Add user')
            print('2. Delete user')
            print('3. View all accounts')
            print('4. Check total balance')
            print('5. Check total loan amount')
            print('6. Toggle loan feature')
            print('7. Exit')

            choice = int(input('Enter your choice: '))
            if choice == 1:
                name = input('Enter user name: ')
                email = input('Enter user email: ')
                address = input('Enter user address: ')
                account_type = input('Enter account type (Savings/Current): ')
                admin.create_account(name, email, address, account_type)
            elif choice == 2:
                account_number = int(input('Enter account number to delete: '))
                admin.delete_account(account_number)
            elif choice == 3:
                print(admin.view_all_accounts())
            elif choice == 4:
                total_balance = admin.check_total_balance()
                print('Total balance in the bank:', total_balance)
            elif choice == 5:
                total_loan_amount = admin.check_total_loan_amount()
                print('Total loan amount in the bank:', total_loan_amount)
            elif choice == 6:
                admin.toggle_loan_feature()
            elif choice == 7:
                break
            else:
                print('Invalid choice')
    elif choice == 3:
        print('Exiting...')
        break
    else:
        print('Invalid choice')
