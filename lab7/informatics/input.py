a = int(input())
b = int(input())
print((a**2+b**2)**0.5)

n = int(input())
print(f'The next number for the number {n} is {n + 1}.')
print(f'The previous number for the number {n} is {n - 1}.')

n = int(input())
k = int(input())
print(k // n)

n = int(input())
k = int(input())
print(k % n)

v = int(input())
t = int(input())
print(((v * t)) % 109)

n = int(input())
print(n % 10)

n = int(input())
print(n // 10)

n = int(input())
print((n % 100) // 10)

n = int(input())
print(n // 100 + (n % 100) // 10 + n % 10)

n = int(input())
print((n // 2) * 2 + 2)

n = int(input())
print((n // 60) % 24, n % 60)

n = int(input())
h = (n // 3600) % 24
m = (n % 3600) // 60
s = n % 60
if m < 10:
    print(f'{h}:0{m}', end=":")
else:
    print(f'{h}:{m}', end=":")
if s < 10:
    print(f'0{s}')
else:
    print(s)

a = input()
b = input()
a, b = b, a
print(a, b)

n = int(input())
t = n * 45 + (n // 2) * 5 + (n - n // 2 - 1) * 15
print(9 + t // 60, t % 60)

a = int(input())
b = int(input())
n = int(input())
print(a * n + (b * n) // 100, (b * n) % 100)

h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
print((h2 - h1) * 3600 + (m2 - m1) * 60 + s2 - s1)

n = int(input())
m = int(input())
print(-(-m // n))

n = int(input())
k = int(input())