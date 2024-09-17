from functools import lru_cache
@lru_cache(None)

def F(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 == 0:
        return G(n) + F(n - 1)
    if n > 2 and n % 2 != 0:
        return F(n - 2) - 2 * G(n + 1)
def G(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 == 0:
        return F(n-3) + F(n-2)
    if n > 2 and n % 2 != 0:
        return F(n+1) - G(n-1)

print(G(120))


#
# i = 0
# while F(i) != 9:
#     i += 1
# print(i)
#
#
# k = 0
# for x in range (1 ,1048576 + 1):
#     if 1048576 % x ==0:
#         k+=1
# print(k)
#
# f = [0] * 50
# f[1] = 1
# for n in range(2, 100):
#     if n == 0:
#         f[n] = 0
#     if n > 0 and n % 3 == 0:
#         f[n] = f[n // 3]
#     if n % 3 > 0:
#         f[n] = (n%3) + f[n - (n%3)]
# print(f[9])
