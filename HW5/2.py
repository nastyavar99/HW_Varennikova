class MinStack:
    def __init__(self):
        self.lst = []
        self.min_elem = []

    def push(self, x: int) -> None:
        self.lst.append(x)
        if not self.min_elem:
            self.min_elem.append(x)
        else:
            if x < self.min_elem[-1]:
                self.min_elem.append(x)
            else:
                self.min_elem.append(self.min_elem[-1])

    def pop(self) -> None:
        if self.lst:
            self.lst.pop()
            self.min_elem.pop()

    def top(self) -> int:
        return self.lst[-1]

    def getMin(self) -> int:
        return self.min_elem[-1]
