class Stack:
    def __init__(self):
        self.queue = []

    def push(self, value):
        self.queue.append(value)

    def pop(self):
        try:
            return self.queue.pop()
        except IndexError as IE:
            print("Stack is empty. Can't pop!!")

    def display(self):
        for values in self.queue:
            print(values, end=' ')
        else:
            print()


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.display()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.display()