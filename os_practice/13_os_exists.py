import os

path_to_check = 'archive'

if os.path.exists(path_to_check):
    print(f"Путь '{path_to_check}' существует.")
    if os.path.isdir(path_to_check):
        print("и эта папка!")    
    elif os.path.isfile(path_to_check):
        print("И этот файл!")    
else:
    print(f"Пути '{path_to_check}' не существует. Давайте создадим папку.")        
    os.makedirs(path_to_check)    
