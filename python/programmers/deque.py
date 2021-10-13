from queue import Queue
from collections import deque

class Deque(Queue):
    def enqueue_back(self, item):
        self.items.append(item)

    def dequeue_front(self):
        value = self.items.pop(0)
        if value is not None:
            return value
        else:
            print("Deque is empty")

if __name__ == "__main__":
    q = deque(['buffy', 'gender', 'wallo'])
    print(q)
    q.append("zails")
    print(q.popleft())
    print(q.pop())
    print(q)
    q.appendleft("angel")
    print(q)
