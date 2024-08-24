a = [100, 96, 87, 1000, 95]

print(a[0])

print(a[0:5])#a[n:m] = a의 n번째 요소부터 M-1번째 요소까지 나열
print(a[4:5])
print(a[:3])#처음부터 m까지
print(a[2:])#n부터 끝까지

b = [[100, 45, 49, 38, 76], [376, 23, 78, 13, 144], [24, 79, 354, 24, 96]]

print(b[0])
print(b[0][4])
print(b[0][2:])
print(b[:2])

c = [1, 2, 3, 4, 5]
d = c

d[1] = 10

print(c)
print(d)

e = a + c

print(e)

f= a * 3
print(f)

print(len(a))
print(len(b))
print(len(b[0]))
