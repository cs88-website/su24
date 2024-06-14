from operator import add, mul, concat
from functools import reduce

cal = 'The University of California at Berkeley'
copycats = 'The University of California Los Angeles'
jc = 'Leland Stanford Junior University'
words = cal.split() # splits by space.

def add_one(n):
    return n + 1

def square(n):
    return n * n

add_one(3)

def make_adder(n):
    def adder(x):
        return x + n
    return adder

add_1 = make_adder(1)
add_1(3)

add_4 = make_adder(4)
add_4(5)

def leq_maker(c):
    def leq(val):
        return val <= c
    return leq

def compose(f, g):
    def h(x):
      return f(g(x))
    return h

add_2 = make_adder(2)
add_3 = make_adder(3)
x = add_2(3)

add_5 = compose(add_2, add_3)
y = add_5(x)

z = compose(square, make_adder(2))(3)

# help(map)

def is_even(n):
    return n % 2 == 0

def is_uppercase(word):
    return word[0].capitalize() == word[0]

def shout(word):
    return word.upper()

def embiggen(item):
    "This uses some Python features we don't really cover, but can be fun."
    if type(a) == str:
        return shout(item)
    elif item.isdigit():
        return int(item) * 2
    else:
        return item

words = cal.split()
# words
# # ['The', 'University', 'of', 'Califonria', 'at', 'Berkeley']

def first_letter(word):
    return word[0]

def long_word(word):
    return len(word) > 3

def acronym(sentence):
    """
    >>> acronym(cal)
    "UCB"
    >>> acronym(copycats)
    "UCLA"
    >>> acronym(jc)
    "LSJU"
    """
    words = sentence.split()
    return reduce(add, map(first_letter, filter(long_word, words)))

first_letter('Berkeley')
list(map(first_letter, words))

def keep_words(word):
    specials = ['Los']
    return word in specials or long_word(word)

def acronym_hof(sentence, filter_fn):
    """
    >>> acronym_hof(cal, keep_words)
    "UCB"
    >>> acronym_hof(copycats, keep_words)
    "UCLA"
    >>> acronym_hof(jc, keep_words)
    "LSJU"
    """
    words = sentence.split()
    return reduce(add, map(first_letter, filter(filter_fn, words)))
