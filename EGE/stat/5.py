k = 0
for n in range(0, 500000000):
    r = bin(n)[2:]

    r = r + (bin(n % 4)[2:])
    r = int(r, 2)
    if 1100000000 <= r <= 1987653210:
        k += 1
        print(k)
