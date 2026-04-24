import math
import time
import random

def start():
    now = input("Grumblin is a little goblin boy.\nHe loves attacking low level adventurers and stealing their loot to add to his ever-growing stash.\n But today, Flim-bim stole his stuff!\nNow, you have to help Grumblin get his treasure back! (press c to continue)")
    if now == "c" or "C":
        print("Grumblin has 10 stat points and 10 hp to start. Attack is for attacking enemies with hands, \nDefense makes sure you don't die, \nMagic makes you attck with mind.")


Atk = int(input("Input a number for Attack:"))
Def = int(input("Input a number for Defense:"))
Mag = int(input("Input a number for Magic:"))

if Atk + Def + Mag >= 10 or Atk + Def + Mag <= 10:
    Atk = int(input("Input a number for Attack:"))
    Def = int(input("Input a number for Defense:"))
    Mag = int(input("Input a number for Magic:"))

print(f"So Grumblin has {Atk} attack, {Def} defense, and {Mag} magic. Now, he can fight for his treasure! There's five rounds until Flim-bim, good luck!")
Hp = 10





turn = 1



   
def fights():
while sumt<5: #NEED TO FIGURE OUT HOW TO MAKE 5 NPC FiGHTS APPEAR BEFORE FLIMBIM
    attacks = ["Scratch","Bite","Rock Throw"]
    strength = []
    durability = []
    turn = []
    npc_hp = []
    creature = ["Wolf", "Mutant spider", "Cyclops","Leviathan", "Yeti", "Gorgon", "Ghoul", "Minotaur"]
    classes = ["Attacker","Defender","Speedster","All-Rounder", "Technical"]
    cre = (random.choice(creature))
    cla = (random.choice(classes))
    att = (random.choice(attacks))
    if classes == "Attacker":
        npc_hp = [10]
        strength = [3]
    if classes == "Defender":
        npc_hp = [15]
        strength = [2]
    if classes == "Speedster":
        npc_hp = [9]
        strength = [1]
    if classes == "All-Rounder":
        npc_hp = [13]
        strength = [2]
    if classes == "Technical":
        npc_hp = [11]
        strength = [2]
    print(f"A {cre} approaches, it's a {cla} type. It may hit you with {attacks}. It has {npc_hp} hp.")
    if turn % 2 == 0:
        Grumfight = input("type Attack to attack with Goblin fist, and Magic to throw a fireball!")
        if Grumfight == "Attack":
            npc_hp - Atk
            print(f"Goblin fist! Enemy now has {npc_hp}!")
            time.sleep(0.5)
            turn = turn + 1
        elif Grumfight == "Magic":
            npc_hp - Mag
            print(f"Fireball! Enemy now has {npc_hp}!")
            time.sleep(0.5)
            turn = turn + 1
    elif turn % 2 == 1:
        
        
    card1 = Atk * 2
    card2 = Atk + turn
    card3 = Mag * 2
    card4 = Mag + turn
    card5 = Def * 2
    card6 = Def + turn
    card7 = Hp * 2
    card8 = Hp + turn
    Cards = [card1, card2, card3, card4, card5, card6, card7, card8]
    random.choice(Cards)

#Flimbim activation
boss_hp = 50
boss_strength = 5
boss_attacks = ["Ground Pound", "Scratch Barrage", "Magic beam"]
print(f"Flim-bim appears! It's the boss and it can hit you with {boss_attacks}. It has {boss_hp} hp.")



