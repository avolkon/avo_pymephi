def triangle_type(a, b, c):
    # Проверка условия существования треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        return "Треугольник с такими сторонами построить невозможно"
    # Проверка типа треугольника
    if a == b == c:
        return "Треугольник равносторонний"
    elif a == b or b == c or a == c:
        return "Треугольник равнобедренный"
    else:
        return "Треугольник разносторонний"

MAX_ATTEMPTS = 5
step = 0

while step < MAX_ATTEMPTS:
    try:
        trian1 = int(input("Введите длину стороны 1: "))
        trian2 = int(input("Введите длину стороны 2: "))
        trian3 = int(input("Введите длину стороны 3: "))
        result = triangle_type(trian1, trian2, trian3)
        if result == "Треугольник с такими сторонами построить невозможно":
            print(result)
            attempts += 1
            print("Попробуйте ввести длины сторон заново.")
        else:
            print(result)
            break
    except ValueError:
        print("Ошибка ввода. Введите целые числа.")
        attempts += 1

if step == MAX_ATTEMPTS:
    print("Превышено максимальное количество попыток.")
