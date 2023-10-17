import unittest
from main import *


class TestRK2(unittest.TestCase):
    # Компьютеры
    deps = [
        Dep(1, 'MacBook Air'),
        Dep(2, 'MacBook Pro'),
        Dep(3, 'iMac 2013'),

        Dep(11, 'ASUS 2000'),
        Dep(22, 'Acer 2003'),
        Dep(33, 'Honor 2020'),
    ]

    # Микропроцессоры
    emps = [
        Emp(1, 'Pentium', 2, 11),
        Emp(2, 'Celeron', 1, 11),
        Emp(3, 'Core i3', 4, 33),
        Emp(4, 'Core i7', 2, 33),
        Emp(5, 'M1', 8, 2),
    ]

    def test_A1(self):
        one_to_many = [(e.name, e.cores, d.model)
                       for d in deps
                       for e in emps
                       if e.dep_id == d.id]
        self.assertEqual(a1_solution(one_to_many),
                         [('Pentium', 2, 'ASUS 2000'), ('Celeron', 1, 'ASUS 2000'), ('Core i3', 4, 'Honor 2020'),
                          ('Core i7', 2, 'Honor 2020'), ('M1', 8, 'MacBook Pro')])

    def test_A2(self):
        one_to_many = [(e.name, e.cores, d.model)
                       for d in deps
                       for e in emps
                       if e.dep_id == d.id]
        self.assertEqual(a2_solution(one_to_many),
                         [('MacBook Pro', 8), ('Honor 2020', 6), ('ASUS 2000', 3)])

    def test_A3(self):
        many_to_many_temp = [(d.model, ed.dep_id, ed.emp_id)
                             for d in deps
                             for ed in emps_deps
                             if d.id == ed.dep_id]

        many_to_many = [(e.name, e.cores, dep_name)
                        for dep_name, dep_id, emp_id in many_to_many_temp
                        for e in emps if e.id == emp_id]
        self.assertEqual(a3_solution(many_to_many),
                         {'MacBook Air': ['Pentium', 'Celeron', 'Core i3'], 'MacBook Pro': ['M1'],
                          'iMac 2013': ['Core i7']})


if __name__ == '__main__':
    unittest.main()
