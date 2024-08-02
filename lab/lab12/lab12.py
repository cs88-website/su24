## Final Review ##

## Control

def second_max(lst):
    """ 
    Return the second highest number in a list of positive integers.
    
    >>> second_max([3, 2, 1, 0])
    2
    >>> second_max([2, 3, 3, 4, 5, 6, 7, 2, 3])
    6
    >>> second_max([1, 5, 5, 5, 1])
    5
    >>> second_max([5, 6, 6, 7, 1])
    6
    >>> second_max([5, 6, 7, 7, 1])
    7
    """

    "*** YOUR CODE HERE ***"


## Higher Order Functions

def count_cond(condition, n):
    """
    >>> def divisible(n, i):
    ...     return n % i == 0
    >>> count_cond(divisible, 2) # 1, 2
    2
    >>> count_cond(divisible, 4) # 1, 2, 4
    3
    >>> count_cond(divisible, 12) # 1, 2, 3, 4, 6, 12
    6

    >>> def is_prime(n, i):
    ...     return count_cond(divisible, i) == 2
    >>> count_cond(is_prime, 2) # 2
    1
    >>> count_cond(is_prime, 3) # 2, 3
    2
    >>> count_cond(is_prime, 4) # 2, 3
    2
    >>> count_cond(is_prime, 5) # 2, 3, 5
    3
    >>> count_cond(is_prime, 20) # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***"
    


## Lists and Dictionaries

def deep_len(lst):
    """Returns the deep length of the list.

    >>> deep_len([1, 2, 3])     # normal list
    3
    >>> x = [1, [2, 3], 4]      # deep list
    >>> deep_len(x)
    4
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> deep_len(x)
    6
    """
    "*** YOUR CODE HERE ***"


def counter(message):
    """ Returns a dictionary of each word in message mapped
    to the number of times it appears in the input string.

    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    word_list = message.split()
    "*** YOUR CODE HERE ***"
    


## Recursion

def knapsack(weights, values, c):
    """
    >>> w = [2, 6, 3, 3]
    >>> v = [1, 5, 3, 3]
    >>> knapsack(w, v, 6)
    6
    """
    "*** YOUR CODE HERE ***"


def compose1(f, g):
    """"Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

def repeated(f, n):
    """
    >>> f = lambda x: x + 1
    >>> g = repeated(f, 1)
    >>> g(5)
    6
    >>> h = repeated(f, 3)
    >>> h(5)
    8
    >>> f2 = lambda x: x * 2
    >>> g2 = repeated(f2, 3)
    >>> g2(3)
    24
    """
    "*** YOUR CODE HERE ***"


## OOP and Inheritance

class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.current_year.

    >>> mint = Mint()
    >>> mint.year
    2020
    >>> dime = mint.create(Dime)
    >>> dime.year
    2020
    >>> Mint.current_year = 2100  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2020
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2100
    >>> Mint.current_year = 2175     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years). 155 is because this dime instance has year 2020
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    >>> m = Mint()
    >>> n = m.create(Nickel)
    >>> n.worth()
    5
    >>> n.year = 2015
    >>> n.worth() # 5 cents + (160 - 50 years). 160 is from 2175 - 2015
    115
    """
    current_year = 2020

    def __init__(self):
        self.update()

    def create(self, coin):
        "*** YOUR CODE HERE ***"

    def update(self):
        "*** YOUR CODE HERE ***"

class Coin:
    cents = 0 # Default value of 0. This value will be overridden in subclasses.

    def __init__(self, year):
        self.year = year

    def worth(self):
        "The worth is a coin's face value + 1 cent for each year over age 50."
        "*** YOUR CODE HERE ***"

class Nickel(Coin):
    cents = 5

class Dime(Coin):
    cents = 10


## Linked Lists

def insert(link, value, index):
    """Insert a value into a Link at the given index.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print_link(link)
    <1 2 3>
    >>> insert(link, 9001, 0)
    >>> print_link(link)
    <9001 1 2 3>
    >>> insert(link, 100, 2)
    >>> print_link(link)
    <9001 1 100 2 3>
    >>> insert(link, 4, 5)
    IndexError
    """
    "*** YOUR CODE HERE ***"


## Trees

def path(t, target):
    """
    >>> t = Tree(9, [Tree(7, [Tree(3), Tree(2)]), Tree(5)])
    >>> path(t, 2)
    [9, 7, 2]
    >>> path(t, 5)
    [9, 5]
    >>> path(t, 8)
    []
    """
    "*** YOUR CODE HERE ***"


## Iterators and Generators

class Str:
    """
    >>> hey_iter = Str('hey')
    >>> for char in hey_iter:
    ...     print(char)
    h
    e
    y
    >>> list(hey_iter)
    []
    """
    def __init__(self, str):
        "*** YOUR CODE HERE ***"

    def __iter__(self):
        "*** YOUR CODE HERE ***"

    def __next__(self):
        "*** YOUR CODE HERE ***"


def generate_perms(lst):
    """
    Generates the permutations of lst one by one.
    >>> perms = generate_perms([1, 2, 3])
    >>> hasattr(perms, '__next__')
    True
    >>> p = list(perms)
    >>> p.sort()
    >>> p
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    if lst == []:
        "*** YOUR CODE HERE ***"
    else:
        for perm in generate_perms(lst[1:]):
            for i in range(len(lst)):
                "*** YOUR CODE HERE ***"


## Link class
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

## Tree class

class Tree:
    def __init__(self, value, branches=()):
        self.value = value
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.value, branches_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.value) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

    def is_leaf(self):
        return not self.branches


