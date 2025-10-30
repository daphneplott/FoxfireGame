from time import sleep
from random import randint

class PersonalityQuizQuestion:

    def __init__(self,prompt:str, answer_list:list, type_answers:list, type_points:list):
        """
        For example: ('This is a question?', [answer1, answer2, answer3],[[answer1givepointsto1,2],[answer2givespointsto3,4],[answer3givespointsto5]], [1,2,3,4,5])
        """
        self.prompt = prompt
        self.answer_list = answer_list
        self.type_answers = type_answers
        self.type_points = type_points
        self.possible_answers = "123456789"[0:len(answer_list)]

    def ask_question(self):
        print("\n"+self.prompt)
        sleep(1)
        for i in range(len(self.answer_list)):
            print(f"{"123456789"[i]}) {self.answer_list[i]}")
            sleep(.5)
        guess = input()
        while guess == "" or guess not in self.possible_answers:
            guess = input(f"Please pick an answer from 1 to {"123456789"[len(self.answer_list)-1]}: ")
        guess = int(guess)
        for item in self.type_answers[guess-1]:
            self.type_points[item-1] += 1

pointslist = [0,0,0,0,  0,0,0,0,  0,0,0,0]
# 1)Telepath, 2)Empath, 3)Vanisher, 4)Shade
# 5)Flasher, 6)Conjurer, 7)Psionopath, 8)Hydrokinetic
# 9)Pyrokinetic, 10)Froster, 11)Guster, 12)Technopath

ability_list = ['Telepath', 'Empath', 'Vanisher', 'Shade', 'Flasher', 'Conjurer', 'Psionopath', 'Hydrokinetic', 'Pyrokinetic', 'Froster', 'Guster', 'Technopath']


q1 = PersonalityQuizQuestion("What is your favorite season?",["Fall","Winter","Summer","Spring"],[[11,6],[4,10,12],[5,9,8,3],[1,2,7]],pointslist )
q2 = PersonalityQuizQuestion("What is your favorite element?",["Wind","Water","Fire","Ice","Quintessence","Shadowflux","Stellarlune"],[[11,2],[8,6],[9,12],[10],[3,5,7],[4],[1]],pointslist )
q3 = PersonalityQuizQuestion("Body, mind, heart, or soul?",["Body","Mind","Heart","Soul"],[[3,6],[1,7,12],[2,8,9,11,10],[4,5]],pointslist )
q4 = PersonalityQuizQuestion("What word best describes you?",["Rash","Whimsical","Logical","Quiet"],[[9,11,7],[8,3,5],[12,1,6],[4,2,10]],pointslist)
q5 = PersonalityQuizQuestion("What would you use your powers for?",["Social problems","Being with nature","Convenience","Protection"],[[1,2,4],[8,9,10,11],[6,5,12],[7,3]],pointslist )
q6 = PersonalityQuizQuestion("What is your favorite subject?",["Math","Physical Science","Art","Literature"],[[12,6],[8,9,10,11],[5,7,3],[2,1,4]],pointslist )
q7 = PersonalityQuizQuestion("What is your ideal vacation?",["Beach","Mountains","Theme Park","Alone"],[[8,5,9],[11,10],[12,2,3,6],[1,4,7]],pointslist )
q8 = PersonalityQuizQuestion("What is your pet peeve?",["The cold","The heat","Socializing","When people speak too bluntly"],[[9,8,5],[10,11,7],[4,3,12],[1,2,6]],pointslist )
q9 = PersonalityQuizQuestion("What is your favorite color?",["Red","Yellow","Green","Blue","Purple","Pink"],[[9,1],[5,3],[11,12],[10,8],[4,6],[2,7]],pointslist )
q10 = PersonalityQuizQuestion("What is your favorite pastime?",["Video games or movies","Socializing","Camping","Reading"],[[12,5,7],[2,6],[8,10,11,9],[3,1,4]],pointslist )
q11 = PersonalityQuizQuestion("What quality do you most want in a friend?",["Adventurous spririt","Practicality","Good listener","Willing to fight for what is right","Sense of humour","Always prepared"],[[8,11],[4,12],[2,1,5],[9,7],[3,10],[6]],pointslist)
q12 = PersonalityQuizQuestion("Which would be your first pick of a power?",["Super-spy powers","Talk to animals","Illusion","Magic blasts"],[[2,12,6],[8,10,1,2],[3,4,5],[9,11]],pointslist)
q13 = PersonalityQuizQuestion("Who is your favorite KOTLC parent?",["Edaline","Alden","Della","Juline","Cassius","Kesler"],[[6,11],[1,7],[3,5],[10,8],[2,9],[12,4]],pointslist)
q14 = PersonalityQuizQuestion("What do you want right now?",["Alone time","A fireworks show","That thing from upstairs","A listening ear","A tropical vacation","Ice cream"],[[4,12],[5,7],[6,11],[2,3],[8,9,1],[10]],pointslist)
q15 = PersonalityQuizQuestion("What role do you fill at school?",["Overacheiver","Class clown","Resourceful","Popular kid","Everyone's friend","Wallflower"],[[12,1],[11,7],[6,5],[8,9],[2,10],[3,4]],pointslist)
q16 = PersonalityQuizQuestion("You're surrounded by the Neverseen. What do you do?",["Blast them!","Use a gadget","Hide?","Get in their head","Create a distraction"],[[9,8,11],[12,6],[3,7],[1,2],[4,5,11]],pointslist)
q17 = PersonalityQuizQuestion("Which would you pick for a pet?",["Sly fox","Cuddly Husky","Wise Owl","Colorful Cameleon","Bioluminescent Jellyfish"],[[9,4],[2,10],[1,12,11],[3,6],[5,8,7]],pointslist)
q18 = PersonalityQuizQuestion("Which of these designs do you like best?",["Sparkles","Swirls","Plaid","Polka dots"],[[3,5,10],[8,9,11],[12,4,1],[6,7,2]],pointslist)
q19 = PersonalityQuizQuestion("How often do you think you'll use your power?",["Always","Very regularly","Pretty often","Sometimes","Never"],[[6,2,3],[10,8,11],[12,4,5],[7,1],[9]],pointslist)
q20 = PersonalityQuizQuestion("What is your favorite book genre?",["Romance","Mystery","Sci-Fi","Fantasy","Action","Cookbook"],[[2,8],[4,3,1],[12,7],[5],[9,11],[6,12]],pointslist)

questions = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20]

alreadyasked = []


def abi_game():
    questions = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20]
    alreadyasked = []
    print("Today we will be finding out what your ability is!") 
    sleep(2)
    round = 0
    while round < 10:
        q = questions[randint(0,len(questions)-1)]
        while q in alreadyasked:
            q = questions[randint(0,len(questions)-1)]
        alreadyasked.append(q)
        q.ask_question()
        round+=1
        sleep(.5)
    max = 0
    mat_at = 0
    for i in range(12):
        if pointslist[i] > max:
            max = pointslist[i]
            max_at = i
    print("Your ability is ...")
    sleep(2)
    print(ability_list[max_at]+"!")
    sleep(2)