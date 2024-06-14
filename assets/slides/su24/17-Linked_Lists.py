#!/usr/bin/env python
# coding: utf-8

# # Data Structures: Linked Lists
# ## We'll learn some new Python tools, too.

# In[2]:


class Link:
    """A linked list.
    >>> s = Link(3, Link(4, Link(5)))
    >>> len(s)
    3
    >>> s[2]
    5
    >>> s
    Link(3, Link(4, Link(5)))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(self.first, rest_str)

    def __len__(self):
        if self.rest == Link.empty:
             return 1
        return 1 + len(self.rest)

def print_link(link):
    if not link:
        return
    print(link.first)
    print_link(link.rest)

def print_link(link):
    if not link:
        return
    item = link
    while item:
        print(item.first)
        item = item.rest


def get_item(l, index):
    if not l:
        return None
    if index == 0:
        return l.first
    return get_item(l.rest, index - 1)

l1 = Link(1)
l1


s = Link(3, Link(4, Link(5)))
s

letters =  Link('A', Link('B', Link('C', Link('D', Link('E')))))
# In[15]:


s.rest

len(s)


# In[19]:


#  s.__len__()


# In[21]:


# __len__(s)

# 1 + len(rest) (4, Link...)
# 1 + 1 + len(rest) Rest: Link(5)
# 1 + 1 + 1 + len(empty) len(())


# In[28]:


print(s.rest.rest.rest)
len(s.rest.rest.rest)


# In[47]:


class Link:
    """A linked list.
    >>> s = Link(3, Link(4, Link(5)))
    >>> len(s)
    3
    >>> s[2]
    5
    >>> s
    Link(3, Link(4, Link(5)))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __len__(self):
        return 1 + len(self.rest)

    def to_list(self):
        if not self:
            return []
        if not self.rest:
            return [self.first]
        return [self.first] + self.rest.to_list()

    # You probably do not want to actually do this!
    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i - 1]

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(self.first, rest_str)


# In[48]:


s = Link(3, Link(4, Link(5)))


# In[57]:


s[1]


# In[58]:


s[2]


# In[61]:


# __getitem__

# i = 2:
# self.rest = Link(4, Link(5))
# self.rest[1]

# i = 1
# self.rest = Link(5)
# self.rest[0]

# i = 0
# self.first == 5


# # Notes about How `Link` Works:

# In[ ]:


# Optional Arguments
# an = after an argument makes it "optional" and provides a default value.
def my_fun(x, y=1):
    return x, y

my_fun(10)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[62]:


names = Link('Michael', Link('Alex'))


# In[63]:


names[1]


# ### What happens if we directly set `Link.rest`?

# In[64]:


names.rest.rest = 'Amir'


# In[65]:


names


# In[69]:


len(names) # What?? Consider why this happens.


# In[70]:


names[2]


# In[ ]:





# In[75]:


# A final expanded Link Class

class Link:
    """A linked list.
    >>> s = Link(3, Link(4, Link(5)))
    >>> len(s)
    3
    >>> s[2]
    5
    >>> s
    Link(3, Link(4, Link(5)))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(self.first, rest_str)

    def __setattr__(self, name, value):
        # Assert that self.rest is always a kind of Link() if we set it directly.
        # https://docs.python.org/3/reference/datamodel.html#object.__setattr__
        if name == 'rest':
            assert value is Link.empty or isinstance(value, Link), "More Info..."
        self.__dict__[name] = value


# #

# # In[76]:


# names = Link('Michael', Link('Alex'))


# # In[77]:


# names


# # In[80]:


# # Now, we'll get an error!
# names.rest.rest = 'Amir'


# In[ ]:
