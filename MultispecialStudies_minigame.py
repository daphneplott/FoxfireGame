from time import sleep
from random import randint


phrase_bank = ["Not the hair, anything but the hair","Sparkles make everything better","You elves and your sparkles, bleh","There's no reason to worry",
"You must be lost","Happy shadow thoughts","Family doesn't decide who we are, we do","I go where you go","Secrets hinder my ability to protect you",
"And you're tired of watching Kenric stare at Oralie","Controlling the wind. Whoop-de-freaking-do","You'd be surprised at how powerful hope can be",
"Any openings in the nobility for a professional troublemaker?","I'm batman, so I could be your hero anyday","The only ones to refuse readings are those with darkness to hide",
"Dude, you did not just insult the hair!","What do you mean, 'mostly' on the cheek?","Hey Dex, your girlfriends are here!","Is any day less worth living simply becuase you're not going to remember it?",
"Their vanisher will never be the same","Why do clothes never have enough pockets?","Except - spoiler alert - Funkyhair never knows what he's doing",
"But we're cognates!"]

ALPHA = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt_phrase(string):
    new_string = ""
    encrypt = {}
    for char in string:
        if char.lower() not in ALPHA:
            new_string += char
        else:
            if char.lower() not in encrypt:
                encrypt[char.lower()] = alphabet[randint(0,len(alphabet)-1)]
                alphabet.remove(encrypt[char.lower()])
            if char.lower() != char:
                new_string += encrypt[char.lower()].upper()
            else:
                new_string += encrypt[char]
    return new_string

guessed_letters = []

wrong_letters = []

correct_letters = []

def print_hangman(phrase):
    string = ""
    for char in phrase:
        if char.lower() in guessed_letters:
            string += char
        elif char.lower() in ALPHA:
            string += "_"
        else:
            string += char
    print(string)
    return None

def validate_guess(string):
    if string.lower() in ALPHA:
        if string.lower() in guessed_letters:
            print("You've already guessed that, try again.")
            return False
        return True
    else:
        print("That doesn't look quite right. Please guess a letter.")
        return False


def check_done(phrase):
    for char in phrase:
        if char.lower() in ALPHA and char.lower() not in correct_letters:
            return False
    return True

def translate(completedlist:list):
    phrase = phrase_bank[randint(0,len(phrase_bank)-1)]
    while phrase in completedlist:
        phrase = phrase_bank[randint(0,len(phrase_bank)-1)]
    completedlist.append(phrase)

    encrypted_phrase = encrypt_phrase(phrase)

    while len(wrong_letters) < 5:
        done = False
        print()
        print(encrypted_phrase)
        print_hangman(phrase)
        # Print the letter in the phrase if you've guessed it, _ if a letter, the character otherwise
        print("Incorrect guesses:", wrong_letters)
        print()
        guess = input("What letter do you guess? ")
        while not validate_guess(guess):
            guess = input("What letter do you want to guess? ")
        guessed_letters.append(guess.lower())
        if guess in phrase or guess.lower() in phrase or guess.upper() in phrase:
            correct_letters.append(guess.lower())
            print("Correct")
            done = check_done(phrase)
            if done:
                break
            sleep(.5)
        else:
            print("Incorrect")
            sleep(.5)
            wrong_letters.append(guess.lower())

    if done:
        print()
        print(phrase)
        print("Well done! You've completed the translation.")
        sleep(1)
        return True
    else:
        print("Hmm. Dissapointing.")
        sleep(1)
        return False

def mul_game():
    print("This is Lady Cadence, and I have unfortunately been called in to substitute for you today.")
    sleep(2)
    print("For your assignment, you will be translating from other languages.")
    sleep(2)
    print("What? You haven't been learning that in your class?")
    sleep(2)
    print("... Fine. I'll give you some hints. You can guess letters you think are in the phrases, and I'll tell you where the letters go.")
    sleep(2)
    print("But, if you guess too many wrong letters, you will fail.\n")
    sleep(2)
    print("You'll have three languages to translate from, gnomish, ogrish, and the human language.")
    sleep(2)
    
    print("\nWe'll start with your translation from Gnomish.")
    sleep(1)

    completed = []

    result1 = translate(completed)
    
    for char in ALPHA:
        if char not in alphabet:
            alphabet.append(char)
    guessed_letters.clear()
    wrong_letters.clear()
    correct_letters.clear()
    
    print("\nNow onto Ogrish.")
    sleep(1)
    result2 = translate(completed)

    for char in ALPHA:
        if char not in alphabet:
            alphabet.append(char)
    guessed_letters.clear()
    wrong_letters.clear()
    correct_letters.clear()
    
    print("\nAnd finally, your translation from the human langauge. At least, one of them.")
    sleep(1)
    result3 = translate(completed)
    
    if result1 and result2 and result3:
        print("Well, I suppose your performance has been satisfactory. Well done.")
        sleep(2)
        return True
    else:
        print("That was ... very bad. You'll have to come back and try again.")
        sleep(2)
        return False

