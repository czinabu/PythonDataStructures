'''
Author: Caleb Zinabu
Assignment: EECS 268 Lab 5 Exercise 2
Last Modified: 7/20/2022
Code Description: Use recursive method to find the number of people with the flu.
'''
class Executive:
    def __init__(self):
        self.day = 0

    def get_input(self): # get user input for day
        try:
            self.day = int(input("What day do you want a sick count for?: "))
        except TypeError:
            print("Your day must be a number.")

    def outbreak(self, day): # check for valid return from recursive function
        if self._rec_outbreak(day) == None:
            return False        
        else:
            return self._rec_outbreak(day)

    def _rec_outbreak(self, day): # return sum of previous 3 days from given day
        if day == 1:
            return 6
        
        if day == 2:
            return 20
        
        if day == 3:
            return 75
        
        if day > 3:
            return (self._rec_outbreak(day-1) + self._rec_outbreak(day-2) + self._rec_outbreak(day-3))

    def run(self): # run the executive class
        self.get_input()

        if not self.outbreak(self.day):
            print("Invalid day")
        else:
            print("Total people with flue:",self.outbreak(self.day))

    def __eq__(self, other):
        return self.day == other.day

    def __gt__(self, other):
        return self.day > other.day
