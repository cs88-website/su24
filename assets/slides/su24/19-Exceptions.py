#!/usr/bin/env python
# coding: utf-8

# # CS88 Lecture 19 - Exceptions

# ## Exceptions
# 
# What happens when your program attempts to do something that just can't be done?
# 
# This should not be normal.  It should be rare!  Typically happens when your program encounters and *exceptional* situation

# In[1]:


3/0


# In[6]:


str.lower(1)


# In[3]:


str.lower('HELLO!')


# In[ ]:





# In[7]:


[][3]


# In[6]:


3 % 0


# ## Q: What should a function do?
# 
# ## A: One thing well.
# 
# ## Q: What should it do if it is passed arguments that don't make sense?

# In[1]:


def divides(x, y):
    return y%x == 0


# In[2]:


def get(data, selector):
    return data[selector]


# In[9]:


divides(2,4)


# In[3]:


divides(0,5)
print('Did this work?')


# In[12]:


get([1,2,3],0)


# In[1]:


get({'a': 34, 'cat':'9 lives'}, 'dog')


# In[3]:


# Python Provides built-ins to address errors
{'a': 34, 'cat':'9 lives'}.get('dog', "NO DOG FOUND")


# In[ ]:





# When an error is encountered the python interpreter *throws an exception*.  Here returns all the way to the top level and reports a stack trace of where the exception occured.

# In[26]:


def divides(x, y):
    return y%x == 0
def divides24(x):
    return divides(x,24)
divides24(0)


# In[27]:


divides24(0)


# In[6]:


def apply(f, s):
    return [f(x) for x in s]


# In[7]:


apply(divides24,[6,4,3,5])


# In[8]:


apply(divides24,[6, 4, 0, 3, 5])


# Many types of exceptions:
# 
# * `TypeError` -- A function was passed the wrong number/type of argument
# * `NameError` -- A name wasn't found
# * `KeyError` -- A key wasn't found in a dictionary
# * `RuntimeError` -- Catch-all for troubles during interpretation

# The flow of control stops at the exception and is 'thrown back'. Here the return (and the print) is not executed if an exception occurs on the divide.

# In[8]:


def noisy_divides(x, y):
    result = (y % x == 0)
    if result:
        print(f"{x} divides {y}")
    else:
        print(f"{y} does not divide {y}")
    return result


# In[9]:


noisy_divides(4,24)


# In[10]:


noisy_divides(0,24)


# In[9]:


def divides24(x):
    return noisy_divides(x,24)


# In[10]:


divides24(0)


# ## Assertions
# 
# Your functions should do all they can to avoid errors, they should handle them gracefully when they occur, and the should not trust that they are called with valid arguments -
# *treat data as dirty till you've washed it*.
# 
# The most common form of throwing exceptions is with the `assert` statement.  Use it generously. Make sure that you code is working on something reasonable before it tries to do its stuff.  It serves as good documentation of the assumptions that your code makes.  And it avoids lots of very obscure bugs.
# 
#     asset <assertion expression>, <string for failed assertion>
#     
# Assert statements raise an exception of type `AssertionError`

# In[11]:


def divides(x, y):
    assert x != 0, "Bad argument to divides - denominator should be non-zero"
    assert (type(x) == int and type(y) == int), "divides only takes integers"
    return y%x == 0


# In[12]:


divides(0,3)


# In[13]:


divides(9, "lives")


# In[24]:


def divides24(x):
    return divides(x,24)


# In[13]:


apply(divides24,[6,0,4,3,5])


# In[48]:


divides(5, 10.5)


# ## Handling errors
# 
# How can you continue in the presence of an error?  Is there a way to *handle the exception*?
# 
# The general form of this construct is
# 
#     try:
#         <try suite>
#     except <exception class> as <name>:
#         <except suite>
#     ... # continue here if <try suite> succeeds without exception

# In[14]:


def safe_apply_fun(f,x):
    try:
        print('Trying to executue f of x', x)
        return f(x)   # normal execution, return the result
    except:           # error occured, f cannot return.  Transfer control back to here
        return "Invalid"   # value returned on exception


# In[19]:


def divides(x, y):
    return y%x == 0
def divides24(x):
    return divides(x,24)
print(safe_apply_fun(divides24,0))
print('We made it!')


# In[53]:


def apply(f, s):
    return [safe_apply_fun(f,x) for x in s]


# In[55]:


apply(divides24,[6,0,4,3,5])


# In[56]:


safe_apply_fun(divides24, 8)


# In[59]:


def rapply(f, s):
    if len(s) == 0:
        return []
    else:
        return [f(s[0])] + rapply(f, s[1:])


# In[60]:


rapply(divides24, [6,4,3,5])


# In[ ]:


rapply(divides24, [6,4,3,0,5])


# In[61]:


def rapply(f, s):
    if len(s) == 0:
        return []
    else:
        return [safe_apply_fun(f, s[0])] + rapply(f, s[1:])


# In[62]:


rapply(divides24, [6,4,3,0,5])


# In[23]:


def safe_apply_fun(f,x):
    try:
        return f(x)   # normal execution, return the result
    except Exception as e:  # exceptions are objects of class derived from base class Exception
        print('An Error occured!')
        print(f'x was: {x}')
        return e   # value returned on exception


# In[24]:


print(safe_apply_fun(divides24,0))
print('I made it!')


# In[ ]:


res = apply(divides24, [6,4,3,0,5])
res


# In[ ]:


res[3]


# In[ ]:


type(res[3])


# ## More on except
# 
# The general form of this construct is
# 
#     try:
#         <try suite>
#     except <exception class> as <name>:
#         <except suite>
#     ... # continue here if <try suite> succeeds without exception
# 
# Execution rule:
# The `<try suite>` is executed first.
# If during the course of executing the `<try suite>`
# * an exception is raised that is not handled otherwise, and
# * if the class of the exception inherits from `<exception class>`, then
# * the `<except suite>` is executed, with `<name>` bound to the exception
# 
# Note:
# * There can be more than one `except` clause for a `try`.
# * They may specify a tuple of exception types.
# * The first one that catches the exception receives control.
# * If none do (or if there is no `try ... except`) control is thrown out of the function call.
# * Each of the function calls on the stack may define exception handlers.  Control is transferred to nearest catching exception suite on the stack.

# In[ ]:


def safe_apply_fun(f,x):
    try:
        return f(x)   # normal execution, return the result
    except AssertionError as e:
        return "Failed Assertion"
    except (TypeError, NameError):
        return "Bad function or arg type"


# In[ ]:


safe_apply_fun(divides24, 0)


# In[ ]:


safe_apply_fun("foo", 0)


# In[ ]:


safe_apply_fun(divides25, 0)


# In[ ]:


safe_apply_fun(lambda x: 24 % x == 0, 0)


# ## Raising your own exceptions
# 
# Exceptions are raised with a `raise` statement:
# 
# `raise <expression>`
# 
# `<expression>` must evaluate to a subclass of BaseException or an instance of one
# 
# Exceptions are constructed like any other object. E.g., `TypeError('Bad argument!')`

# In[ ]:


TypeError("ugly type")


# In[ ]:


assert 1 < 2, "My Assertion"


# In[ ]:


def divides(x, y):
    assert x != 0, "Bad argument to divides - denominator should be non-zero"
    if (type(x) != int or type(y) != int):
        raise TypeError("divides only takes integers")
    return y%x == 0


# In[ ]:


divides("cat",9)


# In[ ]:


safe_apply_fun(divides24, "cat")


# ## Exceptions are classes
# 
# They have constructors, selectors, methods, etc.

# In[27]:


class CS88Error(Exception):
    pass


# In[28]:


def get_age_in_days():
    try:
        age = float(input("What is your age? "))
        assert age > 0, "Negative age, really?"
        age_in_days = age * 365 + (age // 4)
        if age_in_days > (365 * 150):
            raise CS88Error('That number seems too large!')
        print(f"your age in days: {age_in_days}")
    except AssertionError:
        print("Need an age > 0")
    except CS88Error as e:
        print('Catching CS88Error')
        raise e
    except:
        print("Need a valid age Try again!")
        get_age_in_days()
    print('Done!')


# In[29]:


get_age_in_days()


# In[ ]:





# In[ ]:





# --- 
# ### Optional Examples below here...
# 

# In[ ]:





# In[20]:


# Exceptions are classes too
class Noisyxception(Exception):
    def __init__(self, stuff):
        print("Bad stuff happenned", stuff)


# In[ ]:





# In[15]:


# We can nest / try-catch to recover from other types of errors. 

def nostop(fun, x):
    try: 
        try:
            return fun(x)
        except:
            raise NoiseyException((fun, x))
    except:
        return None


# In[16]:


def reciprocal(x):
    return 1/x
nostop(reciprocal, 0)


# In[17]:


def zapper(fun, seq, selectors):
    return [nostop(fun, seq[x]) for x in selectors]


# In[18]:


zapper(reciprocal, [1, 0, 2, 0], [0, 1, 2, 3])


# In[ ]:


zapper(reciprocal, [1, 0, 2, 0], [0, 1, 2, 3, 4])


# In[ ]:


def zing(seq, i):
    try: 
        try:
            return seq[i]
        except:
            raise NoiseyException(("bad sequence index", i))
    except:
        return None

def zapper(fun, seq, selectors):
    return [nostop(fun, zing(seq, x)) for x in selectors]


# In[ ]:


zapper(reciprocal, [1, 0, 2, 0], [0, 1, 2, 3, 4])


# In[ ]:


class NoiseyException(Exception):
    exceptions = []
    def __init__(self, stuff):
        print("Bad stuff happenned", stuff)
        NoiseyException.exceptions.append(stuff)


# In[ ]:


zapper(reciprocal, [1, 0, 2, 0], [0, 1, 2, 3, 4])


# In[ ]:


NoiseyException.exceptions


# In[ ]:




