#Exercise 15.6 & 15.7

from random import randint

class Die:
    """A class to manage a die"""

    def __init__(self, num_sides=6):
        """Initializing the die"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random number from 1 - num_sides"""
        return randint(1, self.num_sides)    