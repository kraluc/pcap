# Queue aka FIFO

# Let's taste something new now.
# A queue is a data model characterized by the term FIFO:
# First In - Fist Out.

# Note: a regular queue (line) you know from shops or post offices
# works exactly in the same way -
# a customer who came first is served first too.

# class QueueError(BaseException):


class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.fifo = []

    def put(self, val):
        self.fifo += [val]

    def get(self):
        try:
            return self.fifo.pop(-len(self.fifo))
        except IndexError:
            raise QueueError


class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
        self.__empty = True

    def put(self, val):
        self.__empty = False
        Queue.put(self, val)

    def get(self):
        if len(self.fifo) == 1:
            self.__empty = True
        return Queue.get(self)

    def isempty(self):
        return self.__empty


que = SuperQueue()
que.put(1)
que.put("dog")
que.put("False")

for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue Empty")
