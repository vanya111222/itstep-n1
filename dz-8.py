class Employee:
    def __init__(self, name, position, salary):
        self.name = name  # Ім'я співробітника
        self.position = position  # Посада співробітника
        self.salary = salary  # Заробітна плата співробітника

    def __str__(self):
        return f"Співробітник: {self.name}, Посада: {self.position}, Заробітна плата: {self.salary} грн"


class Department:
    def __init__(self, name):
        self.name = name  # Назва відділу
        self.employees = []  # Список співробітників у відділі

    def add_employee(self, employee):
        self.employees.append(employee)  # Додавання співробітника в відділ

    def remove_employee(self, employee_name):
        self.employees = [emp for emp in self.employees if emp.name != employee_name]  # Видалення співробітника за ім'ям

    def total_salary(self):
        total = sum(emp.salary for emp in self.employees)  # Підрахунок загальної заробітної плати
        return total

    def list_employees(self):
        if not self.employees:
            print(f"Відділ {self.name} не має співробітників.")
        else:
            print(f"Співробітники відділу {self.name}:")
            for employee in self.employees:
                print(employee)
                print("-" * 40)  # Розділитель між співробітниками

# Приклад використання:

# Створення співробітників
emp1 = Employee("Олександр Іванов", "Менеджер проектів", 25000)
emp2 = Employee("Марина Петренко", "Аналітик", 20000)
emp3 = Employee("Ігор Сидоров", "Розробник", 30000)

# Створення відділу
department = Department("ІТ відділ")

# Додавання співробітників до відділу
department.add_employee(emp1)
department.add_employee(emp2)
department.add_employee(emp3)

# Виведення списку співробітників відділу
department.list_employees()

# Підрахунок загальної заробітної плати відділу
print(f"Загальна заробітна плата відділу: {department.total_salary()} грн")

# Видалення співробітника
department.remove_employee("Марина Петренко")

# Виведення списку співробітників після видалення
print("\nОновлений список співробітників:")
department.list_employees()

# Підрахунок загальної заробітної плати після видалення співробітника
print(f"Загальна заробітна плата відділу після видалення: {department.total_salary()} грн")
