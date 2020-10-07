class Queue:

    def __init__(self, queue_size = 7):
        self.queue_size = queue_size
        self.queue = [None] * queue_size
        self.rear = -1
        self.front = -1

    def isempty(self):
        if self.rear and self.front == -1:
            return True
        else:
            return False

    def isfull(self):
        if self.rear == self.queue_size:
            return True
        else:
            return False

    def enqueue(self, value):
        if not self.isfull():
            if self.isempty():
                self.rear += 1
                self.front += 1
                self.queue[self.rear] =  value
            else:
                self.rear += 1
                self.queue[self.rear] =  value
            return True
        else:
            return False

    def dequeue(self):
        if not self.isfull() and not self.isempty():
            returnval = self.queue[self.rear]
            self.queue[self.rear] = None
            self.rear -= 1
            return returnval
        return False

    def printing(self):
        print(self.queue)

Queue1 = Queue(6)
Queue1.enqueue(3)
Queue1.enqueue(2)
Queue1.enqueue(7)
Queue1.dequeue()
Queue1.printing()
