"""Homework 3"""
"""
C88C Summer 2024:

Please credit any folks in C88C that you collaborated with,
and any online sources you searched for.
Remember, it's OK to ask for help, and to search for topics, but
you may not search for specific solutions or copy any code directly.

List Collaborators:

Credit Any Online Sources (google searches, etc):


"""


def add_matrices(x, y):
    """
    >>> matrix1 = [[1, 3],
    ...            [2, 0]]
    >>> matrix2 = [[-3, 0],
    ...            [1, 2]]
    >>> add_matrices(matrix1, matrix2)
    [[-2, 3], [3, 2]]
    >>> matrix4 = [[ 1, -2,  3],
    ...            [-4,  5, -6]]
    >>> matrix5 = [[-1,  2, -3],
    ...            [ 4, -5,  6]]
    >>> add_matrices(matrix4, matrix5)
    [[0, 0, 0], [0, 0, 0]]
    """
    return [[x[i][j] + y[i][j] for j in range(len(x[0]))]
                               for i in range(len(x))]


def make_derivative(f):
    """Returns a function that approximates the derivative of f.

    Recall that f'(a) = (f(a + h) - f(a)) / h as h approaches 0. We will
    approximate the derivative by choosing a very small value for h.

    >>> def square(x): 
    ...     # equivalent to: square = lambda x: x * x
    ...     return x * x
    >>> derivative = make_derivative(square)
    >>> result = derivative(3)
    >>> round(result, 3) # approximately 2 * 3
    6.0
    """
    h = 0.00001
    def derivative(x):
        return (f(x + h) - f(x)) / h
    return derivative


from operator import add, mul

def reduce(reducer, s, base):
    """Reduce a sequence under a two-argument function starting from a base value.

    >>> def add(x, y):
    ...     return x + y
    >>> def mul(x, y):
    ...     return x * y
    >>> reduce(add, [1, 2, 3, 4], 0)
    10
    >>> reduce(mul, [1, 2, 3, 4], 0)
    0
    >>> reduce(mul, [1, 2, 3, 4], 1)
    24
    """
    for x in s:
        base = reducer(base, x)
    return base


def smooth(f, dx):
    """Returns the smoothed version of f, g where

    g(x) = (f(x - dx) + f(x) + f(x + dx)) / 3

    >>> square = lambda x: x ** 2
    >>> smoothed_square = smooth(square, 1)
    >>> round(smoothed_square(0), 3)
    0.667
    """
    return lambda x: (f(x - dx) + f(x) + f(x + dx)) / 3

def cycle(f1, f2, f3):
    """ Returns a function that is itself a higher order function
    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)   # f1 = add1, f2 = times2, f3 = add3
    >>> identity = my_cycle(0)                 # n = 0
    >>> identity(5)                            # return x, where x = 5
    5
    >>> add_one_then_double = my_cycle(2)      # n = 2
    >>> add_one_then_double(1)                 # return f2(f1(x)), where x = 1
    4
    >>> do_all_functions = my_cycle(3)         # n = 3
    >>> do_all_functions(2)                    # return f3(f2(f1(x))), where x = 2
    9
    >>> do_more_than_a_cycle = my_cycle(4)     # n = 4
    >>> do_more_than_a_cycle(2)                # return f1(f3(f2(f1(x)))), where x = 2
    10
    >>> do_two_cycles = my_cycle(6)            # n = 6
    >>> do_two_cycles(1)                       # return f3(f2(f1(f3(f2(f1(x)))))), where x = 1
    19
    """
    def ret_fn(n):
        def ret(x):
            i = 0
            while i < n:
                if i % 3 == 0:
                    x = f1(x)
                elif i % 3 == 1:
                    x = f2(x)
                else:
                    x = f3(x)
                i += 1
            return x
        return ret
    return ret_fn


def store_word(secret):
    """
    >>> word_len, guess_word = store_word("cake")
    >>> word_len
    4
    >>> guess_word("corn")
    [True, False, False, False]
    >>> guess_word("come")
    [True, False, False, True]
    >>> guess_word("cake")
    [True, True, True, True]
    >>> word_len, guess_word = store_word("pop")
    >>> word_len
    3
    >>> guess_word("ate")
    [False, False, False]
    >>> guess_word("top")
    [False, True, True]
    >>> guess_word("pop")
    [True, True, True]
    """
    def guess_word(guess):
        return [secret[i] == guess[i] for i in range(len(guess))]

    return len(secret), guess_word

