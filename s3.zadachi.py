# 1. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

# '12' -> ['asd12', '12', 'asd', '87'] -> 'asd12', '12'

# my_list = ['asd12', '12', 'asd', '87']
# for i in my_list:
#     if '12' in i:
#         print(i)


# 2. Напишите программу, которая определит позицию второго 
# вхождения строки в списке либо сообщит, что её нет.
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# count = 0
# my_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу", "йцу", "йцу"]
# for i in range(len(my_list)):
#     if my_list[i] == 'йцу':
#         count += 1

#         if count > 1:
#             print(i)
#             break

# 3. Реализуйте алгоритм задания случайных чисел без использования 
# встроенного генератора псевдослучайных чисел.


my_set = set()
for i in range(100):
    my_set.add(str(i))

for e in my_set:
    print(int(e))
    