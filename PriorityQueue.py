class PriorityQueue():

    def __init__(self, queue_size = 7):
        self.queue_size = queue_size
        self.queue = [[None]]* queue_size
        self.pointer = -1

    def printing(self):
        print(self.queue)
        return True

    def isempty(self):
        if self.pointer == -1:
            return True
        return False



Queue1 = PriorityQueue()
Queue1.printing()
