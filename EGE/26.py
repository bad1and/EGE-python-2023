# f = open(r"C:\Users\OLEG\Desktop\26_demo.txt").readlines()
#
# f = [int(i) for i in f]
# f = sorted(f)
#
# mini = []  # <50
# ff = []  # >50
# fff = []  # проценты к ним
# for i in f:
#     if i < 50:
#         mini.append(i)
#     if i > 50:
#         ff.append(i)
#
# for i in ff[0:482]:
#     fff.append(i)
#
# skidka = []
# for i in range(len(fff)):
#     if fff[i] > 0:
#         skidka.append(fff[i] * 0.75)
# bezz = []
#
# # mini + skidka + ff[483:-1]
# for i in ff[482:965]:
#     bezz.append(i)
#
# print(int(round(sum(mini) + sum(skidka) + sum(bezz) , 0))) #первый ответ
# print(max(fff)) # второй ответ


# f = open(r"C:\Users\OLEG\Desktop\26.txt").readlines()
#
# del f[0]
#
# f = sorted([list(map(int, i.split())) for i in f])
# f.sort(key=lambda x: x[1])
#
#
# z = []
# y = []
# k = 0
# pr = f[0][1]
# for i in range(1, len(f)):
#     if f[i][0] >= pr + 15:
#         z.append(pr)
#         pr = f[i][1]
#         k+=1
#     y.append(f[i][0])
# print(sorted(y))

# print(z)
# print(len(z) + 1) # к-во мероприятий

# del f[0:2]
#
# f = list(map(int, f))
# # f.sort(key=lambda x: x[1])
#
# det = sorted(f[0:18746]) # обьем деталей
# kont = sorted(f[18746:]) # обьем контейнеров Отсорт М - Б
#
#
# maxi = -10
# k = 0
# for x in range(len(kont)):
#     for i in range(len(det)):
#         if det[i] != 0:
#             if kont[x] >= det[i]:
#                 k += 1
#                 # print(k, kont[x], det[i], 'ДО')
#                 kont[x] -= det[i]
#                 if det[i] > maxi:
#                     maxi = max(det[i], maxi)
#                 det[i] = 0
#                 # print(k, kont[x], det[i], 'ПОСЛЕ')
# print(k , maxi)


# del f[0]
# del f[0]
# f = sorted([list(map(int, i.split())) for i in f])
# h = [0] * 210
# k = 0
# yach = 0
# for i in range(len(f)):
#     for x in range(len(h)):
#         if f[i][0] >= h[x] + 1:
#             h[x] = f[i][1]
#             k += 1
#             yach = x + 1
#             break
# print(k, yach)
#
#
# for i in range(len(a) - 1):
#     if a[i][0] == a[i + 1][0] and a[i + 1][1] - a[i][1] == 14:
#         ryad.append(a[i])
# print(ryad)

f = open(r"C:\Users\OLEG\Desktop\1.txt").readlines()
f = [list(map(int, i.split())) for i in f]
x = []
for s in range(len(f)):
    x.append([f[s][0], f[s][0] + f[s][1]])
x.sort(key=lambda x: x[1])

k = 1
z = []
m = 0
last = x[0][1]
for i in range(1, len(f)):
    if x[i][0] >= last:
        z.append(last)
        last = x[i][1]
        k += 1
    # print(x[i][0])
    if x[i][0] >= 1300:
        m = max(m, x[i][0] - 1300)
print(k , m)

