# 2 - 63917315
# for x in range(130):
#     a = 2 * 130 ** 4 + 3 * 130 ** 3 + x * 130 ** 2 + 3 * 130 + 2
#     b = 3 * 130 ** 4 + x * 130 ** 3 + 2 * 130 ** 2 + 5 * 130 + 3
#     if (a + b) % 23 == 0:
#         print((a + b) // 23)


# 4 - 552647
# alf = '0123456789A'
# for x in alf:
#     for y in alf:
#         a = int('7' + y + '23' + x + '5', 25)
#         b = int('67' + x + '9' + y, 11)
#         if (a + b) % 131 == 0:
#             print((a + b) // 131)


# 9 - 5718
# n = 7 * 5 ** 1984 - 6 * 25 ** 777 + 5 * 125 ** 333 - 4
# s = 0
# while n > 0:
#     s = s + n%5
#     n //= 5
# print(s)

# 16 - ?
# for p in range(7, 17):
#     for x in range(p):
#         for y in range(p):
#             for z in range(p):
#                 s = y * (p**2) + 4 * p + y + y * (p**2) + 6 * p + 5
#                 r = x * (p**3) + z * (p**2) + 3 * p + 3
#                 if s == r:
#                     print(x * (p**2) + y * p + z)
for p in range(10, 17):
    for x in range(p):
        for y in range(p):
            for z in range(p):
                s = 3 * (p ** 3) + 2 * (p ** 2) + x * p + 8 + x * (p ** 3) + x * (p ** 2) + x * p + 9  # 32x8 + xxx9
                r = y * (p ** 3) + y * (p ** 2) + 0 + 2  # yy02
                if s == r:
                    print(y * (p ** 2) + y * (p) + x , y , x)  # yyx
