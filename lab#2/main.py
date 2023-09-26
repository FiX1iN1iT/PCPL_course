import sys


def get_str(index, prompt):
    '''
    Читаем слово из командной строки или вводим с клавиатуры

    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента

    Returns:
        word (str): Слово
    '''

    try:
        # Пробуем прочитать слово из командной строки
        word = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        word = input()
    return word


def levenstein(str_1, str_2):
    '''
    Вычисление корней квадратного уравнения

    Args:
        str_1 (str): Первое слово
        str_2 (str): Второе слово

    Returns:
        result (int): Расстояние Левенштейна
    '''
    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)
    result = current_row[n]

    return result


def main():
    '''
    Основная функция
    '''
    a = get_str(1, 'Введите первое слово:')
    b = get_str(2, 'Введите второе слово:')
    # Вычисление расстояния Левенштейна
    print("Расстояние Левенштейна =", levenstein(a, b))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Примеры запуска
# main.py самолет самокат (2)
