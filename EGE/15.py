for A in range (1000):
    m = 1
    for x in range (1000):
        if (x & 21074 != 0 <= (x & 12369 == 0 <= x & A != 0)):
            m = 0
            break
    if m == 1:
        print(A)



for A in range(10000):
    m = 1
    for x in range(400):
        for y in range(400):
            if ((2 * y > 5 * x) or (x * y < A) or (x >= 22))==0:
                m = 0
                break
    if m == 1:
        print (A)
        break

# k = 0
# for A in range(400):
#     m = 1
#     for x in range(400):
#         for y in range(300):
#             if (x + 2 * y < A) or (y > x) or (x > 20):
#                 m = 0
#                 break
#         if m == 0:
#             break
#     if m == 1:
#         k +=1
#         print (A)
#
# for A in range(400):
#     k = 1
#     for x in range(400):
#         if (((x % 3) <= (not(x % 5))) or (x + A >= 90)) == 0:
#             k = 0
#             break
#     if k == 1:
#         print(A)

# for A in range(0, 1000):
#     k = 0
#     for x in range(0, 1000):
#         if ((x & 39 == 0) or ((x & 11 == 0) <= (x & A != 0))):
#             k += 1
#     if k == 1000:
#         print(A)
#         break
