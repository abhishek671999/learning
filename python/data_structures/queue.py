class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        try:
            return self.queue.pop()
        except IndexError as IE:
            print("Queue is empty. Can't dequeue!!")

    def peep(self):
        return self.queue[-1]

    def display(self):
        for values in self.queue:
            print(values, end=' ')
        else:
            print()


if __name__=='__main__':
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
    queue.dequeue()
    queue.display()