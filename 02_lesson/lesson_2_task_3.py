import math

def square(length):
    area = math.ceil(length) ** 2
    return area
length_side = float(input("Введите длинну стороны квадрата: "))
print(square(length_side))
