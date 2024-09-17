f = open(r"C:\Users\OLEG\Desktop\26.txt").readlines()
del f[0:2]

f = list(map(int, f))
# f.sort(key=lambda x: x[1])

det = sorted(f[0:18746]) # обьем деталей
kont = sorted(f[18746:]) # обьем контейнеров Отсорт М - Б


maxi = -10
k = 0
for x in range(len(kont)):
    for i in range(len(det)):
        if det[i] != 0:
            if kont[x] >= det[i]:
                k += 1
                # print(k, kont[x], det[i], 'ДО')
                kont[x] -= det[i]
                if det[i] > maxi:
                    maxi = max(det[i], maxi)
                det[i] = 0
                # print(k, kont[x], det[i], 'ПОСЛЕ')
print(k , maxi)