# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib_array = [1,1]

    i = 2
    f_i = lambda array, i,: array[i-1] + array[i-2]
    while i != m:
        fib_array.append(f_i(fib_array,i))
        i += 1

    return fib_array[n:m]

n = int(input("n = "))
m = int(input("m = "))

print(fibonacci(n,m))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    
    repeat = True
    
    while repeat:
        repeat = False
        i = 0
        while i < len(origin_list)-1:
            if origin_list[i] > origin_list[i+1]:
                a = origin_list[i]
                origin_list[i] =  origin_list[i+1]
                origin_list[i+1] = a
                repeat = True
            i += 1


l = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
print(l)
sort_to_max(l)
print(l)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def myFilter(func,array):
    l = []

    for i in array:
        if func(i):
            l.append(i)

    return l

c = [1, 10, 14, 5 , 100, 4, 33]
f = lambda  x: x >= 10
a = myFilter(f, c)

print(a)


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def getPoints():
    p = []

    for i in range(1,5):
        l = []
        l.append(int(input("x{0} = ".format(i))))
        l.append(int(input("y{0} = ".format(i))))
        p.append(l)

    return p

points = getPoints()

sx = lambda l, n, i, j: (l[i][n] + l[j][n]) / 2

s1 = sx(points,0,0,2)
s2 = sx(points,0,1,3)

s3 = sx(points,1,0,2)
s4 = sx(points,1,1,3)

if abs(s1 - s2) == abs(s3 - s4):
    print("это параллелипипед")
else:
    print("это не параллелипипед")


