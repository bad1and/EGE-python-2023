# def f(a, b):
#     if a > b + 1:
#         return 0
#     if a == b:
#         return 1
#     if a < b:
#         return f(a + 3, b) + f(a - 1, b) + f(a * 2, b)
#
#
# print(f(4, 14))

def f(a, b, last):
    if a > b + 1:
        return 0
    if a == b:
        return 1
    if last == 'a':
        return f(a + 3, b, 'b') + f(a * 2, b, 'c')
    else:
        return f(a - 1, b, 'a') + f(a + 3, b, 'b') + f(a * 2, b, 'c')

print(f(4, 14, '.'))

# def f(a, b):
#     if a < b:
#         return 0
#     if a == b:
#         return 1
#     if a > b:
#         return f(a  - 2, b) + f(a - 3, b) + f(a // 3, b)
#
# print(f(20, 3))


# def f(a, b):
#     if a > b:
#         return 0
#     if a == b:
#         return 1
#     if a < b:
#         if a == 9 or (a // 100) == 9:
#             return f(a + 1, b)
#         if 9 < a < 99:
#             return f(a + 1, b) + f(a + 10, b)
#         if 99 < a < 1000:
#             return f(a + 1, b) + f(a + 100, b)
#
# print(f(35, 57))
