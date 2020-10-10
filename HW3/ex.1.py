""""
1.  Реализуйте класс OneIndexedList, который имитирует поведение списка, использующего индексацию начинающуюся
с 1 (а не с 0, как в стандартном списке). Используйте магические методы init, setitem, getitem.
"""


class OneIndexedList:
    def __init__(self, items=None):
        self.items = items or []

    def __getitem__(self, idx):
        return self.items[idx - 1]

    def __setitem__(self, idx, value):
        self.items[idx - 1] = value


a = OneIndexedList()
a.items.append(0)
print(a[1])
