# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# my_list = [word for word in my_list.split() if 'абв' not in word]
# list(filter([item for item in (my_list) if my_list.count==1]))

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# res = []
# for item in my_list:
#     if my_list.count(item) == 1:
#         res.append(item)
# print(res)

# # вариант решения через включения
# res = [item for item in my_list if (my_list.count(item) == 1)]
# print(res)
# # через lambda
# f = lambda item: my_list.count(item) == 1
# res = list(filter(f, my_list))
# print(res)

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
# from ast import Break

candy = 2021

while candy > 0:
    player1 = int(input(' 1 игрок:  '))
    if 0 < player1 <= 28:
        candy = candy-player1
        print(candy)
        if candy <= 0:
            print(' 1 Player WIN!!!')
            break
    else:
        player1 = int(input(' 1 игрок:  '))

    player2 = int(input(' 2 игрок :  '))
    if 0 < player2 <= 28:
        candy = candy-player2
        print(candy)
        if candy <= 0:
            print(' 2 Player WIN!!!')
    else:
        player2 = int(input(' 2 игрок:  '))
        candy = candy-player2
