import sys
import math


def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры

    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента

    Returns:
        float: Коэффициент квадратного уравнения
    '''
    while True:
            try:
                # Пробуем прочитать коэффициент из командной строки
                coef_str = sys.argv[index]
            except:
                # Вводим с клавиатуры
                print(prompt)
                coef_str = input()
            # Переводим строку в действительное число
            try:
                coef = float(coef_str)
            except ValueError:
                print("Некорректный ввод. Попробуйте ещё раз.")
                continue
            else:
                break
    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения

    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C

    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        result.append(root1)
        result.append(root2)
    return result


def get_real_roots(result):
    real_result = []
    for root in result:
        if root > 0:
            real_result.append(math.sqrt(root))
            real_result.append(-math.sqrt(root))
        elif root == 0:
            real_result.append(abs(root))
    return real_result


def solve_biquadrate_equation(a, b, c):
    roots = get_roots(a, b, c)
    real_roots = get_real_roots(roots)
    return real_roots


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    real_roots = solve_biquadrate_equation(a, b, c)
    # Вывод корней
    len_roots = len(real_roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(real_roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(real_roots[0], real_roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {} и {}'.format(real_roots[0], real_roots[1], real_roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {} и {}'.format(real_roots[0], real_roots[1], real_roots[2], real_roots[3]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Примеры запуска
# roots_proc.py 1 0 10 (Нет корней)
# roots_proc.py 1 0 -4 (Два корня)
# roots_proc.py -4 16 0 (Три корня)
# roots_proc.py 1 -13 36 (Четыре корня)
