f = 0
g = 10101010010100101
t = 0
y = 0

for i in range(4735, 8757):
    if i % 5 == 0 and i % 17 == 0 and i % 7 != 0 and i % 14 != 0 and ((i % 100) // 10) >= (i % 1000) / 100:
        y += 1
        t += i
        if (i > f):
            f = i
        if (i < g):
            g = i
# print (t)
# print (y)
print((t // y), f, g)
print((t // y) + f + g)
