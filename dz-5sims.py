class Task:
    def __init__(self, title, description, deadline):
        self.title = title  # Назва завдання
        self.description = description  # Опис завдання
        self.deadline = deadline  # Дедлайн завдання
        self.is_done = False  # Стан завдання (виконано/не виконано)

    def mark_as_done(self):
        self.is_done = True  # Відмічаємо завдання як виконане

    def __str__(self):
        status = "Виконано" if self.is_done else "Не виконано"
        return f"Завдання: {self.title}\nОпис: {self.description}\nДедлайн: {self.deadline}\nСтан: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []  # Список завдань

    def add_task(self, task):
        self.tasks.append(task)  # Додаємо завдання до списку

    def remove_task(self, task_title):
        self.tasks = [task for task in self.tasks if task.title != task_title]  # Видаляємо завдання за назвою

    def mark_task_as_done(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                task.mark_as_done()  # Відмічаємо завдання як виконане
                break

    def list_tasks(self):
        if not self.tasks:
            print("Немає завдань.")
        else:
            for task in self.tasks:
                print(task)
                print("-" * 40)  # Розділитель між завданнями


# Приклад використання:

task1 = Task("Написати звіт", "Написати щотижневий звіт для керівництва", "2024-11-25")
task2 = Task("Прочитати книгу", "Прочитати главу 5 з книги 'Python для початківців'", "2024-11-30")

task_manager = TaskManager()
task_manager.add_task(task1)
task_manager.add_task(task2)

# Вивести список всіх завдань
task_manager.list_tasks()

# Відмітити завдання як виконане
task_manager.mark_task_as_done("Написати звіт")

# Вивести список після зміни
print("\nОновлений список завдань:")
task_manager.list_tasks()

# Видалити завдання
task_manager.remove_task("Прочитати книгу")
print("\nСписок після видалення завдання:")
task_manager.list_tasks()