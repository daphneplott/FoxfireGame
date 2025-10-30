

#In this game, you have to uncover and match names of constellations (Maybe to their pictures someday if byuimage will load). 
# There are 8 such constellations
# Orion, Big Dipper, Leo, Pegasus, Cygnus, Monoceros (unicorn), Cassiopeia, Draco

from byuimage import Image
from random import randint


#Create the constellation images
orion = Image("FoxfireGame/ConstellationImages/OrionConstellation.jpg")
bigdipper = Image("FoxfireGame/ConstellationImages/BigDipperConstellation.jpg")
cassiopeia = Image("FoxfireGame/ConstellationImages/CassiopeiaConstellation.jpg")
cygnus = Image("FoxfireGame/ConstellationImages/CygnusConstellation.jpg")
draco = Image("FoxfireGame/ConstellationImages/DracoConstellation.jpg")
hydra = Image("FoxfireGame/ConstellationImages/HydraConstellation.jpg")
unicorn = Image("FoxfireGame/ConstellationImages/MonocerosConstellation.jpg")
pegasus = Image("FoxfireGame/ConstellationImages/PegasusConstellation.jpg")

orion_name = "Orion, the hunter"
bigdipper_name = "Big Dipper, the bear"
cassiopeia_name = "Cassiopeia, the vain queen"
cygnus_name = "Cygnus, the swan"
draco_name = "Draco, the dragon"
hydra_name = "Hydra, the sea serpent"
unicorn_name = "Monoceros, the Unicorn"
pegasus_name = "Pegasus, the winged horse"


def create_grid(list):
    """
    List should contain 16 elements, 8 images and 8 names
    """
    grid = {}
    alreadydone = []
    for i in range(1,17):
        x = randint(0,15)
        while x in alreadydone:
            x = randint(0,15)
        grid[i] = list[x]
        alreadydone.append(x)
    return grid

def show(list):
    print(f"{list[0]}    {list[1]}    {list[2]}    {list[3]}")
    print(f"{list[4]}    {list[5]}    {list[6]}    {list[7]}")
    print(f"{list[8]}   {list[9]}   {list[10]}   {list[11]}")
    print(f"{list[12]}  {list[13]}   {list[14]}   {list[15]}")
    return None

gridrep =[i+1 for i in range(16)]

grid = create_grid([bigdipper,bigdipper_name,cassiopeia,cassiopeia_name,cygnus,cygnus_name,draco,draco_name,hydra,hydra_name,unicorn,unicorn_name,orion,orion_name,pegasus,pegasus_name])

alreadyfound = []

def validateguess(guess):
    if isinstance(guess, int):
        if 0<guess and guess<17:
            if guess in alreadyfound:
                print("You've already found that image! Let's try again with a new square.")
                return False
            else:
                return True
        elif guess > 16:
            print("Oops! That number's too high! Please try again.")
            return False
        elif guess < 1:
            print("Oops! That number's too low! Please try again.")
            return False
    else:
        print("That guess doesn't look quite right. Please try again.")
        return False
    
def allguessed(lst):
      a = 0
      for element in lst:
        if element == "_" or element == " _" or element == "_ ":
          a += 1
      if a == 16:
        return True
      else:
        return False

def maketwoguesses():
    myguess1 = input("What sqaure would you like to look under? ")
    try:
        myguess1 = int(myguess1)
    except:
        pass
    while validateguess(myguess1) == False:
        myguess1 = input("What square would you like to look under? ")
        try:
            myguess1 = int(myguess1)
        except:
            pass
    
    if type(grid[myguess1]) == str:
        print(grid[myguess1])
    else:
        grid[myguess1].show()
    
    guess2good = False
    while guess2good == False:
        myguess2 = input("What square would you like to look under next? ")
        try:
            myguess2 = int(myguess2)
        except:
            pass
        while validateguess(myguess2) == False:
            myguess2 = input("What square would you like to look under next? ")
            try:
                myguess2 = int(myguess2)
            except:
                pass
        if myguess2 == myguess1:
            print("You just guessed that number! Try picking a new one." )
        else:
            guess2good = True

    if type(grid[myguess2]) == str:
        print(grid[myguess2])
    else:
        grid[myguess2].show()
    return myguess1, myguess2

whatmatches = {orion_name:orion, bigdipper_name:bigdipper, cassiopeia_name:cassiopeia,cygnus_name:cygnus,draco_name:draco,hydra_name:hydra,unicorn_name:unicorn,pegasus_name:pegasus}

def matchguesses(myguess1, myguess2):
    match = False

    if type(grid[myguess1]) != type(grid[myguess2]):
        if type(grid[myguess1]) == str:
            if whatmatches[grid[myguess1]] == grid[myguess2]:
                match = True
        else:
            if whatmatches[grid[myguess2]] == grid[myguess1]:
                match = True

    if match:
        print("You have matched a constellation!")
        if myguess1 < 10:
            gridrep[myguess1 -1] = "_"
        elif myguess1 == 13:
            gridrep[myguess1 -1] = "_ "
        else:
            gridrep[myguess1 -1] = " _"
        
        if myguess2 < 10:
            gridrep[myguess2 -1] = "_"
        elif myguess2 == 13:
                gridrep[myguess2 -1] = "_ "
        else:
            gridrep[myguess2 -1] = " _"
        alreadyfound.append(myguess1)
        alreadyfound.append(myguess2)
        return True
    else:
        print("Hmm... Not a match.")
        return False

def uni_game():
    print("For this assignment, you will be matching constellations.")

    show(gridrep)

    while allguessed(gridrep) == False:
        myguess1, myguess2 = maketwoguesses()
        matchguesses(myguess1, myguess2)
            
        show(gridrep)

    print("\nWell done! You have completed your Universe assignment!")

    return None
