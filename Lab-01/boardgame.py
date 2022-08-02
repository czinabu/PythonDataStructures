'''
Author: Caleb Zinabu
Last Modified: 6/23/2022
Original Due Date: 6/17/2022
'''

class Boardgame: # Class to handle boardgame functions
    def __init__(self):
        self.names = []
        self.years = []
        self.g_ratings = []
        self.p_ratings = []
        self.m_players = []
        self.m_playtime = []

    def listAssign(self, games_list): # Break games_list into further sublists based on categories

        for i in range(len(games_list)):

            sublist = str(games_list[i])
            sublist = sublist.split("\t")
            sublist = list(sublist)

            self.names.append(sublist[0])
            self.years.append(sublist[1])
            self.g_ratings.append(sublist[2])
            self.p_ratings.append(sublist[3])
            self.m_players.append(sublist[4])
            self.m_playtime.append(sublist[5])
            
        return self.names
        return self.years
        return self.g_ratings
        return self.p_ratings
        return self.m_players
        return self.m_playtime

    def grSorted(self, games_list): # Shows games sorted by highest Gibbons range to lowest.
        temp_list = []
        
        for i in range(len(games_list)):

            sublist = str(games_list[i])
            sublist = sublist.split("\t")
            sublist = list(sublist)

            temp_list.append(sublist)

        temp_list.sort(key = lambda temp_list: temp_list[2], reverse=True)

        temp_list = list(temp_list)

        for i in range(len(temp_list)):
            print(temp_list[i][0]+" ("+temp_list[i][1]+") "+"[GR="+temp_list[i][2]+", PR="+temp_list[i][3]+", MP="+temp_list[i][4]+", MT="+temp_list[i][5]+"]")
    
    def gamesFromYear(self, games_list): # Shows all games from user given year
        count = 0

        try:
            userYear = int(input("Enter a year: "))
        except ValueError:
            print("Year must be of type integer.")

        userYear = str(userYear)

        print("")

        for i in range(len(games_list)):

            sublist = str(games_list[i])
            sublist = sublist.split("\t")
            sublist = list(sublist)

            if(userYear == sublist[1]):
                print(sublist[0]+" ("+sublist[1]+") "+"[GR="+sublist[2]+", PR="+sublist[3]+", MP="+sublist[4]+", MT="+sublist[5]+"]")
                count += 1
            else:
                continue
        if(count == 0):
            print("No games were found in given year.")

    def rankingRange(self, games_list): # Shows all games within user given range
        try:
            userRange1 = float(input("First Value: "))
            userRange2 = float(input("Last Value: "))
        except ValueError:
            print("Invalid type.")

        print("Games within Gibbons Rankings [",userRange1,",",userRange2,"]:\n")    

        for i in range(len(games_list)):
            sublist = str(games_list[i])
            sublist = sublist.split("\t")
            sublist = list(sublist)

            if((float(sublist[2]) > userRange1) and (float(sublist[2]) < userRange2)):
                print(sublist[0]+" ("+sublist[1]+") "+"[GR="+sublist[2]+", PR="+sublist[3]+", MP="+sublist[4]+", MT="+sublist[5]+"]")

    def peopleVGibbons(self, games_list): # Shows all games with a user given difference between Gibbons Rating and People's Rating
        try:
            user_diff = float(input("Enter a number: "))
        except ValueError:
            print("Invalid type.")

        print("\nGames with ",user_diff," difference between Gibbons Rating and People's Rating: \n")

        for i in range(len(games_list)):
            sublist = str(games_list[i])
            sublist = sublist.split("\t")
            sublist = list(sublist)

            if(((float(sublist[2]) - float(sublist[3])) >= user_diff) or (float(sublist[3]) - float(sublist[2])) >= user_diff):
                print(sublist[0]+" ("+sublist[1]+") "+"[GR="+sublist[2]+", PR="+sublist[3]+", MP="+sublist[4]+", MT="+sublist[5]+"]")
                
    def playtimeRange(self, games_list): # Shows all games within a user given minimum playtime
        try:
            userMax = float(input("Enter a minimum playtime (minutes): "))
        except ValueError:
            print("Invalid type.")

        print("\nGames with ",userMax," minutes of playtime or lower: \n")

        for i in range(len(games_list)):
            sublist = str(games_list[i])
            sublist = sublist.split("\t")
            sublist = list(sublist)

            if(float(sublist[5]) <= userMax):
                print(sublist[0]+" ("+sublist[1]+") "+"[GR="+sublist[2]+", PR="+sublist[3]+", MP="+sublist[4]+", MT="+sublist[5]+"]")
                
