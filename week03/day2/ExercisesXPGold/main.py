class AmountException(Exception):
    pass


class SecurityException(Exception):
    pass


class BankAccount:
    def __init__(self, balance=0, username="", password="", authenticated=False):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = authenticated

    def deposit(self, amount):
        if self.authenticated:
            if amount > 0:
                self.balance += amount
            else:
                raise AmountException("The amount is not positive")
        else:
            raise SecurityException("The user is not authenticated")

    def withdraw(self, amount):
        if self.authenticated:
            if amount > 0:
                self.balance -= amount
            else:
                raise AmountException("The amount is not positive")
        else:
            raise SecurityException("The user is not authenticated")

    def authenticate(self, username, password):
        if username == self.username and password == self.password:
            self.authenticated = True


class MinimumBalanceAccount(BankAccount):
    def __init__(self, *args, minimum_balance=0):
        super().__init__(*args)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount > self.minimum_balance:
            self.balance -= amount
        else:
            raise AmountException("The amount should remain higher than the minimum balance")


class ATM:
    def __init__(self, account_list, try_limit):
        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0
        self.show_main_menu()

    def show_account_menu(self, current_account):
        current_account.authenticated = True
        while True:
            print("Hello,", current_account.username)
            print("""
Your menu:
1: Withdraw
2: Deposit
3: Show balance
q: Exit        
            """)
            current_action = input("Enter your choice: ")
            if current_action == '1':
                amount = ""
                while not amount.isnumeric():
                    amount = input("Enter the amount to withdraw: ")
                current_account.withdraw(int(amount))
            elif current_action == '2':
                amount = ""
                while not amount.isnumeric():
                    amount = input("Enter the amount to deposit: ")
                current_account.deposit(int(amount))
            elif current_action == '3':
                print("Your current balance is", current_account.balance)
            elif current_action.lower() == 'q':
                break

    def log_in(self, in_username, in_password):
        first_found = list(filter(lambda e: e.username == in_username and e.password == in_password, self.account_list))
        if len(first_found) > 0:
            self.current_tries = 0
            self.show_account_menu(first_found[0])
        else:
            if self.current_tries < self.try_limit:
                self.current_tries += 1
                self.show_main_menu()
            else:
                print("You have reached max tries. Bye-bye")

    def show_main_menu(self):
        input_username = input("Enter your username: ")
        input_password = input("Enter your password: ")
        self.log_in(input_username, input_password)


user1 = BankAccount(0, 'a', 'b')
user1.authenticate('a', 'b')
user1.deposit(10)
user1.withdraw(5)
print(user1.balance)

user2 = MinimumBalanceAccount(0, 'c', 'd', True, minimum_balance=6)
user2.deposit(20)
user2.withdraw(5)
print(user2.balance)

my_atm = ATM([user1, user2], 3)
