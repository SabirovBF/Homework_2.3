
my1_list = [1, 2, 2, 3, 5, 4, 5]
print("До изменения:",my1_list)
i = 0
while i < len(my1_list):
    j = i + 1
    while j < len(my1_list):
        if my1_list[i] == my1_list[j]:
            del my1_list[j]
        else:
            j += 1
    i += 1

print("Список через while",sorted(my1_list))

my2_list = [1, 2, 2, 3, 3, 4, 5]
print("До изменения:",my2_list)
for i in range(len(my2_list)):
    for j in range(i + 1, len(my2_list)):
        if my2_list[i] == my2_list[j]:
            my2_list.pop(j)
            break

print("Список через for", sorted(my2_list))

