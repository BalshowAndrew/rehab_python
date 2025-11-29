# сортируем файлы папки Downloads

import os
import shutil

PATH_TO_SORT = '/home/andrew/Downloads'

all_items = os.listdir(PATH_TO_SORT)

for item in all_items:
    item_full_path = os.path.join(PATH_TO_SORT, item)
    if os.path.isfile(item_full_path):
        try:
            extension = item.split('.')[-1].lower()
            target_folder = ''
            if extension in ['jpg', 'jpeg', 'png', 'gif', 'bmp']:
                target_folder = 'Images'
            elif extension in ['pdf', 'docx', 'doc', 'txt', 'xslx']:
                target_folder = 'Documents'
            elif extension in ['zip', 'rar', '7z']:
                target_folder = 'Archives'
            else:
                target_folder = 'Other'

            target_folder_path = os.path.join(PATH_TO_SORT, target_folder)
            if not os.path.exists(target_folder_path):
                os.makedirs(target_folder_path)
                print(f"Создана папка: {target_folder}")

            shutil.move(item_full_path, target_folder_path)
            print(f"Файл '{item}' перемещен в папку '{target_folder}'")
        except Exception as e:
            print(f"Не удалось обработать файл '{item}'. Ошибка: {e}")

print("\nСортировка завершена!")            

