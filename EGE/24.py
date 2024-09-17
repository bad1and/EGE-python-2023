s = open(r"C:\Users\OLEG\Desktop\24.txt").readline()
alf = str(s)

z = []
for i in range(len(s) - 1):
    if s[i] == 'E':
        z.append(s[i + 1])

res={i:z.count(i) for i in z}

print(res)


# alf = 'ABCDEF'
# for y in alf:
#     a = []
#     for i in range(len(s)):
#         if s[i] == y:
#             a.append(i)
#             if len(a) == 100:
#                 otv.append(a[-1] - 1)
#
# print(otv)

# alf = '0123456789ABCDEFGHIJKLMN'
# k = 0
# maxx = 0
# for i in range(1, len(s)):
#     if s[i] in alf:
#         k += 1
#         maxx = max(k , maxx)
#     else:
#         k = 0
# print(maxx)

# s = 'ACDFOACDFO----ACDFO' # AC


# s = open(r"C:\Users\OLEG\Desktop\24.txt").readline()
# k = ka = last = 0
# for x in s:
#     if x == 'A':
#         k += ka - (last == 'A')
#         ka += 1
#     last = x
# print(k)


# chisla = []
# res = []
#
# for i in range(len(s)):
#     if s[i] == 'T':
#         chisla.append(i)
#
# for i in range(len(chisla) - 101):
#     res.append(len(s[chisla[i]: chisla[i + 99] + 1]))
# print(max(res))
#
#
# for i in range(len(s)-1):
#     ns = 'D'.join(s[i:i+1+1])
#     m = max(m,len(ns))
# print(m)
#
# # s = 'tyuiuooda---'
#
# ns = ''
# m = 0
#
# for sim in s:
#     ns += sim
#     if 'ad' not in ns and 'da' not in ns:
#         m = max(m, len(ns))
#     if 'ad' in ns:
#         ns = 'd'
#     if 'da' in ns:
#         ns = "a"
# print(m)
#
# s = ""
#
# count = 0
# count_old = 0
# m = 0
#
# for i in s:
#     if i == "K":
#         m = max(m, count + count_old + 1)
#         count_old = count
#         count = 0
#     else:
#         count += 1
#     if i == "L":
#         m = max(m, count + count_old + 1)
#         count_old = count
#         count = 0
#     else:
#         count += 1
# m = max(m, count + count_old + 1)
# print(m)
#
# ns = ''
# m = 0
# for x in range(1000):
#     ns += 'A'
#     if ns in s:
#         m = max(m, len(ns))
#     ns += 'B'
#     if ns in s:
#         m = max(m, len(ns))
# print(m)
#
# a = {}
# for sim in s:
#     a[sim] = 0
#
# for i in range(len(s) - 2):
#     if (s[i] == "X" and s[i+2] == "Z"):
#         a[s[i+1]] += 1
# print(a)
#
# a = []
# for i in range (len(s) - 2):
#     if (s[i] == s[i+2]):
#         a.append(s[i+1])
# count
# print(a)

# k = 1
# a = []
# for i in range(len(s) - 1):
#     if (s[i] != s[i + 1]):
#         k += 1
#         a.append(k)
#     else:
#         k = 1
# print(max(a))
#
# k = 1
# maxi = []
#
# for i in range(len(s) - 2):
#     if (int(s[i]) + int(s[i + 1])) > int(s[i + 2]):
#         k += 1
#         maxi.append(k)
#     else:
#         k = 0 # k = 2 #58329
#     print(s[i] , k)
# print(max(maxi))
