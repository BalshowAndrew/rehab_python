import os

def solve():
    """
    Задание 1: Создание дерева директорий
    
    Внутри этой функции нужно написать код, который создает в папке `tasks/data_for_task_1` 
    следующую структуру директорий: `media/images/icons/`. Вы должны создать все вложенные папки одной командой.
    """
    # os.chdir('os_practice/os_homework/tasks')
    path_structure = os.path.join(
        'os_practice',
        'os_homework',
        'tasks',
        'data_for_task_1',
        'media',
        'images',
        'icons')
    os.makedirs(path_structure, exist_ok=True)