class MinStack:

    def __init__(self):
        self.data = []
        self.minimums = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.minimums or val <= self.minimums[-1]:
            self.minimums.append(val)

    def pop(self) -> None:
        if self.data:
            if self.data[-1] == self.minimums[-1]:
                self.minimums.pop()
            self.data.pop()

    def top(self) -> int:
        if self.data:
            return self.data[-1]

    def getMin(self) -> int:
        if self.minimums:
            return self.minimums[-1]


if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())
