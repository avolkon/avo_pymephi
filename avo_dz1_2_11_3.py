import math

def factorial(number):
    if number < 0:
        return None
    
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)

number = int(input("Введите число: "))
result = factorial(number)

if result == None:
    print ('Факториал отрицательных чисел не существует.')
else:
    print(f'Факториал числа {number} = {result}')

# Ниже приведен код, который должен вычислять факториал числа.
# # Однако он содержит ошибки в стиле (нарушение PEP 8) и логике.
# Исправьте его, чтобы он корректно работал и соответствовал стандартам PEP8.
# Программа должна запрашивать число и выводить его факториал.
# Если число отрицательное то выводить "Факториал отрицательного числа не существует", иначе "Факториал равен: "

# import math

# def FACTORIAL(Number):
#     if Number==0:
#         print 1
#     else:
#     return Number*Factorial(Number-1)

# n=input("Введите число:")
# print(FACTORIAL(n))