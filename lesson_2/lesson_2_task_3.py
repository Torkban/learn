import math

def square(a):
    if a >= 0:
        return math.ceil(a**2)
    else:
        return "Некорректное число"

n = float(input("Введите длину стороны квадрата: "))

square_area = square(n)

print("Площадь квадрата: " + str(square_area))

