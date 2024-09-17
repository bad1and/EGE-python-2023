print(2**13//4)
B = '1' * 340 + '2' * 849 + '3' * 151
for x in range(100000):
    s = '0' + '2' * x + '0'
    while '00' not in s:
        s = s.replace('033', '1302', 1)
        s = s.replace('03', '120', 1)
        s = s.replace('023', '203', 1)
        s = s.replace('02', '20', 1)
    if s.count('1') == 340 and s.count('2') == 849 and s.count('3') == 151:
        print(x)
