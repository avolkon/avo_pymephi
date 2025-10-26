def decimal_to_binary(num):

    # Проверка типа: если не int, выбрасываем TypeError
    if not isinstance(num, int):
        raise TypeError("Введите целое число.")
    # Проверка на отрицательное число
    if num < 0:
        raise ValueError("Доступны только неотрицательные числа.")
    # Специальный случай для 0
    if num == 0:
        return "0"
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    return binary

MAX_ATTEMPTS = 10
step = 0

while step < MAX_ATTEMPTS:
    try:
        num = int(input('Введите число: '))
        print(f"Число {num} в двоичном счислении = {decimal_to_binary(num)}")
        break
    except (ValueError, TypeError) as e:
        print(f"Ошибка: {e}. Попробуйте снова.")
        step += 1

if step == MAX_ATTEMPTS:
    print("Превышено максимальное количество попыток.")

# Напишите функцию decimal_to_binary(num), которая преобразует число из десятичной системы счисления в двоичную.
# Входные данные:
# - num: целое неотрицательное число (int)
# Выходные данные:
# - str: строка, содержащая двоичное представление числа num
# Примеры использования:
# - decimal_to_binary(10) → "1010"
# - decimal_to_binary(0) → "0"
# - decimal_to_binary(1) → "1"
# - decimal_to_binary(255) → "11111111"
# Исключения и особые случаи:
# - Если num < 0, выбрасывается ValueError: "Only non-negative integers are allowed."
# - Если num не является int, выбрасывается TypeError: "Input must be an integer."
# Ограничения:
# - Только неотрицательные целые числа
# - Нельзя использовать встроенную функцию bin()
# - Разрешается использовать только базовые арифметические операции: деление, остаток, целочисленное деление
# Требования к реализации:
# - Должна использовать цикл и арифметику (%, //) для построения строки
# - Запрещается использовать внешние библиотеки