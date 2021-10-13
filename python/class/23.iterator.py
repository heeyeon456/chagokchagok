class MyIter:
    def __init__(self):
        self.nCnt = -1
        self.data = [11, 22, 33, 44, 55]

    def __next__(self):
        self.nCnt += 1
        if self.nCnt == 5:
            raise StopIteration()
        return self.data[self.nCnt]

it = MyIter()

for n in it: # n = next(it), n=next(it) ...
    print(n)
# print(next(it)) # it.__next__()
# print(it.__next__())
