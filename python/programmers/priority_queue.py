import heapq

class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority :int):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def __repr__(self):
        return repr(self._queue)

class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({0!r})".format(self.name)

def test_priority_queue():
    # push 와 pop 은 O(logN) 이다.
    q = PriorityQueue()
    q.push(Item('test1'), 1)
    q.push(Item('test2'), 4)
    q.push(Item('test2'), 3)
    print(q)

    value = q.pop()
    print(q)

if __name__ == "__main__":
    test_priority_queue()
