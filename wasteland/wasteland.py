#wasteland game
import time
import random

unvalid = "(Not a valid command.)"

main_char = {'name': "...", 'hp': 100, 'atk': 10, 'def': 20,}
comp_char = {'name': "Stranger", 'hp': 100, 'atk': 10, 'def': 20,}
#-----------------------------------------------------------------------
main_char_inv = {'Torch': 1, 'Box of Matches': 10, 'Knife': 1, 'Box of Crackers': 10,}

class Environment():
    #denne class vælger start biome for spilleren, og om der er træer og/eller vand omkring
    possible_biomes = ["Forest", "Tundra", "Riverside", "Coast", "Plains",]
    def start_biome(biomes):
        water = [True, False]
        trees = [True, False]
        startingbiome = random.choice(biomes)
        if startingbiome == "Forest":
            trees = True
            water = random.choice(water)
        elif startingbiome == "Tundra":
            trees = True
            water = True
        elif startingbiome == "Riverside":
            trees = random.choice(trees)
            water = True
        elif startingbiome == "Coast":
            trees = False
            water = True
        else:
            trees = True
            water = random.choice(water)
    start_biome(possible_biomes)

class FirstScene():
    def firstscene(x):
        print(x + ": Hey.. Hey! You awake?")
        time.sleep(1)
        print("(You slowly open your eyes, and you see a stranger looking right at you.)")
        time.sleep(1)
        print(x + ": I don't think it's a good idea to sleep out here, who knows who might come by.")
        print(x + ": May I join you on your travels?")
        answer_fstscn = input("(What do you say? Y for 'yes', N for 'no')")
        if answer_fstscn == "Y" or "y":
            time.sleep(0.5)
            print(x + ": Great! You lead the way.")
        elif answer_fstscn == "N" or "n":
            time.sleep(1)
            print(x + ": Are you sure? It's dangerous to travel alone. Well, I'm coming with you anyway.")
        else:
            print(unvalid)
    firstscene(comp_char[0])

FirstScene()


#yeeeeet
