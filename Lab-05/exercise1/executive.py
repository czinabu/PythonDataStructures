'''
Author: Caleb Zinabu
Assignment: EECS 268 Lab 5 Exercise 1
Last Modified: 7/19/2022
Code Description: Prints answer of base taken to power given by user
'''

class Executive:
    def __init__(self):
        self.base = 0
        self.exp = 0

    def get_input(self): # recieve and check base and power from user input
        try:
            self.base = int(input("Enter a base: "))
        except TypeError:
            print("Your base must be an integer.")

        try:
            while self.exp >= 0:
                self.exp = int(input("Enter a power: "))

                if self.exp < 0:
                    print("Sorry, your exponent must be zero or larger.")
                else:
                    break
                    
        except TypeError:
            if type(self.exp) != int:
                print("Your exponent must be an integer.")

    def rec_power(self, base, exp): # find the base to the exponent using recursion
        if exp == 0:
            return 1

        if exp > 0:
            return base * self.rec_power(base, exp-1)          
        
    def run(self):
        self.get_input()
        print("Answer:",self.rec_power(self.base, self.exp))

    def __gt__(self, other):
        return self.exp > other.exp

    def __eq__(self, other):
        return self.exp == other.exp
    
