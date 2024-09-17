g = 0
n = 0
f = 2048
for i in range(2048, 8193):
    if i % 7 == 0 and i % 11 != 0 and i % 23 != 0 and i % 10 != 8:
        g += 1
        if (i < f):
            f = i

for i in range(12048, 18193):
    if i % 7 == 0 and i % 11 != 0 and i % 23 != 0 and i % 10 != 8:
        g += 1
        n = i
print(g, n - f)
