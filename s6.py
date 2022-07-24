# def dlb(lst: list) -> list:
#     count_dbl = (len(lst) + 1) // 2
#     res_list = [lst[i] * lst[-i - 1] for i in range(count_dbl)]
#     return res_list


# list_1 = [[2, 3, 4, 5], [2, 3, 4, 5, 6]]
# print(list(map(dlb, list_1)))

# 1) Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# my_list2 = []
# for item in (my_list):
#     if my_list.count(item) == 1:
#         my_list2.append(item)
# print(my_list2)

my_list = [1, 2, 3, 5, 1, 5, 3, 10]
res = []
for item in my_list:
    if my_list.count(item) == 1:
        res.append(item)
print(res)


res = [item for item in my_list if (my_list.count(item) == 1)]
print(res)

f = lambda item: my_list.count(item) == 1
res = list(filter(f, my_list))
print(res)

