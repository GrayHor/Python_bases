# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

'''
fib = [1,1]
n = int(input())
m = int(input())

def ffib(m):
    i = 1
    while i <= m:
        l = len(fib)
        fib.append(fib[l-2] + fib[l - 1])
        i += 1
    return fib[n-1:m]

rez = ffib(m)
print(rez)

'''

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

'''
my_list = [7,2,56,6,3,25]
ln = len(my_list)
print(ln)
i = 0


while i < ln-1:
    if my_list[i] > my_list[i+1]:
        temp = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1]=temp
    else:
        my_list = my_list
        print(my_list)
        i+=1
'''



#Задача-3:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
import math

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
x4 = int(input())
y4 = int(input())

A1A2 = math.sqrt((x1-x2)**2 + (y1-y2)**2)
A2A3 = math.sqrt((x2-x3)**2 + (y2-y3)**2)
A3A4 = math.sqrt((x3-x4)**2 + (y3-y4)**2)
A4A1 = math.sqrt((x4-x1)**2 + (y4-y1)**2)


if A1A2 == A3A4 and A2A3 == A4A1:
    print("Это параллелограмм")
else:
    print("Не параллелограмм")




