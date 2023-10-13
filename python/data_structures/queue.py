class Queue:
    def __init__(self):
        self.__stack = []

    def enqueue(self, value):
        self.__stack.append(value)

    def dequeue(self):
        try:
            temp = self.__stack[0]
            del self.__stack[0]
            return temp
        except IndexError as IE:
            print('Queue is empty. Can\'t dequeue further')

    def display(self):
        for value in self.__stack:
            print(value, end=' ')
        else:
            print()


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.display()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.display()


