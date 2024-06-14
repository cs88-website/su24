class Test:
    def __init__(self, value):
        self.__value = value

    def show_value(self):
        return self.__value

# Our Point ADT
def point(x, y): # our point ADT
	return { 'x': x, 'y': y}

def x(point):
    return point['x']

def y(point):
    return point['y']

def subtract(p1, p2):
    return point(x(p2) - x(p1), y(p2) - y(p1))

origin = point(0, 0)
type(origin)

##### The Point type
class Point:
    class PointError(Exception):
        pass

    def __init__(self, x, y):
        self.x = x
        self.y = y

    subtract = lambda self, other: Point(self.x - other.x, self.y - other.y)

    def __sub__(self, other):
        """Allows us to write point3 = point1 - point2"""
        return self.subtract(other)

    def distance(self, other):
        diff = self - other
        return (diff.x ** 2 + diff.y ** 2) ** 0.5

my_house = Point(5, 5)
my_house.x
type(my_house)

# TODAY: We will not use all the features of the this class.
# _name is just a *convention* to communicate something internal.
# __name makes the name 'private' to this class, which means it can't be easily accessed.

class BaseAccount:
    def __init__(self, name, initial_deposit=0):
        self.name = name
        self.balance = initial_deposit

    def account_name(self):
        return self.name

    def balance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    # We don't cover this synatx, but this is a common python tool to describe data that doesn't change.
    # @property
    # def name(self):
    #     return self.name

## BaseAccount with private attributes. This prevents them from being accessed outside of the class.
# class BaseAccount:
#     def __init__(self, name, initial_deposit=0):
#         self.__name = name
#         self.__balance = initial_deposit

#     def account_name(self):
#         return self.__name

#     def balance(self):
#         return self.__balance

#     def withdraw(self, amount):
#         self.__balance -= amount
#         return self.__balance

#     def deposit(self, amount):
#         self.__balance += amount
#         return self.__balance

#    # This allows us to write account.name as an attribute
#    # we don't cover @property in 88C, but it may be useful
#    @property
#    def name(self):
#        return self.__name



# Make a new account
my_account = BaseAccount('CS88', 100)
# Access Data
# my_account._balance
my_account.balance()
# notice how we we calling the class itself.
# my_account is the self in the balance method.
BaseAccount.balance(my_account)

cs88 = BaseAccount('CS88', 100)
data8 = BaseAccount('DATA8', 100)

data8.withdraw(25)

#data8.balance()
cs88.balance()

# This account uses _ as a convention for internal data.
class BaseAccount2:
    account_number_seed = 1000
    accounts_list = []

    def __init__(self, name, initial_deposit=0):
        self._name = name
        self._balance = initial_deposit
        self._acct_no = BaseAccount2.account_number_seed
        BaseAccount2.account_number_seed += 1
        BaseAccount2.accounts_list += [self]

    def name(self):
        return self._name

    def balance(self):
        return self._balance

    def withdraw(self, amount):
        self._balance -= amount
        return self._balance

    def deposit(self, amount):
        self._balance += amount
        return self._balance

    def account_no(self):
        return self._acct_no

    # Can optionally use @classmethod
    def accounts():
        return BaseAccount2.accounts_list

    def show_accounts():
        for account in BaseAccount2.accounts():
            print(account.name(),
                  account.account_no(),account.balance())


data100 = BaseAccount2('DATA100')
cs61b = BaseAccount2('CS61B')

# print(data100.account_no())

# print(cs61b.account_no())

BaseAccount2.account_number_seed
# print(BaseAccount2.show_accounts())
