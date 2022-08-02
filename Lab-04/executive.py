import time
class Executive:
    def __init__(self):
        self.something = None

    def run(self):
        Calculations().chooseOp()

class Calculations:
    def __init__(self):
        self.idk = None

    def chooseOp(self):
        print("Operations to time:")
        print("1. Popping a single item from a stack")
        print("2. Popping all items from a stack")
        print("3. Queue's enqueue")
        print("4. Linked List get_entry at specifically index 0")
        print("5. Linked List get_entry at specifically the last index")
        print("6. Print all elements in a LinkedList using get_entry")
        user_choice = int(input("\nChoose an operation: "))

        if user_choice == 1:
            self.single_stackPop()
        elif user_choice == 2:
            self.all_stackPop()
        elif user_choice == 3:
            self.enqueue_time()
        elif user_choice == 4:
            self.getEntry_start_time()
        elif user_choice == 5:
            self.getEntry_end_time()
        elif user_choice == 6:
            self.getEntry_print_time()
        else:
            raise ValueError("invalid input")

    def nanosec_to_sec(self,ns):
        BILLION = 1000000000
        return ns/BILLION

    def single_stackPop(self): 
        myStack = Stack()
        size = 1000

        while(size < 100001):
            for i in range(size):
                myStack.push(i)
                
            start_time = time.perf_counter_ns()
            myStack.pop()
            end_time = time.perf_counter_ns()

            result = end_time - start_time
            print("\nTime for size: ",size)
            print("Total time in ns: ",result)
            print("Total time in sec: ",self.nanosec_to_sec(result))
            
            size += 1000

    def all_stackPop(self):
        myStack = Stack()
        size = 1000

        while(size < 100001):
            for i in range(size):
                myStack.push(i)

            start_time = time.perf_counter_ns()
            
            for i in range(size):
                myStack.pop()
                
            end_time = time.perf_counter_ns()

            result = end_time - start_time

            print("\nTime for size: ",size)
            print("Total time in ns: ",result)
            print("Total time in sec: ",self.nanosec_to_sec(result))

            size += 1000
        

    def enqueue_time(self):
        myQueue = LinkedQueue()
        size = 1000

        while(size < 100001):
            start_time = time.perf_counter_ns()
            
            for i in range(size):
                myQueue.enqueue(i)
                
            end_time = time.perf_counter_ns()

            result = end_time - start_time
                
            print("\nTime for size: ",size)
            print("Total time in ns: ",result)
            print("Total time in sec: ",self.nanosec_to_sec(result))

            size += 1000

    def getEntry_start_time(self):
        myList = LinkedList()
        size = 1000

        while(size < 100001):
            for i in range(size):
                myList.insert(i,0)

            start_time = time.perf_counter_ns()
            
            myList.get_entry(0)

            end_time = time.perf_counter_ns()

            result = end_time - start_time

            print("\nTotal time in ns: ",result)
            print("Total time in sec: ",self.nanosec_to_sec(result))

            size += 1000

    def getEntry_end_time(self):
        myList = LinkedList()
        size = 1000

        while(size < 100001):
            for i in range(size):
                myList.insert(i,i)

            start_time = time.perf_counter_ns()

            myList.get_entry(len(myList))

            end_time = time.perf_counter_ns()

            result = end_time - start_time

            print("\nTime for size: ",size)
            print("Total time in ns: ",result)
            print("Total time in sec: ",self.nanosec_to_sec(result))

            size += 1000

    def getEntry_print_time(self):
        myList = LinkedList()
        size = 1000

        while(self.size < 100001):
            for i in range(size):
                myList.insert(i,i)

        start_time = time.perf_counter_ns()

        while(size < 100001):
            for i in range(size):
                print(myList.get_entry(i))

        end_time = time.perf_counter_ns()

        result = end_time - start_time

        print("\nTotal time in ns: ",result)
        print("Total time in sec: ",self.nanosec_to_sec(result))

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
        newNode = Node(entry)
        newNode.next = self._top
        self._top = newNode

    def pop(self):
        if not self.is_empty():
            temp = self._top
            self._top = self._top.next
            return temp.entry
        else:
            raise RuntimeError()

    def peek(self):
        if not is_empty():
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
            first = Node(entry)
            self._front = first
            self._back = first
        else:
            temp = Node(entry)
            self._back.next = temp
            self._back = temp

    def dequeue(self):
        if not is_empty():
            temp = self._front
            self._front = self._front.next
            return temp.entry
        else:
            raise RuntimeError()

    def peek_front(self):
        if not is_empty():
            return self._front
        else:
            raise RuntimeError

class LinkedList:
    def __init__(self):
        self._front = None
        self._length = 0
        
    def length(self):
        return self._length
        
    def insert(self, index, entry):
        temp = Node(entry)
        first = self._front
        jumper = self._front

        if index < 0 or index > self._length:
            raise IndexError()
        if index == 0:
            temp.next = first
            first = temp
            self._length += 1
        if index == self._length:
            for i in range(index-1):
                jumper = jumper.next
            jumper.next = temp
        if index > 0 and index < self._length:
            for i in range(index-1):
                jumper = jumper.next

            new = jumper.next
            jumper.next = temp
            temp.next = new
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
