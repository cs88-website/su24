def iter_fib(n):
    x, y = 0, 1
    for _ in range(n):
       x, y = y, x+y
    return x


def fib(n): # Recursive
    if n < 2:
       return n
    return fib(n - 1) + fib(n - 2)


fib_results = {}
def memo_fib(n): # Look up values in our dictionary.
    global fib_results
    if n in fib_results:
        print(f'found {n} -> {fib_results[n]}')
        return fib_results[n]
    if n < 2:
        fib_results[n] = n
        return n
    result = memo_fib(n - 1) + memo_fib(n - 2)
    fib_results[n] = result
    return result

from functools import cache

# We use a different name just to make it clear.
@cache
def cache_fib(n): # Recursive
    if n < 2:
        return n
    return cache_fib(n - 1) + cache_fib(n - 2)

# However, we do not need to use the decorator like this:
alt_cache_fib = cache(fib)
