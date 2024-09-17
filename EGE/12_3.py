# for x in range(70):
#     for y in range(70):
#         for z in range(70):
#             s = '0' + '1' * x + '2' * y + '3' * z + "0"
#             while '00' not in s:
#                 s = s.replace('01', '210', 1)
#                 s = s.replace('02', '320', 1)
#                 s = s.replace('03', '3012', 1)
#             if s.count('1') == 26 and s.count('2') == 54 and s.count('3') == 48:
#                 print(x + y + z)
s = '1234'
k = 0
for i in range(len(s)):
    k += int(s[i])
print(k)
