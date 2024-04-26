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