class First(object):
    def __init__(self):
        super(First, self).__init__()
        print("first")

class Second(object):
    def __init__(self):
        super(Second, self).__init__()
        print("second")

# 다중 상속 가능
class Third(First, Second):
    def __init__(self):
        super(Third, self).__init__()
        print("third")
t = Third()
