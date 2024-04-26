from bank import Bank
from admin import Admin
from users import User

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
