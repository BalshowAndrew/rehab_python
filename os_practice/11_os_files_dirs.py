"""Work with files and directories with os"""

import os

# Навигация по файловой системе

current_directory = os.getcwd()
print(f"Сейчас мой скрипт работает отсюда: {current_directory}")

whats_inside = os.listdir()
print("Внутри этой папки лежат:")
print(whats_inside)

whats_inside = os.listdir('/home/andrew/rehabilit_python')
print("Внутри папки rehabilit_python лежат:")
print(whats_inside)

whats_inside = os.listdir('.venv')
print("Внутри папки .venv лежат:")
print(whats_inside)

print(f"Сначала я здесь: {os.getcwd()}")
os.chdir('../..')
print(f"Теперь я здесь: {os.getcwd()}")
os.chdir('/home/andrew/rehabilit_python/rehab')
print(f"А теперь я снова здесь: {os.getcwd()}")

# управление папками

os.mkdir('reposits')
os.makedirs('archive/2025/photos')
print(os.listdir())

os.rmdir('reposits')
os.rmdir('archive/2025/photos')
os.rmdir('archive/2025')
os.rmdir('archive')
print(os.listdir())

# Одновременное переименование и перемещение файла

with open('old_name.txt', 'w') as f:
    f.write('some text')

os.rename('old_name.txt', 'new_name.txt')

os.mkdir('archive')
os.rename('new_name.txt', 'archive/name.txt')

# Удалим перемещенный файл и папку
os.remove('archive/name.txt')
os.rmdir('archive')