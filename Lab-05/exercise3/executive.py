'''
Author: Caleb Zinabu
Assignment: EECS 268 Lab 5 Exercise 3
Last Modified: 7/21/2022
Code Description: Use a recursive method to find the fibbonaci sequence for
user given numbers, or check to see if number is part of fibbonaci sequence
'''
import math
class Executive:
    def __init__(self):
        self.mode = ''
        self.value = 0

    def get_input(self): # recieve user input
        input_list = []
        
        input_list = input("Enter mode and value: ").split()

        self.mode = input_list[0]        
        self.value = int(input_list[1])

    def check_mode(self): # check which mode user inputs
        if self.mode == "-i":
            self.fib()
        elif self.mode == "-v":
            if self.check_sequence():
                print(self.value,"is in the sequence")
            else:
                print(self.value,"is not in the sequence")
        else:
            raise ValueError("Invalid mode.")

    def fib(self):
        print(self._rec_fib(self.value))

    def _rec_fib(self, num): # return the user given number of the fibbonaci sequence
        if num == 1 or num == 0:
            return num
        else:
            return (self._rec_fib(num-2) + self._rec_fib(num-1))

    def check_sequence(self): # check if self.value is in the fibonacci sequence
        x = 0
        y = 1

        while y < self.value:
            z = x+y
            x = y
            y = z
            
        if x == self.value or y == self.value:
            return True

        if y > self.value:
            return False
        

    def run(self):
        self.get_input()
        self.check_mode()
