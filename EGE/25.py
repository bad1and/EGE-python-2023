# alf = '0123456789'
# zv = []
# rez = []
# for a in alf:
#     zv.append(a)
# for a in alf:
#     for b in alf:
#         zv.append(a + b)
# for a in alf:
#     for b in alf:
#         for c in alf:
#             zv.append(a + b + c)
# zv.append('')

# for a in alf:
#     for b in zv:
#         for c in zv:
#             x = '12' + a + c + '36' + b + '1'
#             x = int(x)
#             if x % 273 == 0:
#                 rez.append([x, x // 273])
#
# print(sorted(rez))


from fnmatch import *

for x in range(0, 10 ** 10, 1917):
    if fnmatch(str(x), '3?12?14*5'):
        print(x , x//1917)
