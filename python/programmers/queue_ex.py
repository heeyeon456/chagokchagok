class Queue(object):
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        value = self.items[-1]
        if value is not None:
            self.items = self.items[:-1]
            return value
        else:
            print("Queue is empty")

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("Queue is empty")

    def __repr__(self):
        return repr(self.items)

if __name__ == "__main__":
    queue = Queue()
    print("Is queue empty? {0}".format(queue.empty()))
    for i in range(10):
        queue.enqueue(i)
    print(queue)
    print("Size of queue: {0}".format(queue.size()))
    print("dequeue: {0}".format(queue.dequeue()))
    print("dequeue: {0}".format(queue.dequeue()))
    print("dequeue: {0}".format(queue.dequeue()))
    print(queue)
