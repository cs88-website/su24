from operator import add, mul, concat
from functools import reduce

courses = ['DATA C88C', 'DATA 8', 'POLSCI 2', 'MATH 54']
depts = [ course.split() for course in courses ]

depts = list(map(lambda c: c.split(), courses))

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
y

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

cal = 'The University of California at Berkeley'
copycats = 'The University of California Los Angeles'
jc = 'Leland Stanford Junior University'

words = cal.split()
# words
# # ['The', 'University', 'of', 'Califonria', 'at', 'Berkeley']
numbers = range(10)
# [ n * n for n in numbers ]
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

square(5)
map(square, numbers)

def emojify(letter):
    """Turn a letter a-z into an emoji.
    """
    return chr(ord(letter) - ord('a') + ord('😀'))

def un_emojify(emoji):
    """Turn an emoji into a letter a-z.
    """
    return chr(ord(emoji) - ord('😀') + ord('a'))


# <map object at 0x100fe5940>
# range(10)
# range(0, 10)
list(map(square, numbers))
def first_letter(word):
    return word[0]

def long_word(word):
    return len(word) > 3

first_letter('Berkeley')
list(map(first_letter, words))

words
# ['The', 'University', 'of', 'Califonria', 'at', 'Berkeley']
def is_even(n):
    return n % 2 == 0
# ...
is_even(3)
# False
# range(0, 10)
[ n for n in numbers if is_even(n) ]
filter(is_even, numbers)
# <filter object at 0x101069b50>
list(filter(is_even, numbers))

def long_word(word):
    return len(word) > 3

long_word('of')
# False
list(filter(long_word, words))
# ['University', 'Califonria', 'Berkeley']
# >>>
# >>>
reduce
# <built-in function reduce>
add(1, 2)
# 3
reduce(add, numbers)
# 45
list(numbers)


def keep_words(word):
    specials = ['Los']
    return word in specials or long_word(word)

def acronym(text):
    words = text.split()
    return reduce(add, map(first_letter, filter(long_word, words)))


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

def group_by(result_or_start, next_item):
    """
    Combine two item pairs by their first key.
    >>> courses = ['DATA C88C', 'DATA 8', 'POLSCI 2', 'MATH 54']
    >>> depts = [ course.split() for course in courses ]
    >>> reduce(group_by, depts)
    [['DATA', ['C88C', '8']], ['POLSCI', ['2']], ['MATH', ['54']]]
    """
    item = next_item
    if not result_or_start or type(result_or_start[0]) != list:
        result = [ [result_or_start[0], [ result_or_start[1] ] ] ]
    else:
        result = result_or_start
    keys = [ pair[0] for pair in result ]
    if item[0] in keys:
        index = keys.index(item[0])
        pair = result[index]
        pair[1].append(item[1])
    else:
        result.append([ item[0], [ item[1] ] ])
    return result

def group_by_count(result_or_start, next_item):
    """
    Aggregate counts two item pairs by their first key.
    >>> courses = ['DATA C88C', 'DATA 8', 'POLSCI 2', 'MATH 54']
    >>> depts = [ course.split() for course in courses ]
    >>> reduce(group_by_count, depts)
    [['DATA', 2], ['POLSCI', 1], ['MATH', 1]]
    """
    item = next_item
    if not result_or_start or type(result_or_start[0]) != list:
        result = [ [ result_or_start[0], 1 ] ]
    else:
        result = result_or_start
    keys = [ pair[0] for pair in result ]
    if item[0] in keys:
        index = keys.index(item[0])
        pair = result[index]
        pair[1] = pair[1] + 1
    else:
        result.append([ item[0], 1 ])
    return result
