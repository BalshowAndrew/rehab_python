class Employee:
    """Класс сотрудников"""
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    def info(self):
        print(f"{self.name} ({self.position}): зарплата {self.salary}")
    def give_raise(self, amount):
        self.salary += amount

employee_01 = Employee('Иван', 'Manager', 100_000)

employee_01.info()
employee_01.give_raise(250)
employee_01.info()
