class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def subtract(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __sub__(self, other):
        """Allows us to write point3 = point1 - point2"""
        return self.subtract(other)

    def __pow__(self, num):
        """Allow using ** """
        return Point(self.x ** num, self.y ** num)

    def distance(self, other):
        diff = (self - other) ** 2
        return (diff.x + diff.y) ** 0.5

    def __repr__(self):
        return f'<Point {self.x}, {self.y}>'

    def __str__(self):
        """Returns a nicely readable format when we call print()"""
        # Remember, this is just shorthand:
        # return "Point (x: " + str(self.x) + ", y: " + str(self.y) + ")"
        return f'Point (x: {self.x}, y: {self.y})'

origin = Point(0, 0)
campus = Point(6, 8)

class BaseAccount:
    """Create named accounts with a balance that is
    - increased by account_deposit
    - decreased by account_withdrawl
    """
    # Class attributes outside and class defs
    # These are "intended" private.
    _account_number_seed = 1000
    bank_name = 'Berkeley'
    _all_accounts = []

    # Constructor
    def __init__(self, name, initial_deposit=0):
        # Initialize the instance attributes
        self._name = name
        # Call an attribute on the /class/
        self._acct_no = BaseAccount._account_number_seed
        # this is shared across all instances
        BaseAccount._account_number_seed += 1
        self._balance = initial_deposit
        BaseAccount._all_accounts.append(self)

    # Selectors
    def account_name(self):
        return self._name

    def account_balance(self):
        return self._balance

    def account_number(self):
        return self._acct_no

    # Operations
    def deposit(self, amount):
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        self._balance -= amount
        return self._balance

    def account_type(self):
        return "BaseAccount"

    # Display representation
    def __repr__(self):
        return f'<{self.account_type()}: {self.account_name()}-{self.account_number()}>'

    # Print representation
    def __str__(self):
        return f'{self.account_type()}: {self.account_name()}-{self.account_number()} Balance: {self._balance}'

    # Notice this doesn't use self!
    def show_accounts():
        for account in BaseAccount._all_accounts:
            print(account)

    # What if we wanted to manage all accounts?
    def all_accounts():
        return BaseAccount._all_accounts

class CheckingAccount(BaseAccount):
    def __init__(self, name, initial_deposit):
        # Use superclass initializer
        # BaseAccount.__init__(self, name, initial_deposit)
        # Preferably:
        super().__init__(name, initial_deposit)
        # Additional initialization
        self._type = "Checking"

    def account_type(self):
        return f"{self._type}Account"

    # Just for debugging / example:
    def show_superclass(self):
        return super()

class SavingsAccount(BaseAccount):
    interest_rate = 0.05

    def __init__(self, name, initial_deposit):
        # Use superclass initializer
        super().__init__(name, initial_deposit)
        # BaseAccount.__init__(self, name, initial_deposit)
        # Additional initialization
        self._type = "Savings"

    def account_type(self):
        return f"{self._type}Account"

    def accrue_interest(self):
        self._balance = self._balance * (1 + SavingsAccount.interest_rate)

    # Display representation
    def __repr__(self):
        return f'<{self.account_type()}: {self.account_name()}-{self.account_number()} @ {SavingsAccount.interest_rate * 100}%>'

    # Print representation
    def __str__(self):
        return f"{super().__str__()} @ {SavingsAccount.interest_rate * 100}%"


cs88 = CheckingAccount('CS88', 1000)
cs88_savings = SavingsAccount('CS88', 1000)



################################
# (su24 things)
################################



class Car:
    pass

class SportsCar:
    pass

class SUV:
    pass

class Tank:
    pass

class Boat:
    pass

class Person:
    def __init__(self, age):
        self.age = age
    def have_birthday(self):
        self.age += 1
        return f"Now I'm one year older: {self.age}!"
    def have_fun(self):
        return "Whee!"

class Employee(Person):
    def __init__(self, age, company_name):
        super().__init__(age)
        self.company_name = company_name
    def have_birthday(self):
        out_super = super().have_birthday()
        return out_super + f" Well, time for work at {self.company_name}!"
    def have_fun(self):
        return f"I can't have fun, I have to work at {self.company_name}!"

youngster = Person(10)
print(youngster.have_birthday())
print(youngster.have_fun())

employee = Employee(35, "BigCorp")
print(employee.have_birthday())
print(employee.have_fun())

# Composing classes

# Here is a BaseAccount that remembers all accounts created via
# the class variable `_all_accounts`
# Suggestion: let's refactor the class vars into a separate class
# `Bank`!
class BaseAccount:
    """Create named accounts with a balance that is
    - increased by account_deposit
    - decreased by account_withdrawl
    """
    # Class attributes outside and class defs
    # These are "intended" private.
    _account_number_seed = 1000
    bank_name = 'Berkeley'
    _all_accounts = []

    # Constructor
    def __init__(self, name, initial_deposit=0):
        # Initialize the instance attributes
        self._name = name
        # Call an attribute on the /class/
        self._acct_no = BaseAccount._account_number_seed
        # this is shared across all instances
        BaseAccount._account_number_seed += 1
        self._balance = initial_deposit
        BaseAccount._all_accounts.append(self)

    # Selectors
    def account_name(self):
        return self._name

    def account_balance(self):
        return self._balance

    def account_number(self):
        return self._acct_no

    # Operations
    def deposit(self, amount):
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        self._balance -= amount
        return self._balance

    def account_type(self):
        return "BaseAccount"

    # Display representation
    def __repr__(self):
        return f'<{self.account_type()}: {self.account_name()}-{self.account_number()}>'

    # Print representation
    def __str__(self):
        return f'{self.account_type()}: {self.account_name()}-{self.account_number()} Balance: {self._balance}'

    # Notice this doesn't use self!
    def show_accounts():
        for account in BaseAccount._all_accounts:
            print(account)

    # What if we wanted to manage all accounts?
    def all_accounts():
        return BaseAccount._all_accounts

account_a = BaseAccount("account_a", 100)
account_b = BaseAccount("account_b", 50)
print(BaseAccount.all_accounts())

# (Composing) let's define the Bank class
# Notably: each Bank class has its own accounts + account_number_seed
# as instance variables, NOT class variables!

class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = []
        self._account_number_seed = 1000
    
    def add_account(self, account):
        account._acct_no = self._account_number_seed
        self._account_number_seed += 1
        self.accounts.append(account)

    def show_accounts(self):
        for account in self.accounts:
            print(account)


class BaseAccount2:
    """Create named accounts with a balance that is
    - increased by account_deposit
    - decreased by account_withdrawl
    """

    # Constructor
    def __init__(self, name, bank, initial_deposit=0):
        # Initialize the instance attributes
        self._name = name
        self._bank = bank
        # _acct_no will be set by bank.add_account()
        self._acct_no = None
        bank.add_account(self)
        self._balance = initial_deposit

    # Selectors
    def account_name(self):
        return self._name

    def account_balance(self):
        return self._balance

    def account_number(self):
        return self._acct_no

    # Operations
    def deposit(self, amount):
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        self._balance -= amount
        return self._balance

    def account_type(self):
        return "BaseAccount"

    # Display representation
    def __repr__(self):
        return f'<{self.account_type()}: {self.account_name()}-{self.account_number()}>'

    # Print representation
    def __str__(self):
        return f'{self.account_type()}: {self.account_name()}-{self.account_number()} Balance: {self._balance}'

    def __add__(self, other_account):
        name_concat = self.account_name() + "_AND_" + other_account.account_name()
        combined_balance = self.account_balance() + other_account.account_balance()
        bank = self._bank  # arbitrarily choose LHS bank
        return BaseAccount2(name_concat, bank, combined_balance)

print("Composing bank")
bank_of_toad = Bank("bank_of_toad")

account_a = BaseAccount2("account_a", bank_of_toad, 100)
account_b = BaseAccount2("account_b", bank_of_toad, 50)

print("Bank of Toad accounts")
bank_of_toad.show_accounts()

bank_of_wario = Bank("bank_of_wario")
account_c = BaseAccount2("account_c", bank_of_wario, 9999)
account_d = BaseAccount2("account_d", bank_of_wario, 1)

# Note that each bank has its own "account_id" namespace.
# This is because each Bank has _account_number_seed as an instance
# var, not a (shared) class var.
print("Bank of Wario Accounts")
bank_of_wario.show_accounts()
print("Bank of Toad accounts")
bank_of_toad.show_accounts()

# (Demo) magic methods __str__ vs __repr__, __add__
print("Magic methods")
print(account_c)
print(str(account_c))

"""
# Tip: __repr__ vs __str__

# Python interpreter outputs repr()
>>> account_c
<BaseAccount: account_c-1000>
# print() calls str()
>>> print(account_c)
BaseAccount: account_c-1000 Balance: 9999
>>> str(account_c)
'BaseAccount: account_c-1000 Balance: 9999'
>>> repr(account_c)
'<BaseAccount: account_c-1000>'
"""

account_c_d = account_c + account_d
print("account_c + account_d")
print(account_c_d)
print("Bank of Wario accounts")
bank_of_wario.show_accounts()
