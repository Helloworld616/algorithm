class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, num):
        self.data.append(num)

    def dequeue(self):
        self.data.pop(0)

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    # 삭제 없이 단순히 맨 앞의 data 값을 리턴
    def get_front(self):
        return self.data[0]

    # 삭제 없이 단순히 맨 뒤의 data 값을 리턴
    def get_rear(self):
        return self.data[-1]


q = Queue()
q.enqueue(1) # None, q.data => [1]
q.enqueue(2) # None, q.data => [1, 2]
q.get_front() # 1
q.get_rear() # 2
print(q.get_front())
print(q.get_rear())
q.dequeue()
q.dequeue()