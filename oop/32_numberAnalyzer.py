"""Number Analyzer"""

class NumberAnalyzer:
    """Class Number Analyzer"""
    def __init__(self, data: list):
        self.data = data
    def total(self):
        return sum(self.data)
    def average(self):
        if len(self.data) > 0:
            return sum(self.data) / len(self.data)
        else:
            return "Список пуст"
    def show_evens(self):
        return [x for x in self.data if x % 2 == 0]

analyzer = NumberAnalyzer([10, 20, 5, 4])
print(analyzer.total())
print(analyzer.average())
print(analyzer.show_evens())
