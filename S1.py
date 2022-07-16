# t1
# a = int(input('Введите число а = '))
# b = int(input('Введите число b = '))

# if b == a * a:
#     print(f'{a}, {b} -> да')
# elif a == b * b:
#     print(f'{b}, {a} -> да')
# else:
#     print (f'{a}, {b} -> нет')

# t2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# maxx = 0
# for i in range(5):
#     x = int(input('--> '))
#     if i == 0:
#         maxx = x
#     elif x > maxx:
#         maxx = x

# print(maxx)

# my_list = []

# for i in range(5):
#     x = int(input('--> '))

    # my_list.append(x) добавить в список х
    # my_list.pop(1) удалить по индексу
# print(my_list)
# my_list.remove(6) удалить по числу
# print(my_list)
# my_list = [6, 5, 2, 6]

# while 6 in my_list: проверяет по числу
#     my_list.remove(6)

# print(my_list)

# my_list = [5, 2, 9, 1, 3]
# i = 1
# maxx = my_list[0]
# while i < len(my_list):
#     if my_list[i] > maxx:
#         maxx = my_list[i]
#     i += 1 (i + 1)

# print(maxx)
# break прерывает цикл
# continue пробегает по циклу и заканчивает

# t3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
    
#     *Примеры:* 
# n = int(input('Введите число x = ')) решение через вайл
# a = -n
# while a < n + 1:
#     print(a, end = ' ')
#     a += 1

    
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
# n = int(input('Введите число N: '))
# for i in range (-n,n + 1):
#     print(i, end= '/') 
    # end ( вид вывода( ' ' через пробел)) /n

 # t4. Напишите программу, которая будет принимать на вход дробь и показывать 
# первую цифру дробной части числа.
    
#     *Примеры:*
    
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3
# x = float(input('-> '))
# x *= 10
# x = int(x)
# print(x % 10)

# a = '6,78'

# for i in range(len(a)): задает строки в индексы
#     if a[i] == ',':
#         print(a[i + 1])



   # 3. Напишите программу, которая принимает на вход число и проверяет, 
# кратно ли оно (5 и 10) или (15, но не 30).

# int(67,8) --> 67

# x = int(input('--> '))
# if ((x % 5 == 0 and x % 10 == 0) or (x % 15 == 0 or x % 30 != 0)):
#     print('yes')


# ¬ - not
# ⋁ - or
# ⋀ - and











