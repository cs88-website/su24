from functools import reduce
from operator import add

# A Functional Oriented approach
def acronym_f(words):
    return reduce(add,
                map(lambda w: w[0],
                filter(lambda w: len(w) > 3,
                        words.split(' '))))

# A traditional imperative approach
def acronym_i(words):
    result = ''
    words = words.split(' ')
    for word in words:
        if len(word) > 3:
            result += word[0]
    return result

# A "hybird" approach. Mixes paradigms
def acronym_h(words):
    words = words.split(' ')
    long = filter(lambda w: len(w) > 3, words)
    letters = mapa(lambda w: w[0], long)
    return ''.join(letters)

# Kind of data centric / arrays.
def acronym_list(words):
    return ''.join([w[0] for w in words.split(' ') if len(w) > 3])
