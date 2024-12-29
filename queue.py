class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else "Queue is empty"

    def display(self):
        print("Queue:", self.queue)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.display()
queue.dequeue()
queue.display()
