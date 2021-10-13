import heapq

class Heapify(object):
    def __init__(self, data=None):
        self.data = data or []
        for i in range(len(data)//2, -1, -1):
            self.__max_heapify__(i)

    def __repr__(self):
        return repr(self.data)

    def parent(self, i):
        if i & 1: # Sets each bit to 1 if both bits are 1
            return i >> 1 # shift to right 1 bit ( Zero fill left shift )
        else:
            return (i >> 1) - 1

    def left_child(self, i):
        return (i << 1) + 1 # shift to left 1 bit

    def right_child(self, i):
        return (i << 1) + 2 # shift to left 1 bit

    def __max_heapify__(self, i):
        largest = i # 현재 노드
        left = self.left_child(i)
        right = self.right_child(i)
        n = len(self.data)

        # 왼쪽 자식
        largest = (left < n and self.data[left] > self.data[i]) and left or i
        # True 면 left 아니면 i
        # 오른쪽 자식
        largest = (right < n and self.data[right] > self.data[largest]) and \
                  right or largest
        # True 면 right 아니면 largest

        # 현재 노드가 자식들보다 크면 skip, 자식이 크다면 swap
        if i is not largest:
             self.data[i], self.data[largest] = self.data[largest], self.data[i]

             self.__max_heapify__(largest)

    def extract_max(self):
        n = len(self.data)
        max_element = self.data[0]

        # 첫번째 노드에 마지막 노드를 삽입
        self.data[0] = self.data[n-1]
        self.data = self.data[:n-1]
        self.__max_heapify__(0)
        return max_element

    def insert(self, item):
        i = len(self.data)
        self.data.append(item)
        while (i != 0) and item > self.data[self.parent(i)]:
            print(self.data)
            self.data[i] = self.data[self.parent(i)]
            i = self.parent(i)
        self.data[i] = item


def test_heapify():
    l1 = [3, 2, 5, 1, 7, 8, 2]
    h = Heapify(l1)
    assert(h.extract_max() == 8)
    print(h)


if __name__ == "__main__":
     # for i in range(10):
     #      print(i)
     #      print("i & 1: {0}".format(i & 1))
     #      print("i >> 1: {0}".format(i >> 1))
     #      print("i << 1: {0}".format(i << 1))

    # print(False and 1 or 2)

    test_heapify()
