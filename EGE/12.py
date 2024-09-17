for n in range(3, 10000 + 1):
    s = '4' + '1' * n

    while "31" in s or "411" in s or "1111" in s:
        s = s.replace("31", "1", 1)
        s = s.replace("411", "13", 1)
        s = s.replace("1111", "4", 1)

    y = 0
    for i in range(len(s)):
        y += int(s[i])
    if y == 34:
        print(n)
        break

# while ('>1' in s) or ('>2' in s) or ('>3' in s):
#     if ">1" in s:
#         s = s.replace(">1" , "22>" , 1)
#     if ">2" in s:
#         s = s.replace(">2" , "2>" , 1)
#     if ">3" in s:
#         s = s.replace(">3" , "1>" , 1)

# print (s)
