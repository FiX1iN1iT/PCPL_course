# используется для сортировки
# from operator import itemgetter


class Emp:
    """Микропроцессор"""

    def __init__(self, id, name, cores, dep_id):
        self.id = id
        self.name = name
        self.cores = cores
        self.dep_id = dep_id


class Dep:
    """Компьютер"""

    def __init__(self, id, model):
        self.id = id
        self.model = model


class EmpDep:
    """
    'Микропроцессоры компьютера' для реализации
    связи многие-ко-многим
    """

    def __init__(self, dep_id, emp_id):
        self.dep_id = dep_id
        self.emp_id = emp_id


# Компьютеры
deps = [
    Dep(1, 'отдел кадров'),
    Dep(2, 'архивный отдел ресурсов'),
    Dep(3, 'бухгалтерия'),

    Dep(11, 'отдел (другой) кадров'),
    Dep(22, 'архивный (другой) отдел ресурсов'),
    Dep(33, '(другая) бухгалтерия'),
]

# Микропроцессоры
emps = [
    Emp(1, 'Артамонов', 25000, 1),
    Emp(2, 'Петров', 35000, 2),
    Emp(3, 'Иваненко', 45000, 3),
    Emp(4, 'Иванов', 35000, 3),
    Emp(5, 'Иванин', 25000, 3),
]

emps_deps = [
    EmpDep(1, 1),
    EmpDep(2, 2),
    EmpDep(3, 3),
    EmpDep(3, 4),
    EmpDep(3, 5),

    EmpDep(11, 1),
    EmpDep(22, 2),
    EmpDep(33, 3),
    EmpDep(33, 4),
    EmpDep(33, 5),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(e.name, e.cores, d.model)
                   for d in deps
                   for e in emps
                   if e.dep_id == d.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.model, ed.dep_id, ed.emp_id)
                         for d in deps
                         for ed in emps_deps
                         if d.id == ed.dep_id]

    many_to_many = [(e.name, e.cores, dep_name)
                    for dep_name, dep_id, emp_id in many_to_many_temp
                    for e in emps if e.id == emp_id]

    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)

    print('\nЗадание А2')
    res_12_unsorted = []
    # Перебираем все отделы
    for d in deps:
        # Список сотрудников отдела
        d_emps = list(filter(lambda i: i[2] == d.model, one_to_many))
        # Если отдел не пустой
        if len(d_emps) > 0:
            # Зарплаты сотрудников отдела
            d_sals = [sal for _, sal, _ in d_emps]
            # Суммарная зарплата сотрудников отдела
            d_sals_sum = sum(d_sals)
            res_12_unsorted.append((d.model, d_sals_sum))

    # Сортировка по суммарной зарплате
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание А3')
    res_13 = {}
    # Перебираем все отделы
    for d in deps:
        if 'отдел' in d.model:
            # Список сотрудников отдела
            d_emps = list(filter(lambda i: i[2] == d.model, many_to_many))
            # Только ФИО сотрудников
            d_emps_names = [x for x, _, _ in d_emps]
            # Добавляем результат в словарь
            # ключ - отдел, значение - список фамилий
            res_13[d.model] = d_emps_names

    print(res_13)


if __name__ == '__main__':
    main()

# Результаты
# выполнения:
#
# Задание
# А1
# [('Петров', 35000, 'архивный отдел ресурсов'), ('Иваненко', 45000, 'бухгалтерия'), ('Иванов', 35000, 'бухгалтерия'),
#  ('Иванин', 25000, 'бухгалтерия'), ('Артамонов', 25000, 'отдел кадров')]
#
# Задание
# А2
# [('бухгалтерия', 105000), ('архивный отдел ресурсов', 35000), ('отдел кадров', 25000)]
#
# Задание
# А3
# {'отдел кадров': ['Артамонов'], 'архивный отдел ресурсов': ['Петров'], 'отдел (другой) кадров': ['Артамонов'],
#  'архивный (другой) отдел ресурсов': ['Петров']}
