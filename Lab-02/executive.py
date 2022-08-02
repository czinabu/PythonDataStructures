'''
Name: Caleb Zinabu
Last Modified: 7/1/2022
Orignal Due Date: 6/24/2022
Code Description: Simulate a CPU Scheduler using Stacks and Queues
'''

class Executive: # handle file input and running of program
    def __init__(self, filename):
        self.filename = filename
        self.fileList = []

    def inFile(self, filename):
        input_file = open(filename, 'r')

        self.fileList = input_file.read()
        self.fileList = self.fileList.split("\n")

        input_file.close()

        return self.fileList

    def run(self):
        self.inFile(self.filename)
        Process().checkProcess(self.fileList)
class Process: # check file for command and add/remove Processes from Queue
    def __init__(self):
        self.fileList = []
        self.temp_list = []
        self.processStack = None
        self.processName = None

    def checkProcess(self, fileList): # checks command and calls appropriate functtion
        myScheduler = LinkedQueue()
        
        for i in range(len(fileList)):
            self.temp_list.append(fileList[i].split())
            
            if(self.temp_list[i][0] == 'START'):
                myScheduler = self.startProcess(self.temp_list[i][1], myScheduler)                
            elif(self.temp_list[i][0] == 'CALL'):
                Scheduler().processCall(self.temp_list[i][1], myScheduler)
            elif(self.temp_list[i][0] == 'RETURN'):
                Scheduler().returnProcess(myScheduler)
            else:
                raise ValueError("Invalid command.")
            
    def startProcess(self, name, myScheduler): # create process and add to queue
        self.processStack = Stack()
        self.processName = name

        Scheduler().addtoQueue(self.processStack, name, myScheduler)

        return myScheduler

class Scheduler: # Create queue and allow user to add, remove, or return stack
    def __init__(self):
        self.myScheduler = LinkedQueue()
        
    def addtoQueue(self, process, name, myScheduler):
        myScheduler.enqueue(process)
        print(name,"added to queue")
        #print(name,"is: ",process)

        return myScheduler
        
    def processCall(self, func, myScheduler):  # add function to process' call stack    
        front_process = myScheduler.dequeue()
        print(front_process,"calls ",func)
        front_process.push(func)
        myScheduler.enqueue(front_process)

        return myScheduler
        
    def returnProcess(self, myScheduler): # remove functions from process' call stack, or remove process from queue
        front_process = myScheduler.dequeue()

        if front_process._top == None:
            print(front_process,"returns from main.")
            print(front_process,"process has ended")
        else:
            func = front_process.pop()
            print(func)
            myScheduler.enqueue(front_process)
            print(front_process," added back to queue")

            return func
        
class Node:
    def __init__(self, entry):
        self.entry = entry
        self.next = None

class Stack:
    def __init__(self):
        self._top = None

    def is_empty(self):
        if self._top == None:
            return True
        else:
            return False

    def push(self, entry):
        node = Node(entry)
        node.next = self._top
        self._top = node

    def pop(self):
        if self.is_empty() == False:
            temp = self._top
            self._top = self._top.next
            return temp.entry
        else:
            raise RuntimeError()

    def peek(self):
        if self.is_empty() == False:
            return self._top
        else:
            raise RuntimeError()

class LinkedQueue:
    def __init__(self):
        self._front = None
        self._back = None

    def is_empty(self):
        if self._front == None:
            return True
        else:
            return False

    def enqueue(self, entry):
        if self._front == None:
            new = Node(entry)
            self._front = new
            self._back = new
        else:
            new = Node(entry)
            self._back.next = new
            self._back = new

    def dequeue(self):
        if self.is_empty() == False:
            temp = self._front
            self._front = self._front.next
            return temp.entry
        else:
            raise RuntimeError()

    def peek_front(self):
        if self.is_empty() == False:
            temp = self._front
            return temp.entry
        else:
            raise RuntimeError()
