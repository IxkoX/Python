# tasks_app.py
from tasks import Task, TaskList

task_list = TaskList('Ukoly')

while True:
    command = input('Zadej přikaz: ')

    if command == 'add':
        text = input('Zadej text: ')
        task_list.add_task(Task(text))

    if command == 'finish':
        task_id = int(input('Zadej id: '))
        task_list.finish_task_by_id(task_id)
    
    if command == 'dell':
        task_id = int(input('Zadej id: '))
        task_list.remove_task_by_id(task_id)


    task_list.show()


a = 10
a += 10
