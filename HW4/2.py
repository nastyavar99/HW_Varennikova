class ReverseIter:
    def __init__(self, lst=None):
        self.lst = lst or []
        self.i = -1
        self.length = len(self.lst) + 1

    def __iter__(self):
        return self

    def __next__(self):
        if abs(self.i) != self.length:
            number = self.lst[self.i]
            self.i -= 1
            return number
        else:
            raise StopIteration()
