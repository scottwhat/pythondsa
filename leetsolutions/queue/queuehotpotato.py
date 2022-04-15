
"""
This game is a modern-day equivalent of the famous Josephus problem. 
Based on a legend about the famous first-century historian Flavius Josephus, 
he story is told that in the Jewish revolt against Rome, Josephus and 39 of his
 comrades held out against the Romans in a cave. With defeat imminent, they decided
  that they would rather die than be slaves to the Romans. They arranged themselves 
  in a circle. One man was designated as number one, and proceeding clockwise they killed
   every seventh man. Josephus, according to the legend, was among other things an accomplished 
   mathematician. He instantly figured out where he ought to sit in order to be the last to go. 
   When the time came, instead of killing himself, he joined the Roman side. You can find many 
   different versions of this story. Some count every third
 man and some allow the last man to escape on a horse. In any case, the idea is the same.
 
 steps
 
 add all names to queue
 start making rounds up to num, when reach num (dequeue) kill the last name
 repeat until 1 left
 announce winner 
"""
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def hotPotato(nameList, num):
    round = 0
    nameque = Queue()

    for name in nameList:
        nameque.enqueue(name)

    while nameque.size() > 1:
        for i in range(num):
            nameMove = nameque.dequeue()
            nameque.enqueue(nameMove)
        killname = nameque.dequeue()
        print(killname + " is dead")

    print(str(nameque.dequeue())+" survived")


nameL = ["billy","bobby","jaimie","steven"]
print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))


"""
optimal solution


def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))

"""

