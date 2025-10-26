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