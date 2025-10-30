import time
import os
import re
from Elementalism_minigame import ele_game
from Metaphysics_minigame import met_game
from PhysicalEducation_minigame import phy_game
from AbilityDetecting_minigame import abi_game
from ElvinHistory_minigame import elv_game
from MultispecialStudies_minigame import mul_game
from Alchemy_minigame import alc_game
#from Universe_minigame import uni_game

class Building:
    
    def __init__(self, length, width):
        grid = []
        for i in range(length):
            grid.append([])
            for j in range(width):
                grid[i].append(0)
        self.grid = grid
        self.length = length
        self.width = width
        self.position = [0,0]
        """
        Length is row
        Width is columns
        """

    def set(self, input, pos):
        """
        Pos = [row, col]
        """
        if pos[0] >= self.length or pos[0] < 0:
            return False
        if pos[1] >= self.width or pos[1] < 0:
            return False
        self.grid[pos[0]][pos[1]] = input
        return True
        
    
    def get(self,pos = ["x","x"]):
        if pos == ["x","x"]:
            pos = self.position
        if pos[0] >= self.length or pos[0] < 0:
            return None
        if pos[1] >= self.width or pos[1] < 0:
            return None
        return self.grid[pos[0]][pos[1]]
    
    def __str__(self):
        string = ""
        for row in self.grid:
            for item in row:
                string += repr(item)
            string += "\n"
        return string

    def fill_in_hallways(self):
        for i in range(self.length):
            for j in range(self.width):
                if self.get([i,j]) == 0:
                    a = []
                    tmp = self.get([i,j-1])
                    if (tmp == 0) or (type(tmp) == Hallway) or (type(tmp) == Classroom and 'r' in tmp.notWalls):
                        a.append('l')
                    tmp = self.get([i,j+1])
                    if (tmp == 0) or (type(tmp) == Hallway) or (type(tmp) == Classroom and 'l' in tmp.notWalls):
                        a.append('r')
                    tmp = self.get([i-1,j])
                    if (tmp == 0) or (type(tmp) == Hallway) or (type(tmp) == Classroom and 'd' in tmp.notWalls):
                        a.append('u')
                    tmp = self.get([i+1,j])
                    if (tmp == 0) or (type(tmp) == Hallway) or (type(tmp) == Classroom and 'u' in tmp.notWalls):
                        a.append('d')
                    self.set(Hallway(self, i, j, notWalls = a), [i,j])
        return None

    def change_pos(self, row_change, col_change):
        self.position[0] += row_change
        self.position[1] += col_change
        return None
    
class Space:

    roomtype = "None"

    def __init__(self, building:Building, row, col, notWalls:list):
        self.notWalls = notWalls
        self.row = row
        self.col = col
        self.building = building
        

    def __str__(self):
        go = ""
        count = 0
        for item in self.notWalls:
            if item == "l":
                go += f"left into a {self.building.get([self.row,self.col-1]).roomtype}"
            if item == "r":
                go += f"right into a {self.building.get([self.row,self.col+1]).roomtype}"
            if item == "u":
                go += f"up into a {self.building.get([self.row-1,self.col]).roomtype}"
            if item == "d":
                go += f"down into a {self.building.get([self.row+1,self.col]).roomtype}"
            count +=1
            if count < len(self.notWalls):
                go += ", and "
        return f"You are in a {self.roomtype}, and you can go {go}."

class  Hallway(Space):
    
    roomtype = "hallway"

    def __init__(self, building:Building, row, col, notWalls = ['l','r','u','d']):
        super().__init__(building, row,col, notWalls)    

    def __repr__(self):
        if self.building.position == [self.row,self.col]:
            return "  *  "
        return "     "
    
class Classroom(Space):

    def __init__(self, name, building, row, col, minigame, notWalls):
        self.name = name
        super().__init__(building,row, col,notWalls)
        self.roomtype = name + " classroom"
        self.minigame = minigame

    def __repr__(self):
        string = self.name[0:3]
        if self.building.position == [self.row,self.col]:
            string = self.name[0:2] + "*"
        if "l" not in self.notWalls:
            string = "|" + string
        else:
            string = " " + string
        if "r" not in self.notWalls:
            string = string + "|"
        else:
            string = string + " "
        if "u" not in self.notWalls:
            string = f"\033[53m{string}\033[0m"
        if "d" not in self.notWalls:
            string = f"\033[4m{string}\033[0m"
        return string
        
def move_check(input, building:Building):
    if input == "":
        return False
    if input == "I'm done":
        return True
    if input == "Play again":
        return True
    if input == "Save progress":
        return True
    return input[0] in building.get().notWalls


# Get the directory of the current script
current_folder = os.path.dirname(os.path.abspath(__file__))

# Reference a file in the same folder
saveprogressfile = os.path.join(current_folder, 'saveprogress.txt')


schedule1 = "          \033[4m|Monday       | Tuesday           |Wednesday     |Thursday          |Friday               \033[0m\n"
schedule2 = "Morning   |Elementalism |Physical Education |Elvin History |Physical Eduction |Metaphysics          \n"
schedule3 = "Afternoon |Universe     |Ability Detecting  |Alchemy       |Ability Detecting |Multispecial Studies \n"
schedule = schedule1 + schedule2 + schedule3



def Ele_minigame(badges):
    print("Welcome to Elementalism! Let's look at our assignment.")
    time.sleep(2)
    ele_game()
    if "Ele" not in badges:
        badges.append("Ele")
    return None

def Uni_minigame(badges):
    print("Welcome to the Universe! Let's look at our assignment.")
    time.sleep(2)
    #uni_game()
    print("This can be a pretend Universe game......... :(")
    if "Uni" not in badges:
        badges.append("Uni")
    return None

def Alc_minigame(badges):
    print("Welcome to Alchemy! Let's look at our assignment.")
    time.sleep(2)
    alc_game()
    if "Alc" not in badges:
        badges.append("Alc")
    return None

def Met_minigame(badges):
    print("Welcome to Metaphysics! Let's look at our assignment.")
    time.sleep(2)
    met_game()
    if "Met" not in badges:
        badges.append("Met")
    return None

def Elv_minigame(badges):
    print("Welcome to Elvin History! Let's look at our assignment.")
    time.sleep(2)
    result = elv_game()
    if result and "Elv" not in badges:
        badges.append("Elv")
    return None

def Phy_minigame(badges):
    print("Welcome to Physical Education! Let's look at our assignment.")
    time.sleep(2)
    result = phy_game()
    if result and "Phy" not in badges:
        badges.append("Phy")
    return None

def Loc_minigame(badges):
    print("Welcome to the locker room. Let's go play a game in Physical Education.")
    time.sleep(2)
    return None

def Abi_minigame(badges):
    print("Welcome to Ability Detecting! Let's look at our assignment.")
    time.sleep(2)
    abi_game()
    if "Abi" not in badges:
        badges.append("Abi")
    return None

def Mul_minigame(badges):
    print("Welcome to Multispecial Studies! Let's look at our assignmnet.")
    time.sleep(2)
    result = mul_game()
    if result and "Mul" not in badges:
        badges.append("Mul")
    return None



def game():
    os.system("cls")
    Foxfire = Building(4,5)
    """
    [1,0,1,0,1] [r, d, l]
    [1,0,0,0,1] [d, l]
    [0,1,1,0,1] [u, u, l]
    [0,0,0,0,1] [l]
    """
    #Create Foxfire
    Foxfire.set(Classroom("Elementalism",Foxfire,0,0, Ele_minigame, ['r']),[0,0])
    Foxfire.set(Classroom("Universe",Foxfire,0,2, Uni_minigame,['d']),[0,2])
    Foxfire.set(Classroom("Alchemy",Foxfire,0,4, Alc_minigame,['l']),[0,4])
    Foxfire.set(Classroom("Metaphysics",Foxfire, 1,0, Met_minigame,['d']),[1,0])
    Foxfire.set(Classroom("Elvin History",Foxfire,1,4,Elv_minigame, ['l']),[1,4])
    Foxfire.set(Classroom("Physical Education",Foxfire,2,1, Phy_minigame,['r']),[2,1])
    Foxfire.set(Classroom("Locker Room",Foxfire,2,2, Loc_minigame,['u','l']),[2,2])
    Foxfire.set(Classroom("Ability Detection",Foxfire,2,4, Abi_minigame,['l']),[2,4])
    Foxfire.set(Classroom("Multispecial Studies",Foxfire,3,4, Mul_minigame, ['l']),[3,4])
    Foxfire.fill_in_hallways()
    Foxfire.position = [3,3]
    badges = []

    #Intro
    cont = input("Would you like to continue a game, or start a new one? Please enter 'c' to continue, or 'n' to start a new game: ")
    if cont == "c":
        with open(saveprogressfile) as file:
            contname = input("What is your saved name? ")
            for line in file:
                match = re.match(rf"^{contname}.*$",line)
                if match != None:
                    split_str = match.string.split(";")
                    badges = split_str[1:len(split_str)-1]
        if badges == []:
            print("Name not found, let's start a new game!")
            time.sleep(2)
        else:
            print(f"Here are the classes you have completed so far: {badges}")
            time.sleep(4)
    else:
        print("Okay, let's start a new game!")
        time.sleep(2)
    
    os.system("cls")

    print("Welcome to Foxfire!")
    time.sleep(2)
    print("We're so glad to have you here, let's get you started.")
    time.sleep(2)
    print("\nHere's your schedule:")
    time.sleep(1)
    print(schedule)
    time.sleep(5)
    print("\nComplete the activities in every class to graduate.")
    time.sleep(1)
    print("\nYou can move around the school using l/r/u/d. Additionally, you can save the game by typing 'Save progress'. You can retry an assignment by coming back to the room, or by typing 'Play again'. If you want to quit, type 'I'm done'.")
    time.sleep(4)
    print("\nGood luck!\n\n")
    time.sleep(2)

    #Move Loop
    while(True):
        if "Ele" in badges and "Uni" in badges and "Alc" in badges and "Met" in badges and "Elv" in badges and "Phy" in badges and "Abi" in badges and"Mul" in badges:
            print("\nCongratulations! You've finished a successful year at Foxfire!\n")
            if cont == "c":
                string = ""
                with open(saveprogressfile,'r') as file:
                    for line in file:
                        if line.split(";")[0] != contname:
                            string += line
                with open(saveprogressfile,'w') as file:
                    file.write(string)
            break
        print(Foxfire)
        print(Foxfire.get())
        move = input("Where would you like to go? ")
        while (move_check(move, Foxfire) ==False):
            move = input("That doesn't look quite right. Where would you like to go? ")
        if move == "I'm done":
            break
        if move == "Save progress":
            if cont == "c":
                string = ""
                with open(saveprogressfile,'r') as file:
                    for line in file:
                        if line.split(";")[0] != contname:
                            string += line
                with open(saveprogressfile,'w') as file:
                    file.write(string)
                name = contname
            else:
                name = input("What is your name? ")
                while name == "":
                    name = input("What is your name? ")
            file = open(saveprogressfile,'a')
            string = ""
            for item in badges:
                string += item
                string += ';'
            file.write(f"\n{name};{string}\n")
            file.close()
            break
        if move == "Play again":
            pass
        if move[0] == "l": 
            Foxfire.change_pos(0,-1)
        if move[0] == "r":
            Foxfire.change_pos(0,1)
        if move[0] == "d":
            Foxfire.change_pos(1,0)
        if move[0] == "u":
            Foxfire.change_pos(-1,0)
        if type(Foxfire.get()) == Classroom:
            Foxfire.get().minigame(badges)

game()   
