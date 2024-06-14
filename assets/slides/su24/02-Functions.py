# This file is short. see the 02-Functions.txt
# for a log of everything demoed.

3 + 5
(3 + 5) * 11
True
1
88 > 61
88 > 61 + 100
course = 'C88C'
course
print('Hello, ' + course)
Hello, C88C
# >>> 'C88C"
#   File "<stdin>", line 1
#     'C88C"
#     ^
# SyntaxError: unterminated string literal (detected at line 1)
# >>> "C88C"
# 'C88C'
print(True)
result = print('Hello, ' + course)
# Hello, C88C
result
max(88, 61)
result = max(88, 61)
result

def add_8(num):
   """add 8 to the input num
   >>> add_8(80)
   88
   """
   return 8 + num

add_8(80)

def add_8_print(num):
   """add 8 to the input num
   >>> add_8_print(80)
   88
   """
   print(8 + num)

>>> add_8_print(80)
>>> value =add_8_print(80)
>>> value
