a = ['Самое', 'длинное', 'слово', 'в', 'тексте']
b = len(a)
c, d, c1, d1 = 0, 0, 0, 0
Name = float()
Ame = float()
while c < b:
    if d <= len(a[c]):
        d = len(a[c])
        Name = a[c]
        print(len(a[c]))
    c += 1
print('(1способ)Самое длинное слово:', Name)

for i in range(1, b+1):
    if d1 <= len(a[c1]):
        d1 = len(a[c1])
        Ame = a[c1]
    c1 += 1
print('(2способ)Самое длинное слово:', Ame)