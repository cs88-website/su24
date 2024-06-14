from math import sqrt 

#############
# Iterators #
#############

# Q1
class IteratorA:
    def __init__(self):
        self.start = 10

    def __next__(self):
        if self.start > 100:
            raise StopIteration
        self.start += 20
        return self.start

    def __iter__(self):
        return self

class IteratorB:
    def __init__(self):
        self.start = 5

    def __iter__(self):
        return self

class IteratorC:
    def __init__(self):
        self.start = 5

    def __next__(self):
        if self.start == 10:
            raise StopIteration
        self.start += 1
        return self.start

class IteratorD:
    def __init__(self):
        self.start = 1

    def __next__(self):
        self.start += 1
        return self.start

    def __iter__(self):
        return self



##############
# Generators #
##############

# Q2
def countdown(n):
    """
    >>> from types import GeneratorType
    >>> type(countdown(0)) is GeneratorType # countdown is a generator
    True
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"

class Countdown:
    """
    >>> from types import GeneratorType
    >>> type(Countdown(0)) is GeneratorType # Countdown is an iterator
    False
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"

def naturals(initial=1, step=1):
    i = initial
    while True:
        yield i
        i += step

# Q3
from math import sqrt

def is_prime(n):
    """
    Return True if n is prime, false otherwise.

    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(19)
    True
    """
    "*** YOUR CODE HERE ***"

def primes():
    """
    An infinite generator that outputs primes. 

    >>> p = primes()
    >>> for i in range(3):
    ...     print(next(p))
    ...
    2
    3
    5
    """
    "*** YOUR CODE HERE ***"

