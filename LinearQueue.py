class LinearQueue:

    '''arg 'queue_size' is automatically set to 7 if no value is passed'''
    def __init__(self, queue_size = 7):
        self.queue_size = queue_size
        self.queue = [None] * queue_size
        self.rear = -1
        self.front = -1

    '''checks if the stack is empty (used in enqueue and dequeue methods)'''
    def isempty(self) -> typing.Union[bool]:
        '''if the rear pointer and front pointer are bith minus 1 the queue
        is empty'''
        if self.rear and self.front == -1:
            return True
        else:
            return False

    def isfull(self) -> typing.Union[bool]:
        '''if the rear pointer is the same as the queue size the queue is full'''
        if self.rear == self.queue_size:
            return True
        else:
            return False

    def enqueue(self, value) -> typing.Union[bool]:
        '''if the queue is full you cannot enqueue anything'''
        if not self.isfull():
            '''if the queue is empty you have to increase the rear and front
             pointer so they are both zero'''
            if self.isempty():
                self.rear += 1
                self.front += 1
            else:
                self.rear += 1
            '''assign the new value to the new rear pointer value in the queue'''
            self.queue[self.rear] =  value
            return True
        return False

    def dequeue(self) -> typing.Union[bool, int]:
        '''if the queue isnt full or empty it can add something to the queue'''
        if not self.isfull() and not self.isempty():
            returnval = self.queue[self.rear]
            self.queue[self.rear] = None
            self.rear -= 1
            return returnval
        return False

    '''allows the user to print the queue (testing reasons)'''
    def printing(self) -> typing.Union[bool]:
        if not self.isempty():
            print(self.queue)
            return True
        return False

Queue1 = LinearQueue(6)
Queue1.enqueue(3)
Queue1.enqueue(2)
Queue1.enqueue(7)
Queue1.dequeue()
Queue1.printing()
