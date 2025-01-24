#tasks.py
from datetime import datetime

class Task:
    counter = 0 # class variable

    def __init__(self, name: str, priority: int = 1, due_dt: datetime = None):
        self.__class__.counter +=1

        self.id = self.counter
        self.name = name
        self.status = False
        self.priority = priority
        self.created_dt = datetime.now()  # Automaticky nastaví aktuální čas
        self.due_dt = due_dt
    
    def __str__(self):
        # Pevné šířky sloupců
        id_col = str(self.id).ljust(5)
        checkbox = ("✅" if self.status else "🟥").ljust(5)
        name_col = self.name.ljust(40)  # 20 znaků pro název
        priority_col = f"{self.priority}".ljust(10)
        deadline_col = self.due_dt.strftime("%d.%m.%Y") if self.due_dt else ""
        return f"{id_col}{checkbox}{name_col}{priority_col}{deadline_col}"
    
    def finish(self):
        self.status = True

    def undo(self):
        self.status = False

class SuperTask(Task):
    pass

class TaskList:
    def __init__(self, name:str):
        self.name = name
        self.tasks = {}

    def add_task(self, task: Task):
        if task.id not in self.tasks:
            self.tasks[task.id] = task
    def remove_task(self, task:Task):
        return self.remove_task_by_id(task.id)

    def remove_task_by_id(self, task_id: int):
        try:
            removed_task = self.tasks.pop(task_id)
            return removed_task
        except KeyError:
            return None
        
    def finish_task_by_id(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id].finish()
    
    def undo_task_by_id(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id].undo()
    
    def show(self):
        for task in self.tasks.values():
            print(task)
        
    @staticmethod
    def print_header():
        header = f"{'ID'.ljust(5)}{'[ ]'.ljust(5)}{'Name'.ljust(40)}{'Priority'.ljust(10)}Deadline"
        print(header)
        print("-" * len(header))

    def display_tasks(self):
        print(f"Task List: {self.name}")
        print("=" * (len(f"Task List: {self.name}") + 2))
        self.print_header()
        for task in self.tasks.values():
            print(task)

"""
task1 = Task("Ukol 1")
task2 = Task("Ukol 2")
task3 = Task("Ukol 3", priority=10, due_dt = datetime(2025, 1, 31))
task3.finish()
task2.finish()



task_list = TaskList("Seznam ukolů")
task_list.add_task(task1)
task_list.add_task(task2)
task_list.add_task(task3)
task_list.add_task(Task("Napsat testy"))
task_list.add_task(Task("Zkontrolovat SQL příkazy"))
task_list.finish_task_by_id(1)
task_list.finish_task_by_id(4)
task_list.undo_task_by_id(2)

task_list.display_tasks()
"""

