import os

# Собираем путь

folder = 'archive'
filename = 'report.text'

full_path = os.path.join('home', 'andrew', 'rehabilit_python', 'rehab', folder, filename)
print(full_path)

# Получаем из пути имя файла
filename = os.path.basename(full_path)
print(f"Имя файла: {filename}")

# Получаем путь к папке, в которой лежит файл
directory = os.path.dirname(full_path)
print(f"Путь к папке: {directory}")