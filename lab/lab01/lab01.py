"""Lab 1: Control and Functions"""

def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return x and y > 0 # You can replace this line!


def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(5)
    5
    >>> sum_digits(34) # 3 + 4 = 7
    7
    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> x = sum_digits(123) # make sure that you are using return rather than print
    >>> x
    6
    """
    "*** YOUR CODE HERE ***"

