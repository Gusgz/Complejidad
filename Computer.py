import random
class Computer:
    def __init__(self):
        self.position = random.randint(0,4)
        self.name = "Charlie"
        self.points = 0
    def move(self):
        self.position = random.randint(0,4)