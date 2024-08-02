
################
#### Inheritance #####
################

class Error:
    """
    >>> err1 = Error(12, "error.py")
    >>> err1.write()
    error.py:12
    """
    def __init__(self, line, file):
        self.line = line
        self.file = file

    def format(self):
        return self.file + ':' + str(self.line)

    def write(self):
        print(self.format())

class SyntaxError(Error):
    """
    >>> err1 = SyntaxError(17, "lab10.py")
    >>> err1.write()
    lab10.py:17 SyntaxError : Invalid syntax
    >>> err1.add_code(4, "EOL while scanning string literal")
    >>> err2 = SyntaxError(18, "lab10.py", 4)
    >>> err2.write()
    lab10.py:18 SyntaxError : EOL while scanning string literal
    """
    type = 'SyntaxError'
    msgs = {0 : "Invalid syntax", 1: "Unmatched parentheses", 2: "Incorrect indentation", 3: "missing colon"}

    def __init__(self, line, file, code=0):
        super().__init__(line, file)
        self.message = self.msgs[code]

    def format(self):
        return super().format() + ' ' + self.type + " : " + self.message # or SyntaxError.msgs[self.code]

    def add_code(self, code, msg):
        SyntaxError.msgs[code] = msg

class ZeroDivisionError(Error):
    """
    >>> err1 = ZeroDivisionError(273, "lab10.py")
    >>> err1.write()
    lab10.py:273 ZeroDivisionError : division by zero
    """
    type = 'ZeroDivisionError'

    def __init__(self, line, file, message='division by zero'):
        super().__init__(line, file)
        self.message = message

    def format(self):
        end = self.type + ' : ' + self.message
        return super().format() + " " + end


# Linked List Class
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

######################
#### Linked Lists ####
######################

def link_to_list(link):
    """Takes a Link and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link(88))
    [88]
    >>> link_to_list(Link.empty)
    []
    """
    # Recursive solution
    if link is Link.empty:
        return []
    return [link.first] + link_to_list(link.rest)

# Iterative solution
def link_to_list(link):
    result = []
    while link is not Link.empty:
        result.append(link.first)
        link = link.rest
    return result


def every_other(s):
    """Mutates a linked list so that all the odd-indiced elements are removed
    (using 0-based indexing).

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s) # removes 2, 4
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length) # removes 3
    >>> odd_length
    Link(5, Link(1))
    >>> two_items = Link(6, Link(7))
    >>> every_other(two_items) # removes 7
    >>> two_items
    Link(6)
    >>> singleton = Link(4)
    >>> every_other(singleton) # doesn't remove anything
    >>> singleton
    Link(4)
    """
    if s is Link.empty or s.rest is Link.empty:
        return
    else:
        s.rest = s.rest.rest
        every_other(s.rest)


def deep_map(f, link):
    """Return a Link with the same structure as link but with fn mapped over
    its elements. If an element is an instance of a linked list, recursively
    apply f inside that linked list as well.

    >>> s = Link(1, Link(Link(2, Link(3)), Link(4)))
    >>> print_link(s)
    <1 <2 3> 4>
    >>> print_link(deep_map(lambda x: x * x, s))
    <1 <4 9> 16>
    >>> print_link(s) # unchanged
    <1 <2 3> 4>
    >>> t = Link(s, Link(Link(Link(5))))
    >>> print_link(t)
    <<1 <2 3> 4> <<5>>>
    >>> print_link(deep_map(lambda x: 2 * x, t))
    <<2 <4 6> 8> <<10>>>
    """
    if link is Link.empty:
        return link
    if isinstance(link.first, Link):
        first = deep_map(f, link.first)
    else:
        first = f(link.first)
    return Link(first, deep_map(f, link.rest))

