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

# a = open(r'C:/Users/OLEG/Desktop/17-382.txt').readlines()
# a = list(map(int, a))

# k = 0
# m = 0
# j = -1000000000000000
#
# for i in range(len(a) - 2):
#     if ():
#         k += 1
#         j = max(j, a[i] + a[i + 1] + a[i + 2])
# print(k, j)

#
# s=[int(i) for i in open('17 (7).txt')]
# res=[]
# for i in range(len(s)-1):
#     for j in range(i+1,len(s)):
#         if (s[i]-s[j])%36==0 and (s[i]%13==0 or s[j]%13==0):
#             res.append(s[i]-s[j])
# print(len(res),max(res))
