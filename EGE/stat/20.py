from functools import *


def moves(s):
    if s % 2 == 0:
        return s - 1, s // 2
    else:
        return s - 1, s - s // 3


@lru_cache(None)
def g(s):
    if s < 12: return 'w'
    if any(g(m) == 'w' for m in moves(s)): return 'p1'
    if all(g(m) == 'p1' for m in moves(s)): return 'v1'
    if any(g(m) == 'v1' for m in moves(s)): return 'p2'  # Петя


for s in range(12, 100):
    if g(s) == 'p2':
        print(s, g(s))
