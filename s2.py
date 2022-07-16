# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81
# def searchNumber(a, b):
#     my_list = [1]
#     i = 1
#     while len(my_list) < a:
#         list.append(my_list[i-1]*b)
#         i += 1
#     print(my_list)

# searchNumber(5,-3)

# def F(x):
#     s=1
#     print(s, end=' ')
#     for i in range(1,x):
#      s=s*(-3)
#      print(s, end=' ')



# n = int(input('---->'))
# F(n)

# доб информация
# def searchNumber(num=7, *args, **key): key - словарик
#     print(args)
#     print(key)


# searchNumber(5, 10, 123, 5432, 324, 76, a=1, b=2)

# 3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

# a = 'Напишите программу, в которой пользователь будет задавать две строки'
# b = 'а'
# count = 0
# index = 0
# for i in a:
#     if a[index] == b:
#         count += 1
#     index += 1
# print(count)

# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

# st1 = 'привет, мир, т, привет!'
# st2 = ','
# def str(st1, st2):
#     t = 0
#     for i in range(len(st1) - len(st2)):
#         if (st1[i : i + len(st2)] == st2):
#             t += 1
#     return t
# print(str(st1, st2))

# def find_line(string:str, under_strind:str):
#     print(string.count(under_strind))

# user_string = input('Введите текст: ')
# user_understring = input('Введите текст: ')
# find_line(user_string, user_understring)

# symbol = 'so'
# base_string = 'some pernal'
# position = 0
# qty = 0
# while(True):
#     position = base_string.find(symbol, position)
#     if position == -1:
#         break
#     else:
#         position += 1    # как вариант len(symbol)
#         qty += 1
# print(qty)

