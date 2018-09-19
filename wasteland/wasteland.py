#wasteland game
import time
import random

class Characters():
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
        print(x + ": Mind if I join you on your travels?")
        answer_fstscn = input("(What do you say? Y for 'yes', N for 'no')")
        if answer_fstscn == ""
