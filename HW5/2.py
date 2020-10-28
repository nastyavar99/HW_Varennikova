class MinStack:
    def __init__(self):
        self.lst = []
        self.min_elem = None

    def push(self, x: int) -> None:
        self.lst.append(x)
        if self.min_elem is None or self.min_elem > x:
            self.min_elem = x

    def pop(self) -> None:
        if self.lst:
            self.lst.pop()

        self.min_elem = min(self.lst) if self.lst else None

    def top(self) -> int:
        return self.lst[-1]

    def getMin(self) -> int:
        return self.min_elem