def add_one(n):
    return n + 1

add_one(3)

def make_adder(n):
    def adder(x):
        return x + n
    return adder

add_1 = make_adder(1)
add_1(3)

add_4 = make_adder(4)
add_4(5)

def leq_maker(c):
    def leq(val):
        return val <= c
    return leq

def compose(f, g):
    def h(x):
      return f(g(x))
    return h

add_2 = make_adder(2)
add_3 = make_adder(3)
x = add_2(3)

add_5 = compose(add_2, add_3)
y = add_5(x)

z = compose(square, make_adder(2))(3)




def say_hi(name):
    print(f'Hi, {name}')

say_hi = lambda name: print(f'Hi, {name}')

fruits = ["pear", "grape", "KIWI", "APPLE", "melon", "ORANGE", "BANANA"]
sorted(key=lambda x: x.lower())


sorted([5, 4, 3, 2, 1])

# This is the "identity" function
sorted([5, 4, 3, 2, 1], key = lambda x: x)

sorted([1,2,3,4,5], key = lambda x: -x)

sorted([(2, "hi"), (1, "how"), (5, "goes"), (7, "I")], key = lambda x:x[0])

sorted([(2, "hi"), (1, "how"), (5, "goes"), (7, "I")], key = lambda x:x[1])

sorted([(2,"hi"),(1,"how"),(5,"goes"),(7,"I")], key =lambda x: len(x[1]))

full_names = ['Rebecca Dang', 'Ramya Chitturi', 'Aymeric Barrier', 'Sean Yang', 'Joanna Yoo', 'Amit Sant', 'Michelle Chen', 'John Teng', 'Lukas Chang', 'Anjali Gurajapu', 'Christine Zhang', 'Ethan Yoo', 'Karim Kaylani', 'Mingxiao Wei', 'Michael Ball', 'Sebastian Zhao', 'Hetal Shah']

staff = list(map(lambda w: w.split()[0], full_names))
# staff = ['Anjali', 'Mingxiao', 'Aymeric', 'Karim', 'Ethan', 'Michelle', 'Christine', 'Joanna', 'Lukas', 'John', 'Sebastian', 'Sean', 'Amit', 'Michael', 'Ramya', 'Rebecca', 'Hetal']

sorted(staff)

sorted(staff, key = lambda name: len(name))

# More practice with map / filter / reduce
remove_dupes = lambda result, data: result if data in result else result + [ data ]

from functools import reduce
reduce(remove_dupes, staff, [])
