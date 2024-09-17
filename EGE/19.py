from functools import *

def moves(s):
    if s % 2 == 0:
        return s - 1, s - (s // 2)
    else:
        return s - 1, s - (s // 3)


@lru_cache(None)
def g(s):
    if s < 12: return 'w'
    if any(g(m) == 'w' for m in moves(s)): return 'p1'
    if all(g(m) == 'p1' for m in moves(s)): return 'v1'  # Петя


for s in range(12, 100):
    if g(s) == 'v1':
        print(s, g(s))

# from functools import *
# def moves(s):
#     a,b = s
#     return (a+1,b),(a,b+1),(a*5,b),(a,b*5)
#
# @lru_cache(None)
# def g(s):
#     a,b = s
#     if a+b >= 101: return 'w'
#     if any(g(m) == 'w' for m in moves(s)): return 'p1'
#     if any(g(m) == 'p1' for m in moves(s)): return 'v1'
#
# for s in range(1,100+1):
#     s = 8,s
#     if g(s) == 'v1':
#         print (s, g(s))

# отрицание в условии
# from functools import *
# def moves(s):
#     a,b = s
#     return (a-1,b),(a,b-1),(a//2 + a%2,b),(a,b//2+ b%2)
#
# @lru_cache(None)
# def g(s):
#     a,b = s
#     if a <= 1 or b <= 1: return 0 # ошибка бесконечной рекурсии
#     if a+b <= 40: return 'w'
#     if any(g(m) == 'w' for m in moves(s)): return 'p1'
#     if any(g(m) == 'p1' for m in moves(s)): return 'v1'
#
# for s in range(21,100):
#     s = 20,s
#     if g(s) == 'v1':
#         print (s, g(s))
