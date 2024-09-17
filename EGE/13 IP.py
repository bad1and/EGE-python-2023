from ipaddress import *
for mask in range(33):
    net = ip_network(f"244.55.229.28/{mask}" , 0)
    print(net)
#
# print(bin(168)[2:])
# print(bin(160)[2:])
# 'IP 10101000'
# 'A  11100000'
# 'M  10100000'
# print(int('11100000', 2))

from ipaddress import *

k = 0
sl2 = []
sl = ['00000000', '10000000', '11000000', '11100000', '11110000', '11111000', '11111100', '11111110', '11111111']
for i in sl:
    i = int(i, 2)
    sl2.append(i)
k = 0
for A in sl2:
    net = ip_network(f'255.211.33.160/255.255.{A}.0', False)
    b = True

    for ip in net:
        x = bin(int(ip))[2:]
        x = '0' * (32 - len(x)) + x

        kl = x[:16].count('1')
        kr = x[16:].count('1')

        if kl < kr:
            b = False
    if b == True:
        print(A)
        break

from ipaddress import *

#
# for A in range(256):
#     net = ip_network(f'64.129.{A}.10/255.255.252.0', False)
#     b = True
#
#     for ip in net:
#         x = bin(int(ip))[2:]
#         x = '0' * (32 - len(x)) + x
#
#         kl = x[:16].count('1')
#         kr = x[16:].count('1')
#
#
#         if kl > kr:
#             b = False
#     if b == True:
#         print(A)
#         break
# from ipaddress import *
# net = ip_network(f'253.112.169.12/255.255.254.0', False)
# k = 0
# for ip in net:
#     x = bin(int(ip))[2:]
#     x = '0' * (32 - len(x)) + x
#
#     kl = x[:16].count('1')
#     kr = x[16:].count('1')
#     if kr >= kl:
#         k += 1
# print(k)
