######################
#### Trees ####
######################
# Tree Class
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



def same_shape(t1, t2):
    """Returns whether two Trees t1, t2 have the same shape. Two trees have the
    same shape if they have the same number of branches and each of their
    children have the same shape.

    >>> t, s = Tree(1), Tree(3)
    >>> same_shape(t, t)
    True
    >>> same_shape(t, s)
    True
    >>> t = Tree(1, [Tree(2), Tree(3)])
    >>> same_shape(t, s)
    False
    >>> s = Tree(4, [Tree(7)])
    >>> same_shape(t, s)
    False
    >>> s.branches.append(Tree(6)) # Add a new leaf to s to make it same shape as t
    >>> same_shape(t, s)
    True
    >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5)])
    >>> t2 = Tree(6, [Tree(7), Tree(8, [Tree(9), Tree(10)])])
    >>> same_shape(t1, t2)
    False
    >>> t1 = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3)])
    >>> t2 = Tree(9, [Tree(8, [Tree(6), Tree(7)]), Tree(10)])
    >>> same_shape(t1, t2)
    True
    >>> t1 = Tree(1, [Tree(2, [Tree(4, [Tree(6)])]), Tree(3)])
    >>> t2 = Tree(9, [Tree(8, [Tree(7, [Tree(5)])]), Tree(10)])
    >>> same_shape(t1, t2)
    True
    """
    if len(t1.branches) != len(t2.branches): 
        return False 
    for i in range(len(t1.branches)): 
        if not same_shape(t1.branches[i], t2.branches[i]): 
            return False 
    return True


def cumulative_sum(t):
    """Return a new Tree, where each value is the sum of all values in the
    corresponding subtree of t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative = cumulative_sum(t)
    >>> t
    Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(Tree(1))
    Tree(1)
    """
    subtrees = [cumulative_sum(st) for st in t.branches]
    new_value = sum(st.value for st in subtrees) + t.value
    return Tree(new_value, subtrees)


def find_level(t, level):
    """
    >>> t = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> find_level(t, 2)
    [4, 5, 7]
    >>> find_level(t, 1)
    [2, 6]
    >>> find_level(t, 5)
    []
    """
    if level == 0:
        return [t.value]
    elif t.is_leaf():
        return []
    else:
        lst = []
        for b in t.branches:
            lst += find_level(b, level - 1)
        return lst



def merge_trees(t1, t2, fn):
    """
    >>> one = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(6)])
    >>> two = Tree(11, [Tree(10, [Tree(10), Tree(10)]), Tree(10)])
    >>> merge_trees(one, two, lambda x, y: x + y)
    Tree(12, [Tree(12, [Tree(14), Tree(15)]), Tree(16)])
    >>> merge_trees(one, two, lambda x, y: y - x)
    Tree(10, [Tree(8, [Tree(6), Tree(5)]), Tree(4)])
    """
    if t1.is_leaf():
        return Tree(fn(t1.value, t2.value))
    else:
        branches = []
        for b1, b2 in zip(t1.branches, t2.branches):
            branches.append(merge_trees(b1, b2, fn))
        return Tree(fn(t1.value, t2.value), branches)


def quiet_get(data, selector, missing=None):
    """Return data[selector] if it exists, otherwise return missing.

    >>> quiet_get([1, 2, 3], 1)
    2
    >>> quiet_get([1, 2, 3], 4) # no missing argument passed in, so returns None
    >>> quiet_get([1, 2, 3], 4, -1)
    -1
    >>> quiet_get({'a': 2, 'b': 5}, 'a', -1)
    2
    >>> quiet_get({'a': 2, 'b': 5}, 'd', -1)
    -1
    """
    try:
        return data[selector]
    except (KeyError, IndexError):
        return missing

