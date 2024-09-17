a = open(r'C:\Users\OLEG\Desktop\17.txt').readlines()
a = list(map(int, a))

b = []
for i in range(len(a)):
    if abs(a[i]) % 2 == 1:
        b.append(a[i])

sr = sum(b) / len(b)

m = 0
k = 0
for i in range(len(a) - 1):
    if ((a[i] % 5 == 0 and a[i+1] < sr) or (a[i+1] % 5 == 0 and a[i] < sr)): #первый делится значит второй меньше ср ИЛИ второй делится значит первый меньше
        k += 1
        m = max(m, a[i] + a[i + 1])
print(k, m)