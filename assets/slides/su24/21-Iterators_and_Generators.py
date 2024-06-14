#!/usr/bin/env python
# coding: utf-8

# # CS88 Lecture 21: Iterators and Iterables

# A *sequence* is something that you can:
# * index into (it has an order)
# * get the length of.

# In[47]:


[1,2,3]


# In[48]:


s = [1,2,3,4]
s


# In[49]:


len(s)


# In[50]:


s[1]


# In[51]:


"Hello CS88 World"[4]


# What are some examples of types sequences?
# - list
# - tuple
# - string
#
# Note: a `dict` is *not* a sequence
#

# ## Iterable - an object you can iterate over
#
# * *iterable*: An object capable of yielding its members one at a time.
# * *iterator*: An object representing a stream of data.
#
# We have worked with many iterables as if they were sequences

# In[52]:


# list comprehension over an iterable
[x*x for x in s]


# In[53]:


# for loop over one too
for x in s:
    print(x)


# In[54]:


# iteration, but not an iteration over a sequence
while s:
    print(s)
    s = s[1:]


# In[55]:


range(10)


# In[56]:


def squares(s):
    return [x*x for x in s]


# In[11]:


s = [1,2,3,4]
squares(s)


# In[57]:


map(lambda x: x*x, s)


# In[58]:


def anyone(x):
    anyx = False
    for e in x:
        anyx = anyx or bool(e)
    return anyx


# In[61]:


anyone([0, False, [], '', True])


# In[15]:


help(any)


# In[16]:


def anyone(x):
    for e in x:
        if e:
            return True
    return False


# In[17]:


anyone([0, False, [], ''])


# # Functions that return iterables
#
# - `map`
# - `range`
# - `zip`
#
# These objects are not sequences.
#
# If we want to see all of the elements at once, we need to explicitly call
# `list()` or `tuple()` on them

# In[18]:


map(lambda x: x*x, [1,2,3])


# In[19]:


range(5)


# In[20]:


map(lambda x: x*x, range(5))


# In[21]:


[x for x in map(lambda x: x*x, range(5))]


# In[22]:


list(map(lambda x: x*x, range(5)))


# In[23]:


for x in map(lambda x: x*x, range(5)):
  print(x)


# In[24]:


map(lambda x: x*x, range(5))[3]


# In[25]:


zip([1,2,3], ['a', 'b'])


# In[26]:


list(zip([1,2,3], ['a', 'b']))


# ## Motivating question
#
# How can we define objects that behave like sequences without explicitly creating the sequence?
# * Generate each of the objects as we access them

#
# "A prime number (or a prime) is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers."

# In[63]:


def prime(n):
    return n > 1 and not any([n % i == 0 for i in range(2, n)])


# In[66]:


prime(13)


# In[67]:


list(zip(range(10), map(prime, range(10))))


# Why might we want to do this?
# - when the data is really BIG
# - maybe infinite!
#
# We need a concept of *lazy evaluation* - only compute what you need

# In[68]:


range(100000000000)


# In[69]:


x = map(prime, range(100000000000))
x


# In[31]:


for i,p in zip(range(10), x):
    print(i,p)


# In[32]:


[(i,p) for i,p in zip(range(10), x)]


# In[33]:


def first(n, x):
    return [e for i, e in zip(range(n), x)]


# In[34]:


first(10, x)


# # Generators:

# ## Generators: turning iteration into an interable
#
# - *Generator* functions use iteration (for loops, while loops) and the `yield` keyword
# - Generator functions have no return statement, but they don’t return None
# - They implicitly return a generator object
# - Generator objects are just iterators

# In[70]:


def squaresp(n):
    for i in range(n):
        print (i*i)


# In[71]:


squaresp(5)


# In[72]:


def squares(n):
    for i in range(n):
        yield (i*i)


# In[39]:


squares(5)


# In[73]:


list(squares(5))


# In[74]:


next(squares(5))


# In[85]:


sq = squares(5)


# In[86]:


next(sq)


# In[87]:


next(sq)


# In[89]:


next(sq)


# In[91]:


next(sq)


# In[92]:


for num in squares(5):
    print(num)


# In[93]:


from math import sqrt


# In[94]:


map(sqrt, squares(6))


# In[95]:


[i for i in map(sqrt, squares(6))]


# In[96]:


squares(100)[6]


# In[97]:


def isprimes(n):
    for i in range(n):
        yield (prime(i))


# In[98]:


first(5, isprimes(10000000))


# In[100]:


def primes():
    i = 2
    while True:
        if prime(i):
            yield(i)
        i += 1


# In[102]:


primes()


# In[104]:


p = primes()


# In[105]:


p


# In[132]:


next(p)


# In[133]:


first(10, primes())


# In[139]:


def squares2(n):
    i = 0
    while i < n:
        yield(i*i)
        i += 1


# In[140]:


[i for i in map(sqrt, squares2(6))]


# In[141]:


# an infinite object
def all_squares():
    i = 0
    while True:
        yield(i*i)
        i += 1


# In[142]:


all_squares()


# In[143]:


[(i,x) for i,x in zip(range(10),all_squares())]


# ## Nested iteration

# In[144]:


def all_pairs(x):
    for item1 in x:
        for item2 in x:
            yield(item1, item2)


# In[145]:


all_pairs(['apple', 'banana', 'orange'])


# In[146]:


list(all_pairs(['apple', 'banana', 'orange']))


# In[147]:


# nested iteration is available in list comprehensions too
[(i, j) for i in range(4) for j in range(3) ]


# # Sequences and Iterables
#
#
# ## Next element in generator iterable
#
# Iterables work because they have some "magic methods" on them.  We saw magic methods when we learned about classes, e.g., `__init__`, `__repr__` and `__str__`.
#
# The first one we see for iterables is `__next__`

# In[148]:


x = all_squares()


# In[149]:


x


# In[ ]:


help(next)


# In[150]:


next(x)


# In[151]:


next(x)


# In[152]:


next(x)


# In[153]:


x


# In[159]:


x.__next__()


# ## iter - transforming a sequence into an interator
#
# Builtin function iter takes an iterable object, e.g., a sequence, and returns an iterator

# In[ ]:


help(iter)


# In[166]:


x = iter([1,2,3])


# In[167]:


x


# In[168]:


next(x)


# In[169]:


x.__next__()


# In[171]:


x[3]


# In[173]:


x


# In[175]:


n = [1,2,3]


# In[177]:


next(n)


# In[179]:


n.__iter__


# In[180]:


n.__next__


# In[181]:


[x for x in iter([1,2,3])]


# In[182]:


y = all_squares()


# In[183]:


next(y)


# In[184]:


next(y)


# In[185]:


iter(y)


# In[186]:


next(y)


# In[187]:


s = "abc"
xs = iter(s)


# In[188]:


next(xs)


# In[189]:


next(xs)


# In[190]:


next(xs)


# In[191]:


next(xs)


# In[192]:


sq = all_squares()


# In[193]:


sq


# In[194]:


next(sq)


# In[195]:


sq.__next__()


# # Iterators
#
# In order to be *iterable*, a class must implement the `iter` protocol
#
# The iterator objects themselves are required to support the following two methods, which together form the iterator protocol:
#
# * `__iter__()` : Return the iterator object itself. This is required to allow both containers and iterators to be used with the for and in statements.
# - This method returns an iterator object
# - Iterator can be self
#
# * `__next__()` : Return the next item from the container. If there are no further items, raise the `StopIteration` exception.
#
# Classes get to define how they are iterated over by defining these methods

# In[197]:


def slowrange(n):
    i = 0
    result = []
    while i < n:
        result.append(i)
        i += 1
    return result


# In[198]:


slowrange(10)


# In[199]:


class myrange:
    def __init__(self, n, step=1):
        self.i = 0
        self.n = n
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += self.step
            return i
        else:
            raise StopIteration()


# In[200]:


myrange(5)


# In[202]:


[x for x in myrange(5)]


# In[204]:


list(myrange(5))


# In[205]:


myrange(1000000000000000000)


# ### `__next__(self)`
#
# Accessed via the next method
# * Returns the next element in the iteration
#     - Must keep track of where it is in the sequence
# * Once there are no more items left in the sequence, raise an exception:
#     - raise StopIteration

# In[206]:


x = myrange(2)


# In[207]:


next(x)


# In[208]:


next(x)


# In[209]:


next(x)


# ### pro·to·col:
#
# * the official procedure or system of rules governing affairs of state or diplomatic occasions.
#
# * COMPUTING:
# a set of rules governing the exchange or transmission of data between devices.
#
# * a formal or official record of scientific experimental observations.
# a procedure for carrying out a scientific experiment or a course of medical treatment.

# ## Getitem protocol
#
# Another way an object can behave like a sequence is *indexing*: Using square brackets “[ ]” to access specific items in an object.
#
# * Defined by special method: __getitem__(self, i)
#      - Method returns the item at a given index
# * As the designers of the class, get to decide what an index represents:
#     - Sequences: The item at a position in the sequence
#     - Dictionaries: The value associated with a given key
#     - Arrays: Index is a tuple representing the coordinate of the item
#
# A class that does not support __iter__ but with a __getitem__ method that raises an IndexError exception if the index gets to large is also iterable.

# In[ ]:


class myrange2:
    def __init__(self, n):
        self.n = n

    def __getitem__(self, i):
        if i >= 0 and i < self.n:
            return i
        else:
            raise IndexError

    def __len__(self):
        return self.n


# In[ ]:


x = myrange2(4)


# In[ ]:


len(x)


# In[ ]:


[x for x in myrange2(3)]


# In[ ]:


x[2]


# ## Determining if an object is iterable
#
# This is more general than checking for any list of particular type, e.g., list, tuple, string...

# In[1]:


from collections.abc import Iterable
from collections.abc import Sequence


isinstance([1,2,3], Iterable)


# In[ ]:


isinstance((1,2,3), Iterable)


# In[ ]:


isinstance({'a':1, 'b':2}, Iterable)


# In[ ]:


isinstance('s', Iterable)


# In[ ]:


isinstance('s'[0], Iterable)


# In[ ]:


myrange


# In[ ]:


myrange.__iter__


# In[ ]:


isinstance(myrange(4), Iterable)


# In[ ]:


isinstance(myrange2(4), Iterable)


# In[ ]:


isinstance(all_squares(), Iterable)


# # Extra for Experience:
#
# ## Examples

# In[2]:


# Get input from the user as a string
input()


# In[ ]:


def input_stream():
    """Stream input till empty rtn"""
    data = True
    while data:
        data = input('> Type Something fun!  ')
        yield(data)


# In[ ]:


# istream = input_stream()


# In[ ]:


# istream


# # In[ ]:


# list(istream)


# ### Using iterators for lazy evaluation
#
# Let's start with a recursive function to flatten a tree structure

# In[ ]:


def concat(s, lvl=1):
    """Concatenate a sequence of sequences."""
#    print('  s:', '-'*lvl, s)
    conc = []
    for e in s:
#        print("Cat:", '-'*lvl, e)
        conc = conc + e
    return conc

def flatten(tree, lvl=1):
    if isinstance(tree, str) or not isinstance(tree, Iterable):
        return [tree]  # a leaf node
    else:
        return concat([flatten(branch, lvl+1) for branch in tree], lvl)


# In[ ]:


concat([[1,2,3],[4,5,7], [6]])


# In[ ]:


flatten([1, 3, ['a','foo'], range(9,13)])


# In[ ]:


def iconcat(s, lvl=1):
    """Generate a concatenation of a sequence of sequences."""
#    print(" s:", "-"*lvl, s)
    for e in s:
        for x in e:
#            print("IC:", "-"*lvl, x)
            yield(x)

def iflatten(tree, lvl=1):
    if isinstance(tree, str) or not isinstance(tree, Iterable):
        return [tree]  # a leaf node
    else:
        return iconcat([iflatten(branch, lvl+1) for branch in tree], lvl)


# In[ ]:


iconcat([[1,2,3], [4,5], [6]])


# In[ ]:


list(iconcat([[1,2,3], [4,5], [6]]))


# In[ ]:


list(iflatten([1,3,['a','foo'],range(9,13)]))


# In[ ]:


list(iflatten([[1,2],3,[[4]]]))


# In[ ]:


def equal_fringe(tree1, tree2):
    for i1, i2 in zip(iflatten(tree1), iflatten(tree2)):
        if not i1 == i2:
            return False
    return True


# In[ ]:


equal_fringe([1, [2, [3,4]]], [[1,2], 3, [4]])


# In[ ]:


equal_fringe([1,2,[3,4]], [[7,4],3,[4]])
