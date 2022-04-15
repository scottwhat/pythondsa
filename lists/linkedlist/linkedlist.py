from .node import Node

class LinkedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

#adding at the head
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def remove(self,item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

            if previous == None:
                self.head = current.getNext
            else:
                previous.setNext(current.getNext())

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


    def search(self, item):
        if self.isEmpty():
            return False
        else:
            current = self.head
            found = False
            position = 0
            while current != None and not found:
                if current.getData == item:
                    found = True

                elif current != item:
                    position + 1
                    current = current.getNext()
            return found


    def size(self):
        if self.isEmpty():
            return 0
        else:
            counter = 0
            current = self.head
            while current != None:
                counter + 1
                current = current.getNext()
            return counter







