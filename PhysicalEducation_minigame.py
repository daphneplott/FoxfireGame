from time import sleep
from random import randint

def validate_guess(guess):
    if guess == "":
        return False
    if guess[0] == "h" or guess[0] == "l":
        return True
    return False

def play():
    count = 0
    x = randint(1,15)
    while count < 3:
        next = randint(1,15)
        guess = input(f"Current force: {x} ")
        while validate_guess(guess) == False:
            guess = input("Please guess 'higher' or 'lower': ")
        if next > x and guess[0] == 'h':
            print("Splotch matched!")
        elif next < x and guess[0] == "l":
            print("Splotch matched!")
        else:
            break
        count += 1
        x = next
    if count == 3:
        print("Expert splotching! You've won this match!")
        sleep(2)
        return True
    else:
        print("You've been splotched!")
        sleep(2)
        return False


def phy_game():
    print("Today, we are having our ultimate splotching match!")
    sleep(1)
    print("To hit your splotch just right, you have to correctly match your opponents force.")
    sleep(1)
    print("This force is measured on a scale 1-15, and you'll have to guess if your opponent will go higher or lower. If you do that three times, you win the round.")
    sleep(3)
    print("To win the tournament today, you just have to beat 3 out of 6 opponents. Good luck!")
    sleep(2)

    round = 1
    wins = 0

    while round < 7:
        print(f"Round {round}")
        sleep(1)
        print("Ready?")
        sleep(1)
        print("Splotch!")
        sleep(1)
        result = play()
        if result:
            wins += 1
        round +=1
        if wins == 3:
            break
        if (3 - wins) > (7 - round):
            break
    print(f"You have won {wins} rounds.")
    sleep(1)
    if wins >= 3:
        print("Well done! You've won the tournament!")
        sleep(1)
        return True
    else:
        print("Better luck next time, please come back and play again.")
        sleep(1)
        return False
    