# List Comprehensions
courses = ['DATA C88C', 'DATA 8', 'POLSCI 2', 'MATH 54']

# Make a list from a for loop in one line!
numbers = [2 ** x for x in range(10) ]
# print(numbers)

# print() returns None
# [print(c) for c in courses]

# Copy a list!
courses2 = [c for c in courses]


# Functions are named, and we can assign new names

my_print = print

# my_print('Hello')

def greet(name):
    return 'Hello, ' + name + '!'

say_hello = greet

say_hello('CS88')

# Generalizing patterns using arguments

from math import pi, sqrt
from operator import mul

# Functions as arguments

def square(n):
    return n * n

def sum_numbers(n):
    """Sum the first N natural numbers.
    >>> sum_numbers(5)
    15
    >>> sum_numbers(10)
    55
    """
    total = 0
    for i in range(n + 1):
        total += i
    return total

def sum_squared(n):
    """Sum the first N squares of natural numbers.

    >>> sum_squared(5)
    55
    """
    total = 0
    for i in range(n + 1):
        total += square(i) # i ** 2
    return total

def sum_cubes(n):
    """Sum the first N cubes of natural numbers.
    >>> sum_cubes(5)
    225
    """
    total = 0
    for i in range(n + 1):
        total += pow(i, 3)
    return total

def sum_generic(n, func):
    total = 0
    for i in range(n + 1):
        total += func(i)
    return total

def identity(k):
    return k

def cube(k):
    return pow(k, 3)

def summation(n, term):
    """Sum the first N terms of a sequence.
    >>> summation(5, cube)
    225
    >>> summation(5, identity)
    15
    >>> summation(10, identity)
    55
    """
    total = 0
    print(term)
    for i in range(n + 1):
        total = total + term(i)
    return total

def sum_error(n, term):
    """Sum the first N terms of a sequence.
    """
    total = 0
    for i in range(n + 1):
        total = total + term
    return total


from operator import mul

def pi_term(k):
    # This is the expansion of the terms on the summation slide.
    return 8 / (16*k*k + 12*k + 4*k + 3)

summation(10000, pi_term)

def pi_error(approx):
    return str((1 - summation(approx, pi_term) / pi) * 100) + '%'


def add_one(n):
    return n + 1

add_one(3)

def make_adder(n):
    def adder(x):
        return x + n
    return adder

add_1 = make_adder(1)
x = add_1(3)

add_4 = make_adder(4)
add_4(5)

def compose(f, g):
    def h(x):
      return f(g(x))
    return h

add_2 = make_adder(2)
add_3 = make_adder(3)
x = add_2(x)

add_5 = compose(add_2, add_3)
y = add_5(x)

# compose an add_2 function with square
# square(add_2(3))
z = compose(square, make_adder(2))(3)

def leq_maker(c):
    def leq(val):
        return val <= c
    return leq

leq_maker(5)
leq_maker(5)(3)
