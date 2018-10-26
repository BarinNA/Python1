import module_easy

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


triangle = module_easy.triangle("-5,2","7,-7","5,7")

print("Square = {}".format(triangle.getsquare()))
print("Perimetr = {}".format(triangle.getperimetr()))
print("hight = {}".format(triangle.gethight()))

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

trapezium = module_easy.Trapezium("1,1","2,4","5,4","6,1")
print(trapezium.check())
print(trapezium.sideslength())
print(trapezium.perimetr())
print(trapezium.square())