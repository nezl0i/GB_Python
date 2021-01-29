# 3. Реализовать базовый класс Worker (работник).
# - определить атрибуты: name, surname, position (должность), income (доход);
# - последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# - создать класс Position (должность) на базе класса Worker;
# - в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# - проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])


worker_1 = Position("Genry", "Richardson", "Manager", {"wage": 150000, "bonus": 25000})
worker_2 = Position("Donald", "Duck", "Millionere", {"wage": 12500, "bonus": 320})

print(worker_1.position)
print(worker_2.position)


worker_1.get_full_name()
worker_1.get_total_income()
worker_2.get_full_name()
worker_2.get_total_income()


