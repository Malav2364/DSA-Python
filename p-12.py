class Customer:
    def __init__(self, customer_id, name, address, contact_details):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.contact_details = contact_details


class BankAccount:
    def __init__(self, account_number, account_holder, balance=0, account_type="Savings"):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} successfully. New balance: {self.balance}")
        else:
            print("Deposit amount should be greater than 0.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawn {amount} successfully. New balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount should be greater than 0.")

    def check_balance(self):
        print(f"Account balance: {self.balance}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder, initial_balance=0, account_type="Savings"):
        if account_number not in self.accounts:
            customer = Customer(account_holder.customer_id, account_holder.name, account_holder.address,
                                account_holder.contact_details)
            account = BankAccount(account_number, customer, initial_balance, account_type)
            self.accounts[account_number] = account
            print("Account created successfully.")
        else:
            print("Account number already exists.")

    def get_account_details(self, account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            print(f"Account Number: {account.account_number}")
            print(f"Account Holder: {account.account_holder.name}")
            print(f"Balance: {account.balance}")
            print(f"Account Type: {account.account_type}")
        else:
            print("Account not found.")


# Main program
bank = Bank()

while True:
    print("\nWelcome to the Bank Management System")
    print("1.customer details")
    print("2. Create a new account")
    print("3. Deposit money")
    print("4. Withdraw money")
    print("5. Check balance")
    print("6. View account details")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        customer_id = int(input("Enter customer ID: "))
        name = input("Enter customer name: ")
        address = input("Enter customer address: ")
        contact_details = input("Enter customer contact details: ")
        customer = Customer(customer_id, name, address, contact_details)
    elif choice == '2':
        account_number = int(input("Enter account number: "))
        initial_balance = float(input("Enter initial balance: "))
        account_type = input("Enter account type (Savings/Checking): ")
        bank.create_account(account_number, customer, initial_balance, account_type)

    elif choice == '3':
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter deposit amount: "))
        bank.accounts[account_number].deposit(amount)

    elif choice == '4':
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter withdrawal amount: "))
        bank.accounts[account_number].withdraw(amount)

    elif choice == '5':
        account_number = int(input("Enter account number: "))
        bank.accounts[account_number].check_balance()

    elif choice == '6':
        account_number = int(input("Enter account number: "))
        bank.get_account_details(account_number)

    elif choice == '7':
        print("Thank you for using the Bank Management System.")
        break

    else:
        print("Invalid choice. Please try again.")