def armstr(num):
    if not isinstance(num, int):
        raise TypeError("Введите целое число")
    if num < 0:
        raise ValueError("Значение не должно быть отрицательным")
    if num == 0:
        return None  # Пустой вывод

    def count_digits(num):
        count = 0
        while num > 0:
            num //= 10
            count += 1
        return count

    def is_armstr(num):
        n = count_digits(num)
        temp = num
        total = 0
        while temp > 0:
            digit = temp % 10
            power = 1
            for _ in range(n):
                power *= digit
            total += power
            temp //= 10
        return total == num

    for number in range(1, num + 1):
        if is_armstr(number):
            print(number)

MAX_ATTEMPTS = 5
attempts = 0

while attempts < MAX_ATTEMPTS:
    try:
        num = int(input("Введите целое число: "))
        armstr(num)
        break
    except (ValueError, TypeError) as e:
        print(f"Ошибка: {e}. Попробуйте снова.")
        attempts += 1

if attempts == MAX_ATTEMPTS:
    print("Превышено максимальное количество попыток ввода.")


# Напишите функцию armstr(num), которая находит все числа Армстронга в диапазоне от 1 до num.
# Число Армстронга — это число, равное сумме своих цифр, возведенных в степень, равную количеству цифр этого числа.
# Входные данные:
# - num: целое неотрицательное число
# Выходные данные:
# - None: функция печатает числа Армстронга в консоль
# Примеры использования:
# - armstr(1000) → печатает: 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407
# - armstr(10) → печатает: 1, 2, 3, 4, 5, 6, 7, 8, 9
# - armstr(200) → печатает: 1, 2, 3, 4, 5, 6, 7, 8, 9, 153
# Исключения и особые случаи:
# - Если num == 0, вывод пустой (None) (ничего не печатается)
# - Если num < 0 → выбросить ValueError: "Input must be non-negative"
# - Если num не int → выбросить TypeError: "Input must be an integer"
# Ограничения:
# - Не использовать строки, списки, append, join, map, list
# Требования к реализации:
# - Разбивать число на цифры только через деление на 10 (// 10) и остаток (% 10)
# - Считать количество цифр с помощью while
# - Возводить каждую цифру в степень количества цифр
