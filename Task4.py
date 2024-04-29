number = [16, 46, 26, 36, 4, 5, 6]
b = 1
for i in enumerate(number):
    if b % 3 == 0:
        print(i)
    b += 1