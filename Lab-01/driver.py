'''
Author: Caleb Zinabu
Last Modified: 6/23/2022
Original Due Date: 6/17/2022
'''

from executive import Executive

def main(): # main function
    filename = input("Enter the name of the input file: ")
    my_exec = Executive(filename)
    my_exec.run()

if __name__ == "__main__":
    main()
