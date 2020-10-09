class CircularQueue:

    def __init__(self, queue_size = 7):
        self.queue_size = queue_size
        self.queue = [None] * queue_size
        self.front = -1
        self.rear = -1

    '''checks if the stack is empty (used in enqueue and dequeue methods)'''
    def isempty(self):
        '''if the rear pointer and front pointer are bith minus 1 the queue
        is empty'''
        if (self.rear == -1) and (self.front == -1):
            return True
        else:
            return False

    def isfull(self):
        if (self.rear + 1) % self.queue_size == self.front:
            return True
        else:
            return False

    def add_item(self, value):
        if not self.isfull():
            if self.isempty():
                self.front = 0
                self.rear = 0
                self.queue[self.rear] = value
            else:
                self.rear = (self.rear + 1) % self.queue_size
                self.queue[self.rear] = value
            return True
        return False

    def remove_item(self):
        if not self.isempty():
            self.queue[self.front] = None
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.queue_size
            return True
        return False

    def printing(self):
        print(self.queue)
        return True
