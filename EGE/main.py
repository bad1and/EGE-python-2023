k = int(input())
w = int(input())
h = int(input())
t = int(input())

d = k + t
w = d * w + t
h = d * h + t

for y in range(h):
    l = y % d < t
    for x in range(w):
        print(".*"[l or x % d < t], end="")
    print()

x = int(input())
l = int(input())
r = int(input())
k = 0
res = [i for i in range(l, r + 1)]
res1 = []
if 1 <= l <= r <= 10 ** 9 and r - l <= 1000:
    if x != 1:
        for y in range(l, r + 1):
            for i in range(1, y + 1):
                for g in range(1, y + 1):
                    if x != y and x % i == 0 and x % g == 0 and y % g == 0 and y % i == 0 and i != g and i != 1 and g != 1:
                        res1.append(y)
                        k += 1
res2 = list(filter(lambda x: not (x in res1), res))
print(len(res2))
for i in (list(set(res2))):
    print(i,end=' ')


# n = int(input())
#
# k = 0
# if 1 <= n <= 80:
#     for a in range(0, n + 1):
#         for b in range(0, n + 1):
#             for c in range(0, n + 1):
#                 for d in range(0, n + 1):
#                     for e in range(0, n + 1):
#                         for f in range(0, n + 1):
#                             for g in range(0, n + 1):
#                                 for h in range(0, n + 1):
#                                     for i in range(0, n + 1):
#                                         if (a < b < c < d < e < f < g < h < i) and (
#                                                 a + b + c + d + e + f + g + h + i) == n:
#                                             k += 1
#                                             print(a, b, c, d, e, f, g, h, i)
# print("OLEG DEBIL")
# print(k)
