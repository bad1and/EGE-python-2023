a = open(r'C:/Users/OLEG/Desktop/17.txt').readlines()
a = list(map(int, a))
maxi = max([x for x in a if x % 1000 == 832])
summ = []
k = 0

for i in range(len(a) - 2):
    if (a[i] + a[i + 1] + a[i + 2]) > maxi:
        if (((a[i] % 5 == 0) + (a[i + 1] % 5 == 0) + (a[i + 2] % 5 == 0)) > ((a[i] % 3 == 0) + (a[i + 1] % 3 == 0) + (a[i + 2] % 3 == 0))):
            if ((len(str(a[i])) == 4) + (len(str(a[i + 1])) == 4) + (len(str(a[i + 2])) == 4)) >= 1:
                k += 1
                summ.append(a[i] + a[i + 1] + a[i + 2])
print(k, max(summ))