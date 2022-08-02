'''
Author: Caleb Zinabu
Assignment: EECS 268 Lab 6
Last Modified: 07/28/2022
Code Description: Prompt user for file name, pass to executive file,
and run executive file through main.
'''
from executive import Executive

def main():
    filename = input("Please enter file name: ")
    my_exec = Executive(filename)
    my_exec.run()

if __name__ == "__main__":
    main()
 
