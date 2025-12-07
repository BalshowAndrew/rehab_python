"""Нормализатор данных"""

class MyScaler:
    """Class MyScaler"""
    def __init__(self):
        self._min = None
        self._max = None

    def fit(self, data: list):
        self._min = min(data)
        self._max = max(data)

    def transform(self, data: list):
        if self._min is None:
            raise ValueError("Сначала обучите скалер!")

        diff = self._max - self._min
        if diff == 0:
            return [0.0 for _ in data]
           
        return [(x - self._min)/diff for x in data]


scaler = MyScaler()
data = [5, 5, 5]
# print(scaler.transform([15, 10, 30]))
scaler.fit(data)
print(scaler.transform([15, 10, 30]))
print(scaler.transform([1, 10, 60]))
print(scaler.transform([5, 5, 5]))