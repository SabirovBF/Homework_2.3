n = int(input("Введите число:"))
a = n
b = 0
while n > 0:
    b += 1
    n = n // 10
print("Количество цифр в коде с while равно:", b)

c = 0

for i in str(a):
    if i.isdigit():
        c += 1
print("Количество цифр в коде с for равно:", c)