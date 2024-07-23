## Inheritance ##

# Q1

class Account:
    """A bank account that allows deposits and withdrawals.

    >>> eric_account = Account('Eric')
    >>> eric_account.deposit(1000000)   # depositing my paycheck for the week
    1000000
    >>> eric_account.transactions
    [('deposit', 1000000)]
    >>> eric_account.withdraw(100)      # buying dinner
    999900
    >>> eric_account.transactions
    [('deposit', 1000000), ('withdraw', 100)]
    """

    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions = []

    def deposit(self, amount):
        """Increase the account balance by amount and return the
        new balance.
        """
        self.transactions.append(('deposit', amount))
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the
        new balance.
        """
        self.transactions.append(('withdraw', amount))
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance


class Check:
    """A Check object that can be deposited.

    >>> eric_check = Check("Eric", 30)  # 30 dollars, payable to Eric
    >>> eric_check.payable_to
    'Eric'
    >>> eric_check.amount
    30
    >>> eric_check.deposited
    False
    >>> eric_check.mark_deposited()
    >>> eric_check.deposited
    True
    """
    def __init__(self, payable_to, amount):
        "*** YOUR CODE HERE ***"
 
    def mark_deposited(self):
        "*** YOUR CODE HERE ***"


class CheckingAccount(Account):
    """A bank account that charges for withdrawals and can deposit checks.

    >>> check = Check("Steven", 42)  # 42 dollars, payable to Steven
    >>> steven_account = CheckingAccount("Steven")
    >>> eric_account = CheckingAccount("Eric")
    >>> eric_account.deposit_check(check)  # trying to steal steven's money
    The police have been notified.
    >>> eric_account.balance
    0
    >>> steven_account.balance
    0
    >>> check.deposited
    False
    >>> eric_account.transactions
    []
    >>> steven_account.transactions
    []
    >>> steven_account.deposit_check(check)
    42
    >>> check.deposited
    True
    >>> steven_account.transactions
    [('deposit', 42)]
    >>> steven_account.deposit_check(check)  # can't cash check twice
    The police have been notified.
    >>> steven_account.transactions  # transactions history shouldn't have changed
    [('deposit', 42)]
    """
    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)

    def deposit_check(self, check):
        "*** YOUR CODE HERE ***"


## Linked Lists ##

# Linked List Class
class Link:
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> s
    Link(1, Link(2, Link(3)))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

# Notice that this is not part of the Link class.
def print_link(link):
    """Print elements of a linked list link.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print_link(link)
    <1 2 3>
    >>> link1 = Link(1, Link(Link(2), Link(3)))
    >>> print_link(link1)
    <1 <2> 3>
    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> print_link(link1)
    <3 <4> 5 6>
    """
    print('<' + helper(link).rstrip() + '>')

def helper(link):
    if link == Link.empty:
        return ''
    elif isinstance(link.first, Link):
        return '<' + helper(link.first).rstrip() + '> ' + helper(link.rest)
    else:
        return str(link.first) +' '+  helper(link.rest)

# Q2
def list_to_link(lst):
    """Takes a Python list and returns a Link with the same elements.

    >>> link = list_to_link([1, 2, 3])
    >>> print_link(link)
    <1 2 3>
    >>> print_link(list_to_link([4]))
    <4>
    """
    "*** YOUR CODE HERE ***"


# Q3
def reverse(link):
    """Returns a Link that is the reverse of the original.

    >>> print_link(reverse(Link(1)))
    <1>
    >>> link = Link(1, Link(2, Link(3)))
    >>> new = reverse(link)
    >>> print_link(new)
    <3 2 1>
    >>> print_link(link)
    <1 2 3>
    """
    "*** YOUR CODE HERE ***"


# Q4
def slice_link(link, start, end):
    """Slices a Link from start to end (as with a normal Python list).

    >>> link = Link(3, Link(1, Link(4, Link(1, Link(5, Link(9))))))
    >>> new = slice_link(link, 1, 4)
    >>> new
    Link(1, Link(4, Link(1)))
    >>> link2 = slice_link(Link(1), 0, 1)
    >>> link2
    Link(1)
    >>> link3 = slice_link(Link.empty, 0, 0)
    >>> link3
    ()
    """
    "*** YOUR CODE HERE ***"

