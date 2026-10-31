class MinStack:

    def __init__(self):
        self.normal_stack = []
        self.extra_stack = []
        
    def push(self, val: int) -> None:
        self.normal_stack.append(val)
        if self.extra_stack:
            self.extra_stack.append(min(self.extra_stack[len(self.extra_stack)-1], val))
        else:
             self.extra_stack.append(val)

    def pop(self) -> None:
        self.normal_stack.pop()
        self.extra_stack.pop()
        
    def top(self) -> int:
        return self.normal_stack[len(self.normal_stack)-1]

    def getMin(self) -> int:
        return self.extra_stack[len(self.extra_stack)-1]
        
