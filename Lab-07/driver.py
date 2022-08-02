'''
Author: Caleb Zinabu
Assignment: EECS 268 Lab 7
Last Modified: 07/29/2022
Description: Prompt user for file name, pass to executive file,
and run executive file through main.
'''
from executive import Executive

def main():
    filename = input("Enter a file name: ")
    my_exec = Executive(filename)
    my_exec.run()

if __name__ == "__main__":
    main()
