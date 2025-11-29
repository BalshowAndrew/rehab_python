import os

def solve():
    """
    Задание 2: Очистка от временных файлов
    
    В папке `tasks/data_for_task_2` находится беспорядок из разных файлов. 
    Вам нужно написать код, который найдет и **удалит** все файлы, заканчивающиеся на `.tmp`. 
    Другие файлы должны остаться нетронутыми.
    """
    path_to_dir = 'os_practice/os_homework/tasks/data_for_task_2'
    os.chdir(path_to_dir)
    whats_inside = os.listdir()
    # print(whats_inside)
    for item in whats_inside:
        if item.split('.')[-1].lower() == 'tmp':
            os.remove(item)
        else: pass
    # print(os.listdir())        

# solve()