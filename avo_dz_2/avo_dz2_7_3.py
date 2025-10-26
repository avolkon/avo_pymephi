import string

# Создаю словарь: буква -> порядковый номер
abc_dict = {letter: index for index, letter in enumerate(string.ascii_lowercase, start=1)}

# Функция подсчёта суммы индексов букв в слове
def how_many_times(message):
    message = message.lower()  # для унификации регистра
    total = 0
    for letter in message:
        if letter == ' ':
          continue  # пропустить пробел
        elif letter in abc_dict:
            total += abc_dict[letter]
        else:
            # если символ не в словаре, можно игнорировать или обработать иначе
            pass
    return total

message = str(input('Введите сообщение латинскими буквами:'))
print(f"Для написания '{message}' нажми кнопку , {how_many_times(message)} раз")

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