def tribonacci(n):
    # Проверка типа
    if not isinstance(n, int):
        raise TypeError("Введите целое число: ")
    # Проверка на отрицательное
    if n < 0:
        raise ValueError("Число не должно быть отрицательным, запустите программу заново и повторите ввод: ")
    # Начальные три числа ряда Трибоначчи
    if n == 0 or n == 1 or n == 2:
        return 1
    # Переменные для трех последних чисел
    t0, t1, t2 = 1, 1, 1
    # Итеративное вычисление без хранения всего ряда
    for n in range(3, n + 1):
        t_next = t0 + t1 + t2
        t0, t1, t2 = t1, t2, t_next
    return t2

MAX_ATTEMPTS = 30
attempt = 0

while attempt < MAX_ATTEMPTS:
    try:
        n = int(input("Введите целое неотрицательное число: "))
        if n < 0:
            print("Число не должно быть отрицательным, повторите ввод: ")
            attempt += 1
            continue
        result = tribonacci(n)
        print(f"{n}-е число Трибоначчи: {result}")
        break
    except (ValueError, TypeError) as e:
        print(e)
        attempt += 1

if attempt == MAX_ATTEMPTS:
    print("Превышено максимальное число попыток ввода.")
