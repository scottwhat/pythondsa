import random

class Task:

    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1,21)