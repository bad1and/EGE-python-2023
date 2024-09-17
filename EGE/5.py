for n in range(0 , 1000):
    r = bin(n)[2:]
    r = r.replace('0' , '00')
    r = r.replace('1' , '11')
    r = int(r , 2)
    if r >63:
        print(r)


# def CALL(n) -> str:
#     c = ''
#     while n:
#         c += str(n % 4)
#         n //= 4
#     return c[::-1]
#
#
# def F(N) -> int:
#     n = CALL(N)
#     if N % 4 == 0:
#         n += n[-2:]
#     else:
#         n += CALL((N % 4) * 2)
#     return int(n, 4)
#
#
# for i in range(1, 1000):
#     if F(i) >= 1088:
#         print(i)
#         break

# for n in range(13, 14):
#     r = bin(n)[2:]
#     r = str(r)
#
#     a = int(n) % 4
#     a = bin(a)[2:]
#     a = str(a)
#     r = r + a
#
#     r = int(r, 2)
#     print(r)
#
# res = []
# for N in range(1000):
#     n = bin(N)[2:]
#     n += bin(N % 4)[2:]
#     res.append(int(n, 2))
# b=[0]*10000
# for i in res:
#     b[i]=1
# m=max(sum(b[i:i+49]) for i in range(len(b)-49))
# print(m)

# for x in range (41, 53):
#     print (x, bin(x)[2:])
# print ()
# print (int('11111',2))
# print (6 % 4)


# r = int(r, 2)
# print(r)

# a=[]
# for N in range(10,1001):
#     n=bin(N)[2:]
#     n=n.replace('1','0',1)
#     K=int(n,2)
#     a.append(N-K)
# print(len(set(a)))


# sum = r.count('1')
# r += str(sum % 2)

# def summ(n):
#     sumi = 0
#     while n > 0:
#         sumi += n % 10
#         n = n // 10
#     return sumi
#
#
# k = 0
# for n in range(????):
#
#     r = bin(n)[2:]
#     r = str(r)
#
#     if summ(int(r, 2)) % 2 != 0:
#         r = r + '1'
#     else:
#         r = r + '0'
#
#     if summ(int(r, 2)) % 2 != 0:
#         r = r + '1'
#     else:
#         r = r + '0'
#
#     if summ(int(r, 2)) % 2 != 0:
#         r = r + '1'
#     else:
#         r = r + '0'
#
#     r = int(r, 2)
#     if 987654321 <= r <= 2123456789:
#         k += 1
#         print(k)

# k = 0
# kch = 0
# knch = 0
# for n in range(123455,987654321+1):
#     r = bin(n)[2:]
#     r = str(r)
#
#     if n%2==0:
#         kch+=1
#     else:
#         knch +=1
#
#
#     if kch>knch:
#         r = r + "1"
#     elif knch<kch:
#         r = r + "0"
#     elif knch==kch and n%2 == 0:
#         r = r + "0"
#     elif knch==kch and n%2 != 0:
#         r = r + "1"
#
#     if kch>knch:
#         r = r + "1"
#     elif knch<kch:
#         r = r + "0"
#     elif knch==kch and n%2 == 0:
#         r = r + "0"
#     elif knch==kch and n%2 != 0:
#         r = r + "1"
#
#     if kch>knch:
#         r = r + "1"
#     elif knch<kch:
#         r = r + "0"
#     elif knch==kch and n%2 == 0:
#         r = r + "0"
#     elif knch==kch and n%2 != 0:
#         r = r + "1"
#
#     r = int(r, 2)
#     if():
#         k+=1
# print(k)


# for n in range(100):
#     i = n
#     s = ''
#     while i > 0:
#         s += (str(i % 3))
#         i //= 3
#     s = s[::-1]
#     if s % 3 == 0:
#         s = s + s[-2] + s[-1]
#     else:
#         s = s + (s//3 * 5)
