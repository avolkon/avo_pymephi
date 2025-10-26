def bin_kef(num, kef):
    # Проверка типов
    if not isinstance(num, int) or not isinstance(kef, int):
        raise TypeError("Введите целое число.")
    # Проверка валидности значений
    if num < 0 or kef < 0 or kef > num:
        raise ValueError('''Ошибка ввода,
        введите значения с учетом условия 0 ≤ kef ≤ num''')
    # Используем симметрию коэффициента C(n, k) = C(n, n-k)
    if kef > num - kef:
        kef = num - kef
    result = 1
    # Вычисляем биномиальный коэффициент без факториалов
    for i in range(1, kef + 1):
        result = result * (num - i + 1) // i
    return result

MAX_ATTEMPTS = 10
step = 0

while step < MAX_ATTEMPTS:
    try:
        num = int(input('Введите общее число элементов (n): '))
        kef = int(input('''Введите число, по сколько элементов
        будем подбирать сочетание (k)
        (число сочетаний из n по k) : '''))
        print(f'Число сочетаний из {num} по {kef} = {bin_kef(num, kef)}')
        break
    except (ValueError, TypeError) as e:
        print(f"Ошибка: {e}. Попробуйте снова.")
        step += 1

if step == MAX_ATTEMPTS:
    print("Превышено максимальное количество попыток.")

    
# Напишите функцию bin_kef(num, kef), которая вычисляет число сочетаний из num по kef (биномиальный коэффициент).
# Входные данные:
# - num: целое неотрицательное число n
# - kef: целое неотрицательное число k
# Выходные данные:
# - int: одно целое число — результат вычисления
# Примеры использования:
# - bin_kef(5, 2) → 10
# - bin_kef(6, 3) → 20
# - bin_kef(10, 0) → 1
# - bin_kef(10, 10) → 1
# Исключения и особые случаи:
# - Если num или kef не являются целыми числами → TypeError: "Arguments must be integers."
# - Если num < 0 или kef < 0 или kef > num → ValueError: "Invalid values: require 0 ≤ kef ≤ num"
# Ограничения:
# - 0 ≤ kef ≤ num ≤ 1000
# Требования к реализации:
# - Не использовать факториалы напрямую (чтобы избежать переполнения)
# - Оптимизировать через симметрию