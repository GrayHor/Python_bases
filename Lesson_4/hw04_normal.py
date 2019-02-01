# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.



'''
Без re
str = "mtMmEZUOmcq"
itogstr = ""
for el in str:
    if el.islower():
        itogstr = itogstr + el
    else:
        print(itogstr)
        itogstr = ""
print(itogstr)
'''
'''
import re
str = "mtMmEZUOmcq" 
print(re.findall((r'[a-z]+'),str))

'''

# Задание-2:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.


import random,re

my_file=open("Number.txt",'w')
rez = ''

for _ in range(2500):
    a = str(random.randint(0,9))
    rez = rez + a


my_file.write(rez)

pattern = '[0]{2,}|[1]{2,}|[2]{2,}|[3]{2,}|[4]{2,}|[5]{2,}|[6]{2,}|[7]{2,}|[8]{2,}|[9]{2,}'
a = re.findall(pattern, rez)
maxlen = 1
maxel = ""
for el in a:
    if len(el)>maxlen:
        maxel = el
        maxlen +=1

maxonly = []
for el in a:
    if len(el) == maxlen:
        new = maxonly.append(el)

print("Максимальная(ые) последовательность(и)",set(maxonly))

my_file.close