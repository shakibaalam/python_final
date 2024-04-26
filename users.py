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



