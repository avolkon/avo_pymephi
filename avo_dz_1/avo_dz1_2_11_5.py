# Напишите программу для решения квадратных уравнений вида ax² + bx + c = 0. Программа должна:
# - Запрашивать коэффициенты a, b, c в формате число с плавающей точкой "Введите коэффициент {X}: "
# "" {X} заменить на соответствующий коэффициент
# - Определять тип корней (2 действительных, 1 действительный, комплексные)
# - Вычислять корни с точностью до 2 знаков после запятой
# - Использовать отдельные функции для вычисления дискриминанта и корней

import math

def calculate_discriminant(a, b, c):
    return b**2 - 4*a*c

def calculate_roots(a, b, discriminant):
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (round(x1, 2), round(x2, 2))
    elif discriminant == 0:
        x = -b / (2*a)
        return (round(x, 2), )
    else:  # Комплексные корни
        real_part = -b / (2*a)
        imag_part = math.sqrt(-discriminant) / (2*a)
        return (round(real_part, 2), round(imag_part, 2))

def main():
    a = float(input("Введите коэффициент a: "))
    b = float(input("Введите коэффициент b: "))
    c = float(input("Введите коэффициент c: "))

    discriminant = calculate_discriminant(a, b, c)

    if discriminant > 0:
        roots = calculate_roots(a, b, discriminant)
        print("Два действительных корня:")
        print(f"x1 = {roots[0]:.2f}, x2 = {roots[1]:.2f}")
    elif discriminant == 0:
        roots = calculate_roots(a, b, discriminant)
        print("Один действительный корень:")
        print(f"x = {roots[0]:.2f}")
    else:
        real, imag = calculate_roots(a, b, discriminant)
        print("Комплексные корни:")
        print(f"x1 = {real} + {imag}i")
        print(f"x2 = {real} - {imag}i")
main()