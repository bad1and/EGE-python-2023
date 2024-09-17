# f = open(r"C:\Users\OLEG\Desktop\27_B.txt").readlines()
#
# f = list(map(int, f))  # расстояние 155
# k = f[0]
# del f[0:2]
#
# a = -100000000000
# b = -100000000000
# ms = -100000000000
#
# for i in range(k * 2, len(f)):
#     a = max(a, f[i - k * 2])  # 14
#     b = max(b, a + f[i - k])  # 35
#     ms = max(ms, b + f[i])  # 45
#     # print(f'a: {a} , a: {b} , ms: {ms}')
#
# print(ms)


# z = []
# for a in range(len(f)):
#     for b in range(a + 1, len(f)):
#         for c in range(b + 1, len(f)):
#             if (b - a >= 2) and (c - b >= 2):
#                 z.append(f[a] + f[b] + f[c])
#                 # print(f[a], f[b], f[c], summ)
# print(min(z))


# del f[0:2]
#
# maxii = 0
# maxii2 = 0
# for i in range(3, len(f)):
#     maxii = max(maxii, f[i - 3]) #максимальные элементы
#     maxii2 = max(maxii2, maxii + f[i])
#
# print(maxii2)
# z = []
# for i in range(len(f)):
#     for x in range(len(f)):
#         if i - x >= 3:
#             z.append(f[i] + f[x])
# print(max(z))


a = open(r"C:\Users\OLEG\Desktop\27A.txt").readlines()
a = list(map(int, a))


n = a[0]
a = a[1:]

sm = [0] * n
for i in range(n):
    for j in range(n):
        r = min(abs(j - i), n - abs(j - i))
        sm[i] += a[j] * r
print(sm)
print(min(sm) * 3, min(sm).__index__())

for x in range(len(sm)):
    if sm[x]==157076:
        print(x+1)

# for i in range(len(sm)):
#     if sm[i] == 3025:
#         print(i + 1)
