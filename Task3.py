number = int(input('Введите число: '))
f, s = 1, 1
while number > 1:
    f = f * number
    number = number - 1
    print('Шаг %s:' %(s), f)
    s += 1