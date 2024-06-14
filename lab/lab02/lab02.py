"""C88C Lab 2"""
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
def odd_even(x):
    """Classify a number as odd or even.
    
    >>> odd_even(4)
    'even'
    >>> odd_even(3)
    'odd'
    """
    "*** YOUR CODE HERE ***"

def classify(s):
    """
    Classify all the elements of a sequence as odd or even
    >>> classify([0, 1, 2, 4])
    ['even', 'odd', 'even', 'even']
    """
    "*** YOUR CODE HERE ***"


#Question 2
def find_word(words, n):
    """
    >>> find_word(["cat", "window", "zookeeper"], 5)
    'window'
    >>> find_word(["cat", "dog", "fish"], 3)
    'fish'
    >>> find_word(["cat", "dog", "bro"], 3)
    ''
    >>> find_word(["python", "java", "SQL"], 4)
    'python'
    """
    "*** YOUR CODE HERE ***"


# Question 3
def if_this_not_that(i_list, this):
    """
    >>> original_list = [1, 2, 3, 4, 5]
    >>> if_this_not_that(original_list, 3)
    that
    that
    that
    4
    5
    """
    "*** YOUR CODE HERE ***"


# Question 4
def shuffle(cards):
    """Return a shuffled list that interleaves the two halves of cards.

    >>> lst = [1, 2, 3, 4, 5, 6, 7, 8]
    >>> shuffle(lst)
    [1, 5, 2, 6, 3, 7, 4, 8]
    >>> shuffle(range(6))
    [0, 3, 1, 4, 2, 5]
    >>> cards = ['AH', '1H', '2H', '3H', 'AD', '1D', '2D', '3D']
    >>> shuffle(cards)
    ['AH', 'AD', '1H', '1D', '2H', '2D', '3H', '3D']
    >>> cards # should not be changed
    ['AH', '1H', '2H', '3H', 'AD', '1D', '2D', '3D']
    """
    assert len(cards) % 2 == 0, 'len(cards) must be even'
    "*** YOUR CODE HERE ***"


# Question 5

def pairs(n):
    """Returns a new list containing two element lists from values 1 to n
    >>> pairs(1)
    [[1, 1]]
    >>> x = pairs(2)
    >>> x
    [[1, 1], [2, 2]]
    >>> pairs(5)
    [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    >>> pairs(-1)
    []
    """
    "*** YOUR CODE HERE ***"
    


# Question 6
def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> def fn(x):
    ...     return x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """
    "*** YOUR CODE HERE ***"
    



