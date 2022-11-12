
class MyCircularQueue:
    def __init__(self,k:int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0         #front
        self.p2 = 0         #rear
    
    #enQueue() : rear 포인터 이동
    def enQueue(self,value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2+1) % self.maxlen
            return True
        else:
            return False
    
    #deQueue() : front 포인터 이동
    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1+1) % self.maxlen
            return True
    
    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]
    
    def Rear(self) -> int:
        return -1 if self.q[self.p2-1] is None else self.q[self.p2-1]
    
    def isEmpty(self) ->bool:
        return self.p1 == self.p2 and self.q[self.p1] is None
    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None

q = MyCircularQueue(10)
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)
q.enQueue(5)
q.enQueue(6)
q.enQueue(7)
q.enQueue(8)
q.enQueue(9)
print(q.Front(),'',q.Rear())
q.deQueue()
print(q.Front(),'',q.Rear())

