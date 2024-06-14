# %% [markdown]
# # Lecture: Trees
#
# A tree is a _data structure_ that is like a linked list, but each item can have multiple "children" or branches.

# %%
class Tree:
    def __init__(self, value, *branches):
        self.value = value
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        # This is merely a more concise representation useful for later.
        # others = ' ...' if self.branches else ''
        # return 'Tree({0}){1}'.format(self.value, others)
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return f'Tree({self.value}{branches_str})'

    def is_leaf(self):
        return not self.branches

    def add_branch(self, tree):
        assert isinstance(tree, Tree), "Each branch of a Tree must be an instance of a Tree"
        self.branches.append(tree)


# %%
my_tree = Tree(1)


# %%


# %%
my_tree


# %%
my_tree.is_leaf()


# %%
my_tree.value


# %%
my_tree.branches


# %%
lec_tree = Tree(2,
    Tree(7,
        Tree(2),
        Tree(10),
        Tree(6,
            Tree(5),
            Tree(11))),
    Tree(5, Tree(9, Tree(4))))


# %%
lec_tree


# %%
len(lec_tree.branches)


# %%


# %%


# %%
print(lec_tree.value)
for b in lec_tree.branches:
    print(b.value)
    for b2 in b.branches:
        print(b2.value)


# %% [markdown]
# # Traversing A Tree

# %%
def traverse_recursive(t):
    print(f'Saw: {t.value}')
    for b in t.branches:
        traverse_recursive(b)


# %%
traverse_recursive(my_tree)


# %%
traverse_recursive(lec_tree)


# %%
# This is a handy Python feature.

def star_args(*args):
    print(args)


# %%
star_args('Hello')


# %%
star_args()


# %%


# %%


# %%
1 + len(lec_tree.branches)


# %%
def count_nodes(t):
    """The number of leaves in tree.

    >>> tree1 = Tree(1)
    >>> count_nodes(tree1)
    1
    >>> count_nodes(lec_tree)
    10
    """
    if t.is_leaf():
        return 1
    else:
        count = 1
        print(f'T is: {t.value}')
        for branch in t.branches:
            print(f"    Branch: {branch}")
            count += count_nodes(branch)
            print(f'    Count so far: {count}')
        return count


# %%
count_nodes(my_tree)


# %%
my_tree


# %%
my_tree.is_leaf()


# %%


# %%
count_nodes(lec_tree)


# %%


# %%


# %%
# SOLUTION

def count_nodes(t):
    """The number of leaves in tree."""
    return 1 + sum(map(count_nodes, t.branches))
        # return 1 + sum([count_nodes(b) for b in t.branches])


# %%
count_nodes(lec_tree)


# %%
list(map(lambda x: 1, []))


# %%
count_nodes(my_tree)


# %%


# %%


# %%
def coun(t):
    """The number of leaves in tree."""
    return 1 + sum(map(count_nodes, t.branches))


# %%
count_nodes(Tree(1, Tree(2)))


# %%
def print_tree(t, indent=0):
    """Print a representation of this tree in which each label is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> print_tree(fib_tree(4))
    3
      1
        0
        1
      2
        1
        1
          0
          1
    """
    print(f"{'  ' * indent}{t.value}")
    for b in t.branches:
        print_tree(b, indent + 1)


# %%
'8' * 2


# %%
print_tree(my_tree)


# %%
print_tree(lec_tree)


# %%


# %%
    print('  ' * indent + str(t.value) +  f'     indent: {indent}')
    for b in t.branches:
        print_tree(b, indent + 1)


# %%


# %%


# %%


# %%
def print_tree_lines(t, indent=0):
    """Print a representation of this tree in which each label is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> print_tree(fib_tree(4))
    3
      1
        0
        1
      2
        1
        1
          0
          1
    """
    pre = max(0, indent - 1)
    start = '-'
    print(f"{start}{'--' * pre}|--{t.value}")
    for b in t.branches:
        print_tree_lines(b, indent + 1)


# %%
print_tree_lines(lec_tree)


# %%


# %%
count_nodes(my_tree)


# %%
count_nodes(fib_tree(5))


# %%
def leaves(tree):
    """Return a list containing the leaf labels of tree.

    >>> leaves(fib_tree(5))
    [1, 0, 1, 0, 1, 1, 0, 1]
    """
    if tree.is_leaf():
        return [ tree.value ]
    else:
        # Sum with a "start=[]"
        # [1] + [2] + [3]...
        return sum([leaves(b) for b in tree.branches], [])


# %%
def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        fib_n = left.value + right.value
        return Tree(fib_n, [left, right])


# %%
fib_tree(5)


# %%
leaves(fib_tree(5))


# %%
print_tree(fib_tree(5))


# %%
fib_tree(4)


# %%
sum(leaves(fib_tree(4)))


# %% [markdown]
# # Searching Trees
#

# %%
big_tree = Tree(
    '1A', [
    Tree('2A', [
        Tree('3A', [
            Tree('4A', [
                Tree('5A')
            ])]),
        Tree('3B', [
            Tree('4B'),
            Tree('4C', [
                Tree('5B', [
                    Tree('6A')
                ])
            ]),
            Tree('4D'),
            Tree('4E')
        ])
    ]),
    Tree('2B',[
        Tree('3C', [
            Tree('4F')
        ])
    ])
])


# %%
print_tree(big_tree)


# %%
def traverse_recursive(t):
    print('Saw: ' + t.value)
    for b in t.branches:
        traverse_recursive(b)


# %%
traverse_recursive(big_tree)


# %% [markdown]
# Notice that, like out printed view, we got down one whole path before going back up.
#
#
# This is called depth first search.
#
# But, what if we want to go acroos each "level" first, such that I see all the 2's, then all the 3's and so on...

# %% [markdown]
# ## Extra: Breadth First Search.
#
# Use the commented print statements to inspect our `to_visit` list.
# This is called a _queue_. The first items we put in (via `.append`) are the first ones "out", that we access by using `.pop(0)`. We call this "First In, First Out".
#
# But really, it's just a list. It's all about using it in a particular way.

# %%
def traverse_across(t):
    to_visit = []
    to_visit.append(t)
    while len(to_visit) > 0:
        node = to_visit.pop(0)
        print('Visit: ' + node.value)
        for branch in node.branches:
            to_visit.append(branch)
        print(to_visit)


# %%
traverse_across(big_tree)


# %%
my_list = [1, 2, 3]
item = my_list.pop(0)


# %%
print(item)


# %%
print(my_list)


# %% [markdown]
# # Extra: Binary Search Trees
#
# A tree where each sub tree has 2 children, a left and a right.

# %%
ordered_tree = Tree(8, [Tree(3,
                             [Tree(1),
                              Tree(6, [Tree(4), Tree(7)])]
                            ),
                       Tree(10, [
                           Tree(None),
                           Tree(14, [Tree(13), Tree(None)])])
                       ]
                   )


# %%
print_tree(ordered_tree)


# %%
def bst(tree, value):
    if tree.value == value:
        return value
    elif tree.is_leaf():
        return 'NOT FOUND'
    left = tree.branches[0]
    right = tree.branches[1]
    if left.value and value < tree.value:
        return bst(left, value)
    elif right.value:
        return bst(right, value)
    return 'NOT FOUND'


# %%
for i in range(18):
    print(str(i) + ' ' + str(bst(ordered_tree, i)))


# %%


# %%
def list_to_tree(family_tuple):
    value, branch_list = family_tuple
    branches = [list_to_tree(branch_tuple) for branch_tuple in branch_list]
    return Tree(value, branches)


# %%

family_tree = Tree(
        ("Jordan", "Alex"),
        Tree(("Taylor", "Morgan"),
            Tree(("Riley", "Sam"),
                Tree(("Avery", None))
            )
        ),
    Tree( ("Casey", "Jamie"),
        Tree(("Quinn", "Chris"),
            Tree( ("Dakota", None) ),
            Tree( ("Skyler", None) )
        ),
        Tree( ("Jesse", "Jordan") )
    )
    )

family_tree


# %%


# %%
