"""
C88C Summer 2024:

Please credit any folks in C88C that you collaborated with,
and any online sources you searched for.
Remember, it's OK to ask for help, and to search for topics, but
you may not search for specific solutions or copy any code directly.

List Collaborators:

Credit Any Online Sources (google searches, etc):


"""


def exponent_fun(exponent):
    """
    Returns a function that takes one argument and returns the 
    base raised to that exponent.
    >>> square = exponent_fun(2)
    >>> square(5)
    25
    >>> cubed = exponent_fun(3)
    >>> cubed(2)
    8
    """
    "*** YOUR CODE HERE ***"
    

def compare_lambda(operator):
    """
    Write a function that returns a subtraction lambda 
    function or addition lambda function depending on 
    the operator passed into compare lambda. Both lambda 
    functions take in two arguments.

    >>> adding = compare_lambda("+")
    >>> adding(3,2)
    5
    >>> subtracting = compare_lambda("-")
    >>> subtracting(6,2)
    4
    >>> operator_not_supported = compare_lambda("*")
    >>> operator_not_supported(2,3)
    'Remember to only use + or -!'
    """
    "*** YOUR CODE HERE ***"


def flip_dict(dictionary):
    """Returns a flipped version of the original dictionary.

    >>> TAs = {"12pm-2pm": "sean", "4pm-6pm": "rebecca", "2pm-4pm": "lily"}
    >>> flipped_TAs = flip_dict(TAs)
    >>> flipped_TAs 
    {'sean': '12pm-2pm', 'rebecca': '4pm-6pm', 'lily': '2pm-4pm'}
    """
    "*** YOUR CODE HERE ***"
    

def common_players(roster):
    """Returns a dictionary containing values along with a corresponding
    list of keys that had that value from the original dictionary.
    >>> full_roster = {"bob": "Team A", "barnum": "Team B", "beatrice": "Team C", "bernice": "Team B", "ben": "Team D", "belle": "Team A", "bill": "Team B", "bernie": "Team B", "baxter": "Team A"}
    >>> player_dict = common_players(full_roster)
    >>> dict(sorted(player_dict.items()))
    {'Team A': ['bob', 'belle', 'baxter'], 'Team B': ['barnum', 'bernice', 'bill', 'bernie'], 'Team C': ['beatrice'], 'Team D': ['ben']}
    """
    "*** YOUR CODE HERE ***"
    

