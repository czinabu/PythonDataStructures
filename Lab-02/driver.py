'''
Name: Caleb Zinabu
Last Modified: 7/1/2022
Orignal Due Date: 6/24/2022
Code Description: Simulate a CPU Scheduler using Stacks and Queues
'''
from executive import Executive

def main():
    filename = input("Enter filename: ")
    my_exec = Executive(filename)
    my_exec.run()

if __name__ == "__main__":
        main()
