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