# k = 0
# ch = "02468"
# nech = "13579"
# for a in l:
#     for b in l:
#         for c in l:
#             for d in l:
#                 for e in l:
#                     for f in l:
#                         # k+=1
#                         s = a + b + c + d + e + f
#                         if (s[0] % 2 != 0 and (s[-1] in 0 or s[-1] in 5) and
#                                 (s.count("0") <= 1 and
#                         s.count("1") <= 1 and
#                         s.count("2") <= 1 and
#                         s.count("3") <= 1 and
#                         s.count("4") <= 1 and
#                         s.count("5") <= 1 and
#                         s.count("6") <= 1 and
#                         s.count("7") <= 1 and
#                         s.count("8") <= 1 and
#                         s.count("9") <= 1)
#                                 and
#                         ((s[0] in ch and
#                         s[1] in nech and
#                         s[2] in ch and
#                         s[3] in nech and
#                         s[4] in ch and
#                         s[5] in nech)
#                          or
#                         (s[0] in nech and
#                         s[1] in ch and
#                         s[2] in nech and
#                         s[3] in ch and
#                         s[4] in nech and
#                         s[5] in ch))
#                         ):
#                             k += 1
# print(k)


# ---------------------------------------------------

# q = 0
# alf = "12345678"
# for a in alf:
#     for b in alf:
#         for c in alf:
#             for d in alf:
#                 for e in alf:
#                     for f in alf:
#                         for g in alf:
#                             for h in alf:
#                                 for i in alf:
#                                     for j in alf:
#                                         for k in alf:
#                                             s = a + b + c + d + e + f + g + h + i + j + k
#                                             if (((int(s[0]) % 2 == 0 and
#                                                   int(s[1]) % 2 != 0 and
#                                                   int(s[2]) % 2 == 0 and
#                                                   int(s[3]) % 2 != 0 and
#                                                   int(s[4]) % 2 == 0 and
#                                                   int(s[5]) % 2 != 0 and
#                                                   int(s[6]) % 2 == 0 and
#                                                   int(s[7]) % 2 != 0 and
#                                                   int(s[8]) % 2 == 0 and
#                                                   int(s[9]) % 2 != 0 and
#                                                   int(s[10]) % 2 == 0)
#                                                  or
#                                                  (int(s[0]) % 2 != 0 and
#                                                   int(s[1]) % 2 == 0 and
#                                                   int(s[2]) % 2 != 0 and
#                                                   int(s[3]) % 2 == 0 and
#                                                   int(s[4]) % 2 != 0 and
#                                                   int(s[5]) % 2 == 0 and
#                                                   int(s[6]) % 2 != 0 and
#                                                   int(s[7]) % 2 == 0 and
#                                                   int(s[8]) % 2 != 0 and
#                                                   int(s[9]) % 2 == 0 and
#                                                   int(s[10]) % 2 != 0))
#
#                                                     and
#
#                                                     (s.count("1") <= 4 and
#                                                      s.count("2") <= 4 and
#                                                      s.count("3") <= 4 and
#                                                      s.count("4") <= 4 and
#                                                      s.count("5") <= 4 and
#                                                      s.count("6") <= 4 and
#                                                      s.count("7") <= 4 and
#                                                      s.count("8") <= 4)
#                                             ):
#                                                 q += 1
#                                                 print(q)


# from itertools import *
# k = 0
# a = product('12345678',repeat=11)
# y = [' '.join(i) for i in a]
# for r in y:
#     l = [i for i in r if r.count(i) <= 4]
#     l2 = [i for i in range(len(r) - 1) if int(r[i]) % 2 != int(r[i + 1]) % 2]
#     if len(l) and len(l2) == len(r):
#         k += 1
# print(k)

from itertools import product
k = 0
for x in product("0123", repeat=4):
   if x[0] != '0' and len(set(x)) < 4:
       k+=1
print(k)