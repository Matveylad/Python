# import os
# print(os.sep())
# print(f.read(3)) распечатка



#  r - чтение
# W - запись
# a - 

# r - чтение
# w - запись
# a - дозапись


# file_path = r'folder\file.txt'
# with open(file_path, 'w') as f:
#     f.read('123\n')

# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

# file_path = r'hello python\file.txt'
# with open(file_path,'r') as f:
#         mystr = f.read()
# print(mystr)
# mystr = mystr.split()

# print(mystr)
# for i in range(len(mystr)):
#     mystr[i] = int(mystr[i])
# print(mystr)
# print(max(mystr))
# print(min(mystr))

# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами: D=b^2-4ac

# path = r'hello python\file.txt'
# with open(path, 'r') as my_file:
#     data = my_file.read()
# data = data.split()
# print(data)
# data = data[:-2]
# print(data)
# data = [int(data[0][:-3]), int((data[1] + data[2])[:-1]), int(data[3] + data[4])]
# print(data)
# # D=b^2-4ac
# d = data[1]**2 - 4 * data[0] * data[2]
# print(d)
# # x=((-b+(d^(1/2)))/(2*a))
# x_1 = (-data[1] + d**0.5) / (2 * data[0])
# x_2 = (-data[1] - d**0.5) / (2 * data[0])
# print(x_1, x_2)

# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

