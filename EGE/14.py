# for x in range(15):
#     a = 8*25**5 + x*25**4 + 5*25**3 + 6*25**2 + 7*25 + 8
#     b = 4*25**5 + 5*25**4 + 7*25**3 + x*25**2 + 6*25 + 9
#     c = 1*25**4 + 4*25**3 + 5*25**2 + x*25 + 1
#     if (a+b+c) % 21 == 0:
#         print ((a+b+c) // 21)


# for p in range(7, 17):
#     for x in range(p):
#         for y in range(p):
#             for z in range(p):
#                 a = int(y * 4 * y)
#                 b = int(y * 65)
#                 # c = int("63" + x + "5", 22)
#                 if (a + b) == (x * z * 33):
#                     print(x * (p**2) + y * p + z)

            # x = 36**8 + 6**20 - 12
            # s = ''
            # while x > 0:
            #     s = str(x%6) + s
            #     x = x // 6
            # print (s.count ("5"))

            # s = 8**7 + 4**5 + 2**10 - 32
            # r = bin(s)[2:]
            # r = str(r)
            # print(r.count("1"))

x = 1331**650 - 55*121**610 + 77*11**510 - 3*11**100 - 221
s = ""
while x != 0:
    s += str(x % 11)
    x //= 11
s = s[::-1]
print(s)


