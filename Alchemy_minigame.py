from random import randint, shuffle
from time import sleep

class Ingredient:

    def __init__(self, name, effect_type, effect):
        # ex: Ingredient("Gold dust","color","gold")
        self.name = name
        self.effect_type = effect_type
        self.effect = effect

    def __str__(self):
        return self.name
    
    def __repr(self):
        return self.name
    
    def __eq__(self,other):
        if type(other) != Ingredient:
            return False
        if self.name == other.name and self.effect_type == other.effect_type and self.effect == other.effect:
            return True
        return False

class Elixer:
    def __init__(self, in1:Ingredient, in2:Ingredient, in3:Ingredient, name = "Unknown"):
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.name = name
        self.inglist = [in1.name, in2.name, in3.name]

    def __str__(self):
        return f"This elixer has {self.in1.effect_type} {self.in1.effect}, {self.in2.effect_type} {self.in2.effect}, and {self.in3.effect_type} {self.in3.effect}."

    def __eq__(self, other):
        if type(other) != Elixer:
            return False
        if self.in1 == other.in1 and self.in2 == other.in2 and self.in3 == other.in3:
            return True
        return False
    

#Ingredients

flareadonfur = Ingredient("Flareadon Fur","color","gold")
unicornhorn = Ingredient("Unicorn Horn","color","silver")
dragonscale = Ingredient("Dragon Scale","color","green")
rosepetal = Ingredient("Rose Petal","color","pink")
pegasushair = Ingredient("Pegasus Hair","color","blue")
lavender = Ingredient("Lavender","color","purple")
lemonpeal = Ingredient("Lemon Peal","color","yellow")
autumnleaf = Ingredient("Autumn Leaf","color","red")
pumpkinseeds = Ingredient("Pumpkin Seeds","color","orange")
yetifur = Ingredient("Yeti Fur","color","white")
murcatscales = Ingredient("Murcat Scales","color","purple, orange, and teal")
ritzcrackers = Ingredient("Ritz Crackers","color","teal")

eucalyptusoil = Ingredient("Eucalyptus Oil","is","thin")
milkweedsap = Ingredient("Milkweed Sap","is","smooth")
mirrorshard = Ingredient("Mirror Shard","is","metallic")
tredgeoncarapace = Ingredient("Tredgeon Carapace","is","iridescent")
honey = Ingredient("Honey","is","thick")
manticoretail = Ingredient("Manticore Tail","is a","powder")
unicorntears = Ingredient("Unicorn Tears","is","translucent")
dawnlings = Ingredient("Dawnlings","smells","sweet")
bluewheat = Ingredient("Blue Wheat","is a","salve")
selkyskin = Ingredient("Selky Skin","is","opaque")
kelpieskin = Ingredient("Keplie Skin","is","sparkly")
flickerwing = Ingredient("Flickerwing","it","glows")

pookapus = Ingredient("Pooka Pus","has an effect of","cell regeneration")
kelpiedung = Ingredient("Kelpie Dung","has an effect of","painkiller")
pheonixsweat = Ingredient("Pheonix Sweat","has an effect of","burn ointment")
jaculusvenom = Ingredient("Jaculus Venom","has an effect of","minor healing")
bottledrainbow = Ingredient("Bottled Rainbow","has an effect on","hair color")
chamuleaves = Ingredient("Chamu Leaves","has an effect on","hair texture")
irilenenectar = Ingredient("Irilene Nectar","has an effect on","eye color")
amarallitine = Ingredient("Amarallitine","has an effect on","transmuting metals")
ruckleberries = Ingredient("Ruckleberries","has an effect on","purifying metals")
bennufeathers = Ingredient("Bennu Feathers","has an effect of","extinguishing fires")
slumberberries = Ingredient("Slumberberries","is a","sedative")
sirenwhiskers = Ingredient("Siren Whiskers","has an effect on","the mouth and throat")


#Elixers

abrasionpersuasion = Elixer(pumpkinseeds,milkweedsap,pookapus,"Abrasion Persuasion")
acheybreak = Elixer(yetifur,honey,kelpiedung,"Achey-Break")
blisterblast = Elixer(autumnleaf,selkyskin,kelpiedung,"Blister Blast")
bruisecruise = Elixer(pegasushair,bluewheat,jaculusvenom,"Bruise Cruise")
burnout = Elixer(lemonpeal,bluewheat,pheonixsweat,"Burn Out")
woundwipe = Elixer(lavender,bluewheat,jaculusvenom,"Would Wipe")
floof = Elixer(lemonpeal,tredgeoncarapace,chamuleaves,"Floof")
browneyesolidaritea = Elixer(flareadonfur,selkyskin,irilenenectar,"Brown-eye Solidari-tea")
greenleaf = Elixer(dragonscale,eucalyptusoil,bottledrainbow,"Greenleaf")
lovelylocks = Elixer(rosepetal,flickerwing,chamuleaves,"Lovely Locks")
mermaidtigerdelight = Elixer(murcatscales,kelpieskin,bottledrainbow,"Mermaid Tiger Delight")
seasee = Elixer(ritzcrackers,kelpieskin,irilenenectar,"Sea See")
goldtransmutation = Elixer(flareadonfur,mirrorshard,amarallitine,"Gold Transmutation")
silvertransmutation = Elixer(unicornhorn,mirrorshard,amarallitine,"Silver Transmutation")
ironpurification = Elixer(autumnleaf,tredgeoncarapace,ruckleberries,"Iron Purification")
hushslush = Elixer(lavender,honey,sirenwhiskers,"Hush Slush")
droolydew = Elixer(yetifur,eucalyptusoil,sirenwhiskers,"Drooly Dew")
quicksnuff = Elixer(dragonscale,manticoretail,bennufeathers,"Quicksnuff")
fadefuel = Elixer(pegasushair,unicorntears,pookapus,"Fade Fuel")
slumberberrytea = Elixer(rosepetal,dawnlings,slumberberries,"Slumberberry Tea")


full_ingredient_list1 = [flareadonfur,unicornhorn,dragonscale,rosepetal,pegasushair,lavender,lemonpeal,autumnleaf,pumpkinseeds,yetifur,murcatscales,ritzcrackers]
full_ingredient_list2 = [eucalyptusoil,milkweedsap,mirrorshard,tredgeoncarapace,honey,manticoretail,unicorntears,dawnlings,bluewheat,selkyskin,kelpieskin,flickerwing]
full_ingredient_list3 = [pookapus,kelpiedung,pheonixsweat,jaculusvenom,bottledrainbow,chamuleaves,irilenenectar,amarallitine,ruckleberries,bennufeathers,slumberberries,sirenwhiskers]

elixerlist = [abrasionpersuasion,acheybreak,blisterblast,bruisecruise,burnout,woundwipe,floof,browneyesolidaritea,greenleaf,lovelylocks,mermaidtigerdelight,seasee,goldtransmutation,silvertransmutation,ironpurification,hushslush,droolydew,quicksnuff,fadefuel,slumberberrytea]

def print_ingredient_list(inglist:list):
    for i in range(len(inglist)):
        sleep(.5)
        print(f"{i + 1}) {inglist[i]}")

def validate(choice):
    try:
        choice = int(choice)
        if choice < 1 or choice > 6:
            print("Please enter a number 1 to 6.")
            return False
        return True
    except:
        print("Please enter a number 1 to 6.")
        return False


def alc_game():
    print("For your alchemy assignment, you will need to create the required elixer.")
    sleep(2)
    assigned_elixer = elixerlist[randint(0,len(elixerlist)-1)]
    print(f"Today, we are making the {assigned_elixer.name} elixer. {assigned_elixer}")
    sleep(2)

    ingredient_list1 = []
    ingredient_list2 = []
    ingredient_list3 = []

    ingredient_list1.append(assigned_elixer.in1)
    ingredient_list2.append(assigned_elixer.in2)
    ingredient_list3.append(assigned_elixer.in3)

    while len(ingredient_list1) < 6:
        new_ing = full_ingredient_list1[randint(0,len(full_ingredient_list1)-1)]
        if new_ing not in ingredient_list1:
            ingredient_list1.append(new_ing)
    shuffle(ingredient_list1)
    new = []
    for i in range(6):
        new.append(ingredient_list1[(i+3)%6])
    ingredient_list1 = new
    shuffle(ingredient_list1)

    while len(ingredient_list2) < 6:
        new_ing = full_ingredient_list2[randint(0,len(full_ingredient_list2)-1)]
        if new_ing not in ingredient_list2:
            ingredient_list2.append(new_ing)
    shuffle(ingredient_list2)
    new = []
    for i in range(6):
        new.append(ingredient_list2[(i+3)%6])
    ingredient_list2 = new
    shuffle(ingredient_list2)

    while len(ingredient_list3) < 6:
        new_ing = full_ingredient_list3[randint(0,len(full_ingredient_list3)-1)]
        if new_ing not in ingredient_list3:
            ingredient_list3.append(new_ing)
    shuffle(ingredient_list3)
    new = []
    for i in range(6):
        new.append(ingredient_list3[(i+3)%6])
    ingredient_list3 = new
    shuffle(ingredient_list3)

    while True:
        print("Pick your first ingredient.")
        print_ingredient_list(ingredient_list1)
        choice1 = input()
        while not validate(choice1):
            choice1 = input()
        choice1 = int(choice1)

        chosen_ing1 = ingredient_list1[choice1 - 1]

        sleep(.5)
        print("Pick your second ingredient.")
        print_ingredient_list(ingredient_list2)
        choice2 = input()
        while not validate(choice2):
            choice2 = input()
        choice2 = int(choice2)

        chosen_ing2 = ingredient_list2[choice2 - 1]

        sleep(.5)
        print("Pick your final ingredient.")
        print_ingredient_list(ingredient_list3)
        choice3 = input()
        while not validate(choice3):
            choice3 = input()
        choice3 = int(choice3)

        chosen_ing3 = ingredient_list3[choice3 - 1]

        my_elixer = Elixer(chosen_ing1,chosen_ing2,chosen_ing3)
        sleep(1)
        print(my_elixer)
        sleep(2)

        if my_elixer == assigned_elixer:
            print(f"Well done! You've created the {assigned_elixer.name} elixer.")
            sleep(2)
            break
        else:
            print(f"Not quite. We want the {assigned_elixer.name} elixer. {assigned_elixer} Let's keep trying.")
            sleep(2)
    return None
