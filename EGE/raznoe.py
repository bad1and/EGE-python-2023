def summ(n):
    sumi = 0
    while n > 0:
        sumi += n % 10
        n = n // 10
    return sumi


k = 0
for n in range(2123456789):

    r = bin(n)[2:]
    r = str(r)

    if summ(int(r, 2)) % 2 != 0:
        r = r + '1'
    else:
        r = r + '0'

    if summ(int(r, 2)) % 2 != 0:
        r = r + '1'
    else:
        r = r + '0'

    if summ(int(r, 2)) % 2 != 0:
        r = r + '1'
    else:
        r = r + '0'

    r = int(r, 2)
    if 987654321 <= r <= 2123456789:
        k += 1
        print(k)
141975308