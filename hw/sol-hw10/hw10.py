"""
C88C Summer 2024:

Please credit any folks in C88C that you collaborated with,
and any online sources you searched for.
Remember, it's OK to ask for help, and to search for topics, but
you may not search for specific solutions or copy any code directly.

List Collaborators:

Credit Any Online Sources (google searches, etc):


"""


##################################
#### Iterators and Generators ####
##################################

class ScaleIterator:
    """An iterator the scales elements of the iterable by a number scale.

    >>> s = ScaleIterator([1, 5, 2], 5)
    >>> list(s)
    [5, 25, 10]
    >>> m = ScaleIterator(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    def __init__(self, iterable, scale):
        self.iterable = iter(iterable)
        self.scale = scale

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterable) * self.scale


class IteratorRestart:
    """
    >>> iterator = IteratorRestart(2, 7)
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

    def __iter__(self):
        self.current = self.start
        return self


def hailstone(n):
    """
    >>> hs = hailstone(10)
    >>> type(hs)
    <class 'generator'>
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    while n > 1:
        yield n
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    yield n


def pairs(lst):
    """
    >>> type(pairs([3, 4, 5]))
    <class 'generator'>
    >>> for x, y in pairs([3, 4, 5]):
    ...     print(x, y)
    ...
    3 3
    3 4
    3 5
    4 3
    4 4
    4 5
    5 3
    5 4
    5 5
    """
    for i in lst:
        for j in lst:
            yield i, j

class PairsIterator:
    """
    >>> for x, y in PairsIterator([3, 4, 5]):
    ...     print(x, y)
    ...
    3 3
    3 4
    3 5
    4 3
    4 4
    4 5
    5 3
    5 4
    5 5
    """
    def __init__(self, lst):
        self.lst = lst
        self.i = 0
        self.j = 0

    def __next__(self):
        if self.i == len(self.lst):
            raise StopIteration
        result = (self.lst[self.i], self.lst[self.j])
        if self.j == len(self.lst) - 1:
            self.i += 1
            self.j = 0
        else:
            self.j += 1
        return result

    def __iter__(self):
        return self


def merge(r0, r1):
    """Yield the elements of strictly increasing iterables r0 and r1 and
    make sure to remove the repeated values in both.
    You can also assume that r0 and r1 represent infinite sequences.

    >>> twos = naturals(initial = 2, step = 2)
    >>> threes = naturals(initial = 3, step = 3)
    >>> m = merge(twos, threes)
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    i0 = iter(r0)
    i1 = iter(r1)
    e0 = next(i0)
    e1 = next(i1)
    while True:
        yield min(e0, e1)
        if e0 < e1:
            e0 = next(i0)
        elif e1 < e0:
            e1 = next(i1)
        else:
            e0, e1 = next(i0), next(i1)


def naturals(initial=1, step=1):
    i = initial
    while True:
        yield i
        i += step