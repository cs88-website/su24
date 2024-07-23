"""
C88C Summer 2024:

Please credit any folks in C88C that you collaborated with,
and any online sources you searched for.
Remember, it's OK to ask for help, and to search for topics, but
you may not search for specific solutions or copy any code directly.

List Collaborators:

Credit Any Online Sources (google searches, etc):


"""


def operation_inator(operation_string):
    """
    >>> identity = operation_inator('self')
    >>> identity(5)
    5
    >>> identity(6)
    6
    >>> add_one = operation_inator('add one')
    >>> add_one(2)
    3
    >>> add_one(3)
    4
    >>> mul_together = operation_inator('multiply together')
    >>> mul_together(0, 1)
    0
    >>> mul_together(3, 2)
    6
    >>> zero_to_self = operation_inator('zero to self')
    >>> zero_to_self(3)
    [0, 1, 2]
    >>> zero_to_self(1)
    [0]
    """
    if operation_string == 'self':
        return lambda x: x
    elif operation_string == 'add one':
        return lambda x: x + 1
    elif operation_string == 'multiply together':
        return lambda x, y: x * y
    elif operation_string == 'zero to self':
        return lambda x: list(range(x))


def higher_order_lambdas():
    """
    Return a lambda function that takes in a multiplier and returns a lambda function that given an input will 
    return the input multiplied by the multiplier
    >>> hol = higher_order_lambdas()
    >>> doubles = hol(2)
    >>> doubles(3)
    6
    >>> hol = higher_order_lambdas()
    >>> triples = hol(3)
    >>> triples(4)
    12
    """
    return lambda m : lambda n : m * n

def lambda_curry2(f2):
    """
    Returns a Curried version of a two argument function func.
    >>> from operator import add, mul
    >>> x = lambda_curry2(add)
    >>> y = x(3)
    >>> y(5)
    8
    >>> a = lambda_curry2(mul)
    >>> b = a(3)
    >>> b(5)
    15
    """
    return lambda arg1: lambda arg2: f2(arg1, arg2)


def replace_all(d, x, y):
    """
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> e = replace_all(d, 3, 'poof')
    >>> e == {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    new = {}
    for key in d:
        if d[key] == x:
            new[key] = y
        else:
            new[key] = d[key]
    return new


def music_dict(songs_dict):
    """
    Returns a dictionary where each key is an artist name and the
    value is a list of all of the songs by that artist.

    >>> songs = {"Good Days": "SZA", "Karma": "Taylor Swift", "22": "Taylor Swift", "Snooze": "SZA", "vampire": "Olivia Rodrigo"}
    >>> music_dict(songs)
    {'SZA': ['Good Days', 'Snooze'], 'Taylor Swift': ['Karma', '22'], 'Olivia Rodrigo': ['vampire']}
    """
    artist_songs = {}
    for song, artist in songs_dict.items():
        if artist in artist_songs:
            artist_songs[artist].append(song)
        else:
            artist_songs[artist] = [song]
    return artist_songs


def merge_dict(dict1, dict2):
    """Returns a dictionary that is the result of two dictionaries being merged together. 
    Dictionaries are merged by adding up their values. You can assume that the same keys 
    appear in both dictionaries.
    >>> data8 = {"midterms":1, "projects":3}
    >>> data100 = {"midterms":2, "projects":3}
    >>> combined_exams = merge_dict(data8, data100)
    >>> combined_exams
    {'midterms': 3, 'projects': 6}
    >>> sunday_orders = {"pizza": 3, "hot dogs": 2, "fries": 5}
    >>> monday_orders = {"pizza": 1, "hot dogs": 1, "fries": 8}
    >>> combined_orders = merge_dict(sunday_orders, monday_orders)
    >>> combined_orders
    {'pizza': 4, 'hot dogs': 3, 'fries': 13}
    """
    result_dict = {}
    for work in dict1:
        result_dict[work] = dict1[work] + dict2[work]
    return result_dict

