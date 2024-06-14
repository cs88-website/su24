"""
General Recuesion Examples.
"""

def countdown(n):
    if n == 0:
        print('Blastoff!')
    else:
        # What happens if we swap the order?
        countdown(n - 1)
        print(n)


# countdown(2)
    # countdown(1)
    #   countdown(0)
    #   print(1)
    # print(2)

def countdown_print(n):
    if n == 0:
        print('Blastoff!')
    else:
        # What happens if we swap the order?
        print(f'Before: {n}')
        countdown_print(n - 1)
        print(f'After: {n}')

def sum_of_sqaures_print(n):
    print(f"Sum n: {n}")
    if n < 1:
        return 0
    # elif n < 0: # what if we wanted to handle negative numbers?
        # return sum_of_sqaures_print(n * -1)
        # return squared + sum_of_sqaures_print(n + 1)
    else:
        squared = n**2
        # print (f"N: {n}, Squared: {squared}")
        return squared + sum_of_sqaures_print(n - 1)

def sum_of_sqaures(n):
    if n < 1:
        return 0
    else:
        return n**2 + sum_of_sqaures(n - 1)

def first(s):
    """Return the first element in a sequence."""
    return s[0]

def rest(s):
    """Return all elements in a sequence after the first"""
    return s[1:]

def reverse(s):
    """
    >>> reverse('hello')
    'olleh'
    >>> reverse(reverse('hello'))
    'hello'
    """
    if not s:
        return ''
    return reverse(rest(s)) + first(s)

def reverse_2(s):
    """
    >>> reverse_2('hello')
    'olleh'
    >>> reverse_2(reverse_2('hello'))
    'hello'
    """
    if not s:
        return ''
    last = s[-1]
    all_but_last = s[0:-1]
    return last + reverse(all_but_last)

def min_r(s):
    """Return minimum value in a sequence."""
    if len(s) == 1:
        return first(s)
    else:
        return min(first(s), min_r(rest(s)))

def palindrome(word):
  if len(word) <= 1:
    return True
  elif word[0] == word[-1]:
    return palindrome(word[1:-1])
  return False

def reverse_for(s):
    """
    >>> reverse_for('hello')
    'olleh'
    """
    result = ''
    for letter in s:
        result = letter + result
        print(result)
    return result

def reverse_while(s):
    """
    >>> reverse_while('hello')
    'olleh'
    """
    result = ''
    while s:
        first = s[0]
        s = s[1:] # remove the first letter
        result = first + result
    return result


def reverse_print(s):
    """
    >>> reverse_recur('hello')
    'olleh'
    """
    if not s:
        return ''
    print('Pre-recursive-call:' , s[0], s[1:])
    result = reverse_print(s[1:]) + s[0]
    print(result)
    return result

def palindrome_iter(word):
    """"
    >>> palindrome_iter('racecar')
    True
    """
    while word:
        if word[0] != word[-1]:
            return False
        word = word[1:-1]
    return True



### Pascal's Triangle
def generate_pascal_triangle(n):
    if n == 1:
        return [[1]]
    else:
        prev_triangle = generate_pascal_triangle(n - 1)
        last_row = prev_triangle[-1]
        new_row = [1]

        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])

        new_row.append(1)
        prev_triangle.append(new_row)

        return prev_triangle
