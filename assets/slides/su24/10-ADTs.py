counter = 0
def counter_fun():
    counter += 1
    return counter
# ...
# counter_fun()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in counter_fun
# UnboundLocalError: local variable 'counter' referenced before assignment
# counter
# 0
# counter = 10
def make_counter():
    counter = [0]
    def count_up():
            counter[0] += 1
            return counter
    return count_up
# ...
c = make_counter()
c
# <function make_counter.<locals>.counts at 0x10ce88ee0>
c()
# 1
c()
# 2
c()
# 3
second = make_counter()
second
# <function make_counter.<locals>.counts at 0x10ce88f70>
second()
# 1
second()
# 2
second()
# 3
c()
# 4


def make_withdraw_account(initial):
    balance = [initial]

    def withdraw(amount):
        if balance[0] - amount < 0:
            return 'Insufficient funds'
        balance[0] -= amount
        return balance[0]
    return withdraw


withdraw = make_withdraw_account(100)
withdraw(25)
withdraw(25)
withdraw(25)
withdraw(50)

def new_account(initial_balance):
    data = { 'balance': initial_balance }

    def withdraw(amount):
        if data['balance'] - amount < 0:
            return 'Insufficient funds'
        data['balance'] -= amount
        return data['balance']

    def deposit(amount):
        if amount < 0:
            return 'Amount must be > 0'
        data['balance'] += amount
        return data['balance']

    def do_action(action, value=None):
        if action == 'balance':
            return data['balance']
        elif action == 'withdraw':
            return withdraw(value)
        elif action == 'deposit':
            return deposit(value)
        else:
            return 'UNKNOWN ACTION'
    return do_action






course = {
    'name': 'Comp Structures in Data Science',
    'number': 'C88C',
    'room': '2050 VLSB',
    'units': 3,
    'sections': [100 + x for x in range(12)]
}

text = 'Once Upon A Time'

counts = { word : len(word) for word in text.split(' ') }
counts

counts.keys()
counts.values()
counts.items()
# counts['time']
# counts['hello']
counts.get('hello')
