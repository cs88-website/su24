text = "Hello, C88C!"
index = 0

# Some background:
text[0] # == "H"
while index < len(text):
    print(text[index])
    index += 1 # Same as index = index += 1

total = 0
n = 1
while n <= 10:
    total += n
    n += 1
print(total)

def sum_to_n(n):
    """
    >>> sum_to_n(10)
    55
    """
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

def sum_to_n_down(n):
    """
    >>> sum_to_n(10)
    55
    """
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total

total = 0
for num in range(0, 11):
    total += num
print(total)

text = "Hello, C88C!"
for letter in text:
    print(letter)

def sum_to_n(n):
    total = 0
    for num in range(0, n + 1):
        total += num
    return total

def sum_to_n_down(n):
    total = 0
    for num in range(n, 0, -1):
        total += num
    return total

sum(range(0, 11))

def sum_to_n(n):
    return sum(range(0, n + 1))

text = 'Hello, C88C!'
len(text)
text.count('l')
text.count(8)
text.count('8')

courses = ['DATA C88C', 'DATA 8', 'POLSCI 2', 'MATH 54']

list(range(0, 11))

numbers = [ x for x in range(11) ]

numbers = [2 ** x for x in range(10) ]

courses[0]
courses[0].split(' ')
[ c.split(' ') for c in courses ]

courses = ['DATA C88C', 'DATA 8', 'POLSCI 2', 'MATH 54']

departments = [ c.split(' ')[0] for c in courses ]
