for A in range(0, 400):
    m = 1
    for x in range(0, 400):
        if ((x % A) <= ((x % 6) <= (x % 4))) == 0:
            m = 0
            break
    if m == 1:
        print(A)
