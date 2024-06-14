"""
C88C Summer 2024:

Please credit any folks in C88C that you collaborated with,
and any online sources you searched for.
Remember, it's OK to ask for help, and to search for topics, but
you may not search for specific solutions or copy any code directly.

List Collaborators:

Credit Any Online Sources (google searches, etc):


"""


# Question 1
def make_buzzer(n):
    """ Returns a function that prints numbers in a specified
    range except those divisible by n.

    >>> i_hate_fives = make_buzzer(5)
    >>> i_hate_fives(10)
    Buzz!
    1
    2
    3
    4
    Buzz!
    6
    7
    8
    9
    """
    "*** YOUR CODE HERE ***"
    


# Question 2
def intersects(f, x):
    """Returns a function that returns whether f intersects g at x.

    >>> def square(x):
    ...     return x * x
    >>> def triple(x):
    ...     return x * 3
    >>> def increment(x):
    ...     return x + 1
    >>> def identity(x):
    ...     return x
    >>> at_three = intersects(square, 3)
    >>> at_three(triple) # triple(3) == square(3)
    True
    >>> at_three(increment)
    False
    >>> at_one = intersects(identity, 1)
    >>> at_one(square)
    True
    >>> at_one(triple)
    False
    """
    "*** YOUR CODE HERE ***"
    


# Question 3
def funception(func_a, start):
    """ Takes in a function (function A) and a start value.
    Returns a function (function B) that will find the product of 
    function A applied to the range of numbers from 
    start (inclusive) to stop (exclusive)

    >>> def func_a(num):
    ...     return num + 1
    >>> func_b1 = funception(func_a, 3)
    >>> func_b1(2)
    4
    >>> func_b2 = funception(func_a, -2)
    >>> func_b2(-3)
    >>> func_b3 = funception(func_a, -1)
    >>> func_b3(4)
    >>> func_b4 = funception(func_a, 0)
    >>> func_b4(3)
    6
    >>> func_b5 = funception(func_a, 1)
    >>> func_b5(4)
    24
    """
    "*** YOUR CODE HERE ***"
    





# Question 4
def match_pairs(lst, fn):
    """
    >>> lst = ["bobby", "frodo", "sally", "kyoko", "beth"]
    >>> def same_last_char(a, b):
    ...     return a[-1] == b[-1]
    >>> sorted(match_pairs(lst, same_last_char)) # sorted is used for testing 
    [['bobby', 'sally'], ['frodo', 'kyoko'], ['kyoko', 'frodo'], ['sally', 'bobby']]
    >>> def same_first_char(a, b):
    ...     return a[0] == b[0]
    >>> sorted(match_pairs(lst, same_first_char))
    [['beth', 'bobby'], ['bobby', 'beth']]
    """
    "*** YOUR CODE HERE ***"


