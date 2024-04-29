n = int(input('Введите число n: '))
s = 0
s1 = 0
a = 0
for i in range(n+1):
    if i % 2 == 0:
        s += i
print('Сумма четных чисел(1 способ):', s)

while a <= n:
    if a % 2 == 0:
        s1 += a
    a += 1
print('Сумма четных чисел(2 способ):', s)
