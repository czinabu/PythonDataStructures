'''
Author: Caleb Zinabu
Assignment: EECS 268 Lab 7
Last Modified: 07/29/2022
Description: Use Binary Trees to store and look up information on pokemon.
'''
from BNode import BNode

class Executive:
    def __init__(self, myFile):
        self.myFile = myFile
        self.fileList = []
        self.pokeList = []
        self.poke_subList = []

    def inFile(self): # Take in file and read each line into a list
        input_file = open(self.myFile, 'r')

        self.fileList = input_file.readlines()

        input_file.close()

        for i in range(len(self.fileList)):
            self.pokeList.append(self.fileList[i])

        for i in range(len(self.pokeList)):
            self.poke_subList.append(self.pokeList[i].split())

    def run(self): # run entire program
        self.inFile()
        pokeTree = PokeTree(self.poke_subList)
        pokeTree.createTree()
        pokeTree.menu()

class PokeTree: 
    def __init__(self, poke_list):
        self.poke_list = poke_list
        self.myBST = BinarySearchTree()
        self.BST_list = []
        self.copyCount = 0

    def createTree(self): # Create our binary search tree
        for i in range(len(self.poke_list)):
            self.myBST.add(self.poke_list[i])

        self.BST_list.append(self.myBST)

    def menu(self): # display menu and allow user to choose function
        choice = 0
        while choice != 5:
            print("\nWelcome to PokeTree!\n")
            print("Select an action below!")
            print("1. Search")
            print("2. Add")
            print("3. Print")
            print("4. Copy")
            print("5. Remove")
            print("6. Quit\n")
            choice = int(input("Enter a menu choice from above!: "))
            print()

            if choice == 1:
                self.search()
            elif choice == 2:
                self.add()
            elif choice == 3:
                print("\nTraversal orders:")
                print("1. Pre-order.")
                print("2. In-order.")
                print("3. Post-order.")
                t_order = int(input("Choose a traversal order: "))
                print()

                self.print(t_order, self.myBST._root)
            elif choice == 4:
                self.copy()
            elif choice == 5:
                asdf
            else:
                print("Goodbye!")

        

    def search(self): # Take in pokedex number and return corresponding pokemon
        if len(self.BST_list) > 1:
            print("\nThere are currently",len(self.BST_list),"trees.")
            list_choice = int(input("Which tree would you like to search from?: "))

        if len(self.BST_list) > 1:
            for i in range(len(self.BST_list)):
                if i == (list_choice-1):
                    targetId = input("Enter pokedex number: ")
                    print()
                    return(self.BST_list[i].search(targetId))
        else:
            targetId = input("Enter pokedex number: ")
            print()
            return(self.myBST.search(targetId))

    def add(self): # add your own pokemon to our binary search tree
        if len(self.BST_list) > 1:
            print("\nThere are currently",len(self.BST_list),"trees.")
            list_choice = int(input("Which tree would you like to add to?: "))
        
        new_pokemon = []
        for i in range(3):
            new_pokemon.append("")

        new_pokemon[0] = input("Enter your Pokemon's US name: ")
        new_pokemon[1] = input("Enter your Pokemon's Pokedex number: ")
        new_pokemon[2] = input("Enter your Pokemon's Japanese name: ")

        if len(self.BST_list) > 1:
            for i in range(len(self.BST_list)-1):
                if i == list_choice:
                    self.BST_list[i].add(new_pokemon)

    def print(self, order, entry): # print all pokemon in our binary search tree
                                   # and allow user to choose traversal order
        if order == 1:
            print(entry.entry)
            if entry.left != None:
                self.print(order, entry.left)
            if entry.right != None:
                self.print(order, entry.right)

        if order == 2:
            if entry.left != None:
                self.print(order, entry.left)
            print(entry.entry)
            if entry.right != None:
                self.print(order, entry.right)

        if order == 3:
            if entry.left != None:
                self.print(order, entry.left)
            if entry.right != None:
                self.print(order, entry.right)
            print(entry.entry)

    def copy(self): # make a copy of our binary search tree
        if self.copyCount > 1:
            print("Copy already exists.")
            return
        else:
            self.copyCount += 1
            myBST_copy = self.myBST
            self.BST_list.append(myBST_copy)
            print("Copy successfully created.")
            
    def remove(self): # remove an entry from BST based on pokedex number
        if len(self.BST_list) > 1:
            print("\nThere are currently",len(self.BST_list),"trees.")
            list_choice = int(input("Which tree would you like to remove from?: "))

class BinarySearchTree:
    def __init__(self):
        self._root = None

    def add(self, entry):
        if self._root == None:
            self._root = BNode(entry)
        else:
            return self._rec_add(entry, self._root)

    def _rec_add(self, entry, cur_node):
        if entry[1] == cur_node.entry[1]:
            raise RuntimeError()
            return
        if entry[1] < cur_node.entry[1]:
            if cur_node.left == None:
                cur_node.left = BNode(entry)
            else:
                self._rec_add(entry, cur_node.left)
        if entry[1] > cur_node.entry[1]:
            if cur_node.right == None:
                cur_node.right = BNode(entry)
            else:
                self._rec_add(entry, cur_node.right)

    def search(self, target):
        return self._rec_search(target, self._root)

    def _rec_search(self, search_key, cur_node):
        if cur_node == None:
            raise RuntimeError()
        if cur_node.entry[1] == search_key:
            print(cur_node.entry)
        if cur_node.entry[1] < search_key:
            return self._rec_search(search_key,cur_node.right)
        if cur_node.entry[1] > search_key:
            return self._rec_search(search_key,cur_node.left)

    def __lt__(self, other):
        return self._root < other._root

    def __gt__(self, other):
        return self._root > other._root
