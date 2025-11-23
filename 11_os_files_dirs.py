"""Work with files and directories with os"""

import os

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
