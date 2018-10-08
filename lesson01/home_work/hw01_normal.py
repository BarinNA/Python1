
__author__ = 'Носков А.А.'

import math

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.
print("Задача 1")
x = int(input())
m = 0 

while x != 0:
    a = x % 10
    if m < a:
        m = a
    x = x // 10
print(m)        

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

print("Задача 2")
a,b = int(input("a = ")),int(input("b = "))

A = 0
while a != 0:
    A = A*10 + a % 10
    a = a // 10

B = 0
while b != 0:
    B = B*10 + b % 10
    b = b // 10
print("a = ", A,"\n","b = ", B)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

print("Задача 3")
a,b,c = int(input("a = ")),int(input("b = ")),int(input("c = "))

d = b**2 - 4*a*c

x1 = (-b + math.sqrt(d))/2*a
x2 = (-b - math.sqrt(d))/2*a

print("x1 = ", x1, "\n", "x2 = ", x2)

