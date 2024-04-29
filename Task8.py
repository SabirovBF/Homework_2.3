my_list = ["a", "b", "c", "d", "c"]
a = len(my_list)
b = len(set(my_list))
if a == b:
    print("Дубликатов нет")
else:
    print("Дубликаты есть")