class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        raise Exception("stack is Empty")        
    
    def __len__(self):
        return len(self.stack)
    
    def display(self):
        while self.stack:
            print(self.stack.pop())
    
stack = Stack()
stack.push(2)
stack.push(6)
stack.push(1)
stack.push(5)
stack.push(3)    