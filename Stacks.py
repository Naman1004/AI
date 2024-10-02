class Stack:
    def __init__(self):
        self.stack = []

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Add an element to the stack
    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} to the stack")

    # Remove and return the top element of the stack
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    # View the top element without removing it
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    # Get the size of the stack
    def size(self):
        return len(self.stack)

    # Display the stack
    def display(self):
        print(f"Stack: {self.stack}")


# Example usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()

print(f"Top element is {s.peek()}")
print(f"Popped element is {s.pop()}")
s.display()
print(f"Stack size is {s.size()}")
