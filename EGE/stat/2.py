print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if (((x == z) <= ((not y) or w)) == (not (w <= z) or (x <= y))) == 1:
                    if z == 0:
                        print(w, x, y, z)



