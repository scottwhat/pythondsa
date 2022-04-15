
class Deque:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    #use the last index as the first to keep o(1) time
    def addFront(self, item):
        self.items.append(item)

    #add rear o(n) time
    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        self.items.pop()

    def removeRear(self):
        self.items.pop(0)

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
