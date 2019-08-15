from functools import lru_cache


@lru_cache(maxsize=None)
def routes(a, b):
    if a > b:
        return routes(b, a)
    elif a == 0:
        return 1
    else:
        return routes(a - 1, b) + routes(a, b - 1)


print(routes(20, 20))
