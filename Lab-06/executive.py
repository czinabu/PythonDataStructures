'''
Author: Caleb Zinabu
Assignment: EECS 268 Lab 6
Last Modified: 07/28/2022
Code Description: Use recursion to find out which parts of a given city will
be consumed by a blob. Return result to main function.
'''

class Executive:
    def __init__(self, filename):
        self.filename = filename
        self.file_list = []
        self.numRows = 0
        self.numCols = 0
        self.startRow = 0
        self.startCol = 0
        
    def inFile(self): # read in user given file and input each file line into a list
        input_file = open(self.filename, 'r')
        self.file_list = input_file.read()
        self.file_list = self.file_list.split("\n")
        input_file.close()
        
        self.numRows = int(self.file_list[0][0])
        self.numCols = int(self.file_list[0][2])
        self.startRow = int(self.file_list[1][0])
        self.startCol = int(self.file_list[1][2])

    def checkFile(self): # check if map dimensions and blob start points are valid
        if int(self.numRows) < 1:
            raise RuntimeError("Invalid amount of rows.")
        elif int(self.numCols) < 1:
            raise RuntimeError("Invalid amount of columns.")
        elif int(self.startRow) < 0:
            raise RuntimeError("Start position out of range.")
        elif int(self.startCol) < 0:
            raise RuntimeError("Start position out of range.")
        elif int(self.startRow) > int(self.numRows):
            raise RuntimeError("Start position out of range.")
        elif int(self.startCol) > int(self.numCols):
            raise RuntimeError("Start position out of range.")
        
        
    def run(self): # run executive class and return to main
        self.inFile()
        self.checkFile()
        myCity = City(self.numRows, self.numCols, self.startRow, self.startCol, self.file_list)
        myCity.createMap()
        myCity.start_destruction()
        myCity.printCity()

class City:
    def __init__(self, numRows, numCols, startRow, startCol, file_list):
        self.file_list = file_list
        self.numRows = numRows
        self.numCols = numCols
        self.startRow = startRow
        self.startCol = startCol
        self.tempMap = []
        self.cityMap = []
        self.total = 0

    def createMap(self): # create a city map out of file contents using list implementation
        for i in range(self.numRows):
            self.tempMap.append(self.file_list[i+2])
        for i in range(self.numRows):
            self.cityMap.append(list(self.tempMap[i]))

    def printCity(self): # print map of city after blob destruction
        print(self.file_list[0])
        print(self.file_list[1])

        self.tempMap = []
        
        for i in range(self.numRows):
            self.tempMap.append(self.cityMap[i])
        
        for i in range(self.numRows):
            print(*self.tempMap[i])

        print("Total eaten:",self.total)

    def start_destruction(self): # give blob a starting position based on file input
        for i in range(self.numRows):
            for j in range(self.numCols):
                if i == self.startRow and j == self.startCol:
                    if self.is_valid_move(i,j):
                        self.destruction(i,j)

    def destruction(self, row, col): # use recursion to move blob through new map                       
        self.mark(row,col)
        self.checkSewer(row, col)

        if self.is_exit(row, col):
            return
        
        if self.is_valid_move(row-1, col):
            up_result = self.destruction(row-1, col)
            if up_result == True:
                return True
        if self.is_valid_move(row, col+1):
            right_result = self.destruction(row, col+1)
            if right_result == True:
                return True
        if self.is_valid_move(row+1, col):
            down_result = self.destruction(row+1, col)
            if down_result == True:
                return True
        if self.is_valid_move(row, col-1):
            left_result = self.destruction(row, col-1)
            if left_result == True:
                return True
        return False

    def mark(self, row, col): # Check path in front of blob, and leave mark
        if self.cityMap[row][col] != '@':
            if self.cityMap[row][col] == 'P':
                self.total += 1
            self.cityMap[row][col] = 'B'


    def is_exit(self, row, col): # Check surroundings of blob for unmarked territory
        if self.is_valid_move(row-1, col):
            return False
        elif self.is_valid_move(row, col+1):
            return False
        elif self.is_valid_move(row+1, col):
            return False
        elif self.is_valid_move(row, col-1):
            return False
        else:
            return True
        
    def checkSewer(self, row, col): # Check to see if current spot is a sewer and teleport to other sewers
        if self.cityMap[row][col] == '@':
            for i in range(self.numRows):
                for j in range(self.numCols):
                    if self.cityMap[i][j] == '@' and i > row:
                        self.destruction(i,j)
            
    def is_valid_move(self, row, col): # check if move is valid by observing current map       
        if row < 0 or row > (self.numRows-1):
            return False
        elif col < 0 or col > (self.numCols-1):
            return False
        elif self.cityMap[row][col] == 'B':
            return False
        elif self.cityMap[row][col] == '#':
            return False
        elif self.cityMap[row][col] == 'S':
            return True
        else:
            return True
