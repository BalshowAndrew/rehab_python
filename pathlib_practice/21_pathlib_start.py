from pathlib import Path

# Создаем путь к файлу
config_path = Path('settings/production/database.ini')

# Получаем специальные пути
current_dir = Path.cwd()
home_dir = Path.home()

print(f"Путь к конфигу: {config_path}")
print(f"Текущая директория: {current_dir}")
print(f"Домашняя диррктория: {home_dir}")

root_path = Path('/etc')
full_path = root_path / 'nginx' / 'nginx.conf'

print(full_path)

# Аблолютные и относительные пути
path = Path('os_practice/os_homework/tasks/task_1.py')
print(f"Путь '{path}' абсолютный? {path.is_absolute()}")

# превращаем относительный путь в абсолютный
absolute_path = path.resolve()
print(f"Абсолютный путь: {absolute_path}")
print(f"Путь '{absolute_path}' абсолютный? {absolute_path.is_absolute()}")

# разбор пути на компоненты
print(f"Родительская директория: {absolute_path.parent}")
print(f"Имя файла: {absolute_path.name}")
print(f"Имя без расширения: {absolute_path.stem}")
print(f"Расширение: {absolute_path.suffix}")
print(f"Кортеж из частей пути: {absolute_path.parts}")

# поднимаемся по дереву каталогов
print(f"Первый родитель: {absolute_path.parents[0]}")
print(f"Второй родитель: {absolute_path.parents[1]}")
print(f"Третий родитель: {absolute_path.parents[2]}")

# проверка существования файла или директории
if absolute_path.exists():
    if absolute_path.is_file():
        print(f"Файл '{absolute_path.name}' существует")
    elif absolute_path.is_dir():
        print(f"Директория '{absolute_path}' существует")
           
# Создадим дирректорию
path_obj = Path('pathlib_practice/homeworks')

path_obj.mkdir(parents=True, exist_ok=True)
print(f"Директория '{path_obj}' успешно создана или уже существует.")

# Чтение и запись файлов
path_obj = Path('hello.txt')
content = 'Привет, мир pathlib'

path_obj.write_text(content, encoding='utf-8')

read_content = path_obj.read_text(encoding='utf-8')
print(read_content)

# Переименование и перемещение
src = Path('hello_pathlib.txt')
dst = Path('hello.txt')

if src.exists():
    src.rename(dst)
    print(f"Файл '{src}' переименован в '{dst}'.")

# Удаление файлов и директорий
file_to_del = Path('hello.txt')
dir_to_del = Path('pathlib_practice/homeworks')

if file_to_del.exists():
    file_to_del.unlink()

if dir_to_del.exists():
    dir_to_del.rmdir()
