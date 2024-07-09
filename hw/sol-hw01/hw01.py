"""Homework 1."""
"""
C88C Summer 2024:

Please credit any folks in C88C that you collaborated with,
and any online sources you searched for.
Remember, it's OK to ask for help, and to search for topics, but
you may not search for specific solutions or copy any code directly.

List Collaborators:

Credit Any Online Sources (google searches, etc):


"""


def odd(number):
    """Return whether the number is odd.

    >>> odd(2)
    False
    >>> odd(5)
    True
    """
    return number % 2 == 1


from math import sqrt

def distance(x1, y1, x2, y2):
    """Calculates the Euclidian distance between two points (x1, y1) and (x2, y2)

    >>> distance(1, 1, 1, 2)
    1.0
    >>> distance(1, 3, 1, 1)
    2.0
    >>> distance(1, 2, 3, 4)
    2.8284271247461903
    """
    return sqrt((y2-y1)**2 + (x2-x1)**2)

def distance3d(x1, y1, z1, x2, y2, z2):
    """Calculates the 3D Euclidian distance between two points (x1, y1, z1) and
    (x2, y2, z2).

    >>> distance3d(1, 1, 1, 1, 2, 1)
    1.0
    >>> distance3d(2, 3, 5, 5, 8, 3)
    6.164414002968976
    """
    return sqrt((y2-y1)**2 + (x2-x1)**2 + (z2-z1)**2)


from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-5, -1)
    -4
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b) # You can replace this line, but don't have to.


from math import sqrt

def quadratic(a, b, c):
    """
    >>> quadratic(1, 0, -1)
    (1.0, -1.0)
    >>> quadratic(1, 2, 1)
    (-1.0, -1.0)
    >>> quadratic(1, 3, -4)
    (1.0, -4.0)
    """
    t = sqrt(b*b - 4*a*c)
    return (-b+t)/(2*a),(-b-t)/(2*a)


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    total = 1
    if k > n:
        k = n
    while k > 0:
        total *= n
        n -= 1
        k -= 1
    return total


def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(2)
    2
    1
    >>> a
    2
    >>> b = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> b
    7
    """
    s = 1
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        print(n)
        s = s + 1
    return s

