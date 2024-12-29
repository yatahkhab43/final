class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop() if self.stack else "Stack is empty"

    def peek(self):
        return self.stack[-1] if self.stack else "Stack is empty"

stack = Stack()
stack.push(10)
stack.push(20)
print("Top Element:", stack.peek())
print("Popped Element:", stack.pop())
