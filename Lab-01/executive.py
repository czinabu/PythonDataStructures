'''
Author: Caleb Zinabu
Last Modified: 6/23/2022
Original Due Date: 6/17/2022
'''

from boardgame import Boardgame

class Executive: # Class to handle organization and running of program
    def __init__(self, filename):
        self.filename = filename
        self.games_list = []

    def inFile(self, filename): # Read in file and assign each line to an index in list
        input_file = open(filename, 'r')

        games = input_file.read()

        self.games_list = games.split("\n")

        input_file.close()

        Boardgame().listAssign(self.games_list)

        return self.games_list

    def run(self): # executes functions in Executive class
        self.inFile(self.filename)
        Menu().displayMenu(self.games_list)

class Menu: # Class to handle menu functions
    def __init__(self):
        self.userChoice = 0

    def displayMenu(self, games_list): # displays menu choices and returns a user given choice
        while(self.userChoice != 6):
            print("\nBOARDGAMES!\n")
            print("1. Print all games highest Gibbons range to lowest.\n")
            print("2. Print all games from a year.\n")
            print("3. Print a ranking range.\n")
            print("4. The People VS Dr. Gibbons\n")
            print("5. Print based on playtime.\n")
            print("6. Exit the program.\n")

            self.userChoice = int(input("Select a number for your choice: "))
            print("")

            self.menuChoice(self.userChoice, games_list)

        if(self.userChoice == 6):
            print("Exiting program... Goodbye!\n")


    def menuChoice(self, userChoice, games_list): # calls a boardgame function based on user given choice
        if(userChoice == 1):
            Boardgame().grSorted(games_list)
        elif(userChoice == 2):
            Boardgame().gamesFromYear(games_list)
        elif(userChoice == 3):
            Boardgame().rankingRange(games_list)
        elif(userChoice == 4):
            Boardgame().peopleVGibbons(games_list)
        elif(userChoice == 5):
            Boardgame().playtimeRange(games_list)
