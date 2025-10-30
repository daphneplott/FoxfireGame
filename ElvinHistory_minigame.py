from random import randint
from time import sleep

class TriviaQuestion:

    def __init__(self,prompt, answer_list, correct_answer):
        self.prompt = prompt
        self.answer_list = answer_list
        self.correct_answer = correct_answer
        self.possible_answers = "abcdefghijklmnop"[0:len(answer_list)]

    def ask_question(self):
        print("\n"+self.prompt)
        for i in range(len(self.answer_list)):
            sleep(.5)
            print(f"{"abcdefghij"[i]}) {self.answer_list[i]}")
        guess = input()
        while guess == "" or guess not in self.possible_answers:
            guess = input(f"Please pick an answer from a to {"abcdefghij"[len(self.answer_list)-1]}: ")
        if guess == self.correct_answer:
            print("Correct!")
            sleep(1)
            return True
        else:
            print("Incorrect")
            sleep(1)
            return False

q1 = TriviaQuestion("In what book does Sophie manifest as an enhancer?",["Neverseen","Nightfall","Lodestar","Flashback"],"c")
q2 = TriviaQuestion("Whos is the boy who disapeared?", ["Alvar", "Fitz", "Ruy", "Gethen"],'a')
q3 = TriviaQuestion("What is the name of Fitz's stuffed animal?",["Mr Stinkbottom","Mr Snuggles","Mrs Sassyfur","Mr Sparkles"],'b')
q4 = TriviaQuestion("What is Physic's real name?",["Elwin","Mr Forkle","Lady Cadence","Livvy"],'d')
q5 = TriviaQuestion("Which of these is not a Goblin bodygaurd?",["Cadfael","Woltzer","Grizel","Cadoc","Lovise","Brielle"],'a')
q6 = TriviaQuestion("Who was Sophie's first kiss?",["Fitz","Keefe","Dex","Tam","Hasn't happened yet"],'c')
q7 = TriviaQuestion("How are Maruca and Wylie related?",["Siblings","Cousins","Distant cousins","They aren't related"],'b')
q8 = TriviaQuestion("Who is the council's spokesperson?",["Bronte","Terik","Kenric","Emery"],'d')
q9 = TriviaQuestion('Who did Alden date before Della?',["Edaline","Juline","Alina","Gisella"],'c')
q10 = TriviaQuestion("What color are Keefe's eyes?",["Dark blue","Teal blue","Sky blue","Icy blue"],'d')
q11 = TriviaQuestion("What is Keefe's middle name?",["Cassius","Irwin","Avery","Elroy"],'b')
q12 = TriviaQuestion("What unmapped star did Sophie illegally bottle?",["Marquiseire","Candesia","Lucillant","Phosforien",
                    "Nightfall","Elementine","Quintessence"],'f')
q13 = TriviaQuestion("What color do elves wear to plantings?",["Green","Black","Blue","Yellow","White"],'a')
q14 = TriviaQuestion("Which of these is not a gadget that Dex made?",["Panic switch rings","Sucker Punch","Ability Restrictor",
                    "Enhancing blocking crush cuffs","Enhancing blocking fingernails","Twiggler","Solar-powered Ipod"], 'e')
q15 = TriviaQuestion("What are the baby Alicorns' names?",["Twilight and Star","Sol and Luna","Luna and Wynn","Velvet and Shimmer"],'c')
q16 = TriviaQuestion("What did Tam and Linh dye their hair with?",["Hair-changing potions","Their registry pendants","Magical vanity mirror","Floral dyes","Human hair dye"],'b')
q17 = TriviaQuestion("What is Biana's Team Valiant mascot?",["Unicorn","Yeti","Selkie","Kelpie"],'d')
q18 = TriviaQuestion("What two abiliites can comine to create illusions?",["Shade and Flasher","Flasher and Guster","Telepathy and Empath","Empath and Shade"],'a')
q19 = TriviaQuestion("What is Calla's famous dish?",["Mallowmelt","Starkflower Stew","Ripplepuffs","Cinnacreme"],'b')
q20 = TriviaQuestion("What special ability is banned?",["Telepathy","Guster","Hydrokinetic","Shades","Pyrokinetic","Inflictor"],'e')

questions = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20]

alreadyasked = []

def elv_game():
    questions = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20]
    alreadyasked = []
    print("For this assignment, you will be taking a history quiz. There will be ten questions, and you need to score 80"+"%"+" or higher to pass.") 
    sleep(2)
    round = 0
    correct = 0
    while round < 10:
        q = questions[randint(0,19)]
        while q in alreadyasked:
            q = questions[randint(0,19)]
        alreadyasked.append(q)
        result = q.ask_question()
        if result:
            correct += 1
        round+=1
    if correct >= 8:
        print(f"You scored {correct}/10. Well done! You have passed your test!")
        sleep(2)
        return True
    else:
        print(f"You scored {correct}/10. Please come back later to retake the test.")
        sleep(2)
        return False
