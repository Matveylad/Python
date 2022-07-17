# import os
# print(os.sep())
# print(f.read(3)) распечатка



#  r - чтение
# W - запись
# a - 

file_path = r'folder\file.txt'
with open(file_path, 'a') as f:
f.write('123\n')
