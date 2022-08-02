class Executive:
    def __init__(self, filename):
        self.filename = filename
        self.fileList = []
        self.temp_list = []

    def inFile(self, filename):
        input_file = open(filename, 'r')

        self.fileList = input_file.read()
        self.fileList = self.fileList.split("\n")

        input_file.close()

        return self.fileList
    
    def checkFile(self): # checks command and calls appropriate functtion       
        for i in range(len(self.fileList)):
            self.temp_list.append(self.fileList[i].split())
            
            if(self.temp_list[i][0] == 'NAVIGATE'):
                Browser().navigate_to(self.temp_list[i][1])
            elif(self.temp_list[i][0] == 'BACK'):
                asdf
            elif(self.temp_list[i][0] == 'FORWARD'):
                asdf
            elif(self.temp_list[i][0] == 'HISTORY'):
                Browser().history()
            else:
                raise ValueError("Invalid command.")
        
    def run(self):
        self.inFile(self.filename)
        self.checkFile()

class Node:
    def __init__(self, entry):
        self.entry = entry
        self.next = None

class LinkedList:
    def __init__(self):
        self._front = None
        self._length = 0
        
    def length(self):
        return self._length
        
    def insert(self, index, entry):
        new = Node(entry)
        temp = self._front
        jumper = self._front

        if index < 0 or index > self._length:
            raise IndexError()
        if index == 0:
            temp.next = self._front
            self._front = temp
            self._front.next = temp
            self._length += 1
        if index > 0 and index <= self._length:
            for i in range(index-1):
                jumper = jumper.next

            temp = jumper.next
            jumper.next = new
            new.next = temp
            self._length += 1
        
    def remove(self, index):
        jumper = self._front
        
        if index == 0:
            first = self._front
            self._front = self._front.next
        elif index > 0 or index < self._length-1:
            for i in Range(index-1):
                jumper = jumper.next
            new = jumper.next
            jumper.next = jumper.next.next
        elif index == self._length-1:
            for i in Range(index-1):
                jumper = jumper.next
            jumper.next = none
        else:
            raise IndexError()
        
    def get_entry(self, index):
        jumper = self._front
        for i in range(index):
            jumper = jumper.next
            if jumper == none:
                raise IndexError()
            else:
                continue
        return jumper.entry
        
    def set_entry(self, index):
        jumper = self._front

        for i in range(index-1):
            jumper = jumper.next
        self.entry
        
    def clear(self):
        self._front = None
        self._length = 0

class Browser:
    def __init__(self):
        self.myBrowser = LinkedList()
    def navigate_to(self, url):
        self.myBrowser.insert(self.myBrowser.length(),url)
    def forward(self):
        asdf
    def back(self):
        asdf
    def history(self):
        print("Oldest\n")
        print("===========\n")

        for i in range(self.myBrowser.length()):
            print(i,self.myBrowser.get_entry())

        print("===========\n")
        print("Newest\n")
