# динамическое
def F(n):
    if n in (1, 2):
        return n
    a = [None] * (n + 1)
    a[0] = 0
    a[1] = 1
    a[2] = 2
    for i in range(3, n + 1):
        a[i] = i * (i - 1) + a[i - 1] + a[i - 2]
    return a[n]


print(F(2023) - F(2021) - 2 * F(2020) - F(2019))

# списками
f = [0] * 2500
for n in range(2500):
    if n == 1:
        f[n] = 1
    if n == 2:
        f[n] = 2
    if n > 2:
        f[n] = n * (n - 1) + f[n - 1] + f[n - 2]

print(f[2023] - f[2021] - 2 * f[2020] - f[2019])
