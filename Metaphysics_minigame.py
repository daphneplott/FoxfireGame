
from random import randint
from time import sleep

def validate_guess(input, lower, upper):
    try:
        input = int(input)
        if input >= lower and input <= upper:
            return True
        else:
            print("That's not in the correct range. Please try again.")
            return False
    except:
        print("That doesn't look quite right, let's try again.")
        return False

def round1():
    """
    1 - 5 - 10
    1 - 2 - 4 . 6 - 8- 10
    1 . 3 - 4 . 6 - 7 . 9 - 10
    + 1 round
    """
    print("For round one, you have to guess a number between 1 and 10, and you only have four tries.")
    sleep(2)
    x = randint(1,10)
    count = 0
    while count < 4:
        guess = input("What is your guess? ")
        while (validate_guess(guess, 1, 10) == False):
            guess = input("What is your guess? ")
        guess = int(guess)
        if guess == x:
            print("Well done, you've guessed correctly!")
            return True
        else:
            if (guess > x):
                print("Your guess is too high.")
            else:
                print("Your guess is too low.")
            count += 1
    print("You've reached the maximum number of guesses. Let's try again.")
    return False

def round2():
    """
    1 - 25
    """
    print("For round two, you have to guess a number between 1 and 25, and you only have five tries.")
    sleep(2)
    x = randint(1,25)
    count = 0
    while count < 5:
        guess = input("What is your guess? ")
        while (validate_guess(guess, 1, 25) == False):
            guess = input("What is your guess? ")
        guess = int(guess)
        if guess == x:
            print("Well done, you've guessed correctly!")
            return True
        else:
            if (guess > x):
                print("Your guess is too high.")
            else:
                print("Your guess is too low.")
            count += 1
    print("You've reached the maximum number of guesses. Let's try again.")
    return False

def round3():
    """
    1 - 100
    """
    print("For round three, you have to guess a number between 1 and 100, and you only have seven tries.")
    sleep(2)
    x = randint(1,100)
    count = 0
    while count < 7:
        guess = input("What is your guess? ")
        while (validate_guess(guess, 1, 100) == False):
            guess = input("What is your guess? ")
        guess = int(guess)
        if guess == x:
            print("Well done, you've guessed correctly!")
            return True
        else:
            if (guess > x):
                print("Your guess is too high.")
            else:
                print("Your guess is too low.")
            count += 1
    print("You've reached the maximum number of guesses. Let's try again.")
    return False


def met_game():
    print("For today's assignment, you will have to use the power of your brain to guess a number.")
    sleep(2)
    print("Don't worry, it's not telepathy, but you only have a limited number of guesses, so choose wisely.\n")
    sleep(2)
    while(True):
        if round1():
            break
    print("You did well in round one, so let's make this just a little bit trickier.\n")
    sleep(2)
    while(True):
        if round2():
            break
    print("I'm impressed! But I bet you can do something even harder.\n")
    sleep(2)
    while(True):
        if round3():
            break   
    sleep(2)
    print("Well done! You've shown that mind is superior over matter.")
    sleep(2)
    return None
