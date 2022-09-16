#Exercise 15.10
from random import randint

class Die:
    """A class to manage a die"""

    def __init__(self,num_sides=6):
        """Initializing the die"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random integer between 1 and 6"""
        return randint(1,self.num_sides)