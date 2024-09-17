x = 5*(343**8) + 4*(49**12) + 7**14 - 98
s = ''
while x > 0:
    s = str(x%7) + s
    x = x // 7
print (set(s)) #к-во уникальных значений
print (s.count('2'))
print (s.count('5'))
print (s.count('0'))
print (s.count('1'))
print (s.count('6'))