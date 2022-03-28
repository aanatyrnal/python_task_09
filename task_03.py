# 3. Реализовать базовый класс Worker (работник):
# ● определить атрибуты: name, surname, position (должность), income (доход);
# ● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
# ● создать класс Position (должность) на базе класса Worker;
# ● в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# ● проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, incom):
        self.name = name
        self.surname = surname
        self.position = position
        self._incom_wage = incom['wage']
        self._incom_bonus = incom['bonus']

class Position(Worker):

    def get_full_name(self):
        return f' {self.name} {self.surname} {self.position}'

    def get_total_income(self):
        return round(self._incom_wage + self._incom_bonus, 2)

people = Position('Ivan', 'Ivanov', 'Engineer', {'wage': 200, 'bonus': 100})
print(people.get_full_name())
print(people.get_total_income())
