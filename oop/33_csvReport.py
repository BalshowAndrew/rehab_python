"""CSV Report"""

import pandas as pd
from pathlib import Path
import kaggle


class CSVReport:
    """CSV Report"""
    def __init__(self, path: str):
        self.path = path
        self.df = pd.read_csv(path)
        print(f"Я загрузил файл из пути: {self.path}")
    def get_shape(self):
        print(f"В датасете {self.df.shape[0]} строк и {self.df.shape[1]} столбцов")
    def get_columns(self):
        return self.df.columns.tolist()    



kaggle.api.authenticate()
kaggle.api.dataset_download_files(
    'heptapod/titanic',
    path='oop/datas',
    unzip=True)

path = Path('oop/datas/train_and_test2.csv')
absolut_path = path.resolve()


titanic = CSVReport(absolut_path)
titanic.get_shape()
print(titanic.get_columns())


