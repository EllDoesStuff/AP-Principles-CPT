import math
import time
import random
import sys

def start():
    now = input("Grumblin is a little goblin boy.\nHe loves attacking low level adventurers and stealing their loot to add to his ever-growing stash.\nBut today, Flim-bim stole his stuff!\nNow, you have to help Grumblin get his treasure back! (press c, then enter to continue)")
    if now == "c" or "C":
        print("Grumblin has 10 stat points (spend these on your stats) after drinking a magic potion, and 10 hp to start. \nAttack is for attacking enemies with your hands, \nDefense makes sure you don't die, \nMagic makes you attack with your mind.\nMake sure your values add up to ten!")

        






   
def fights():
        Hp = 10
        attacks = ["Scratch","Bite","Rock Throw"]
        creature = ["Wolf", "Mutant spider", "Cyclops","Leviathan", "Yeti", "Gorgon", "Ghoul", "Minotaur"]
        classes = ["Attacker","Defender","Speedster","All-Rounder", "Technical"]
        cre = (random.choice(creature))
        cla = (random.choice(classes))
        att = (random.choice(attacks))
        if cla == "Attacker":
            npc_hp = 10
            strength = 3
        if cla == "Defender":
            npc_hp = 15
            strength = 2
        if cla == "Speedster":
            npc_hp = 9
            strength = 1
        if cla == "All-Rounder":
            npc_hp = 13
            strength = 2
        if cla == "Technical":
            npc_hp = 11
            strength = 2
        while npc_hp > 0:
            turn = 1
            print(f"A {cre} approaches, it's a {cla} type. It may hit you with {att}. It has {npc_hp} hp.")
            if turn % 2 == 1 and turn != 0:
                Grumfight = input("type Attack to attack with Goblin fist, and Magic to throw a fireball!")
                if Grumfight == "Attack" or "attack":
                    if npc_hp - Atk < 0:
                        npc_hp = 0
                    else:    
                        npc_hp = npc_hp - Atk
                    
                elif Grumfight == "Magic" or "magic":
                    if npc_hp - Mag < 0:
                        npc_hp = 0
                    else:    
                        npc_hp = npc_hp - Mag
                    print(f"Fireball! Enemy now has {npc_hp} HP!")
                    time.sleep(0.5)
                    turn = turn + 1
            if turn % 2 == 0 and turn != 0 and npc_hp != 0:              
                if Hp - (strength - math.ceil(Def * 1/3)) < 0:
                    Hp = 0
                    print("You failed! Flim-bim keeps your treasure.")
                    time.sleep(2)
                    sys.exit(0)
            Hp -= strength - math.ceil(Def * 1/3)        
            print(f"You took {strength - math.ceil(Def * 1/3)} damage. You now have {Hp} HP!")
            print("|-----------------------------------------------------------------------|")                 
            if npc_hp == 0:
                turn = 0
                Hp = 10


def BOSS():
        boss_hp = 40
        boss_strength = 4
        boss_attacks = ["Ground Pound", "Scratch Barrage", "Magic beam"]
        Hp = 10
        print(f"Flim-bim appears! It's the boss and it can hit you with {random.choice(boss_attacks)}. It has {boss_hp} hp.")
        while boss_hp > 0:
            turn = 1
            if turn % 2 == 1 and turn != 0:
                Grumfight = input("type Attack to attack with Goblin fist, and Magic to throw a fireball!")
            if Grumfight == "Attack" or "attack":
                if boss_hp - Atk < 0:
                    boss_hp = 0
                else:    
                    boss_hp = boss_hp - Atk
                    print(f"Goblin Fist! Enemy now has {boss_hp} HP!")
                    time.sleep(0.5)
                    turn = turn + 1                    
            elif Grumfight == "Magic" or "magic":
                if boss_hp - Mag < 0:
                    boss_hp = 0
                else:    
                    boss_hp = boss_hp - Mag
                    print(f"Fireball! Enemy now has {boss_hp} HP!")
                    time.sleep(0.5)
                    turn = turn + 1
        if turn % 2 == 0 and turn != 0 and boss_hp != 0:              
            Hp -= boss_strength - math.ceil(Def * 1/3)
            if Hp - (boss_strength - math.ceil(Def * 1/3)) < 0:
                Hp = 0
                print("You failed! Flim-bim keeps your treasure.")
                time.sleep(2)
                sys.exit(0)                    
            print(f"You took {boss_strength - math.ceil(Def * 1/3)} damage. You now have {Hp} HP!")   
            print("|----------------------------------------------------------------------------|")
            turn += 1
        print("You win! Grumblin gets his treasure back, and Flim-bim is defeated!")         
            


start()
Atk = int(input("Input a number for Attack:"))
Def = int(input("Input a number for Defense:"))
Mag = int(input("Input a number for Magic:"))

if Atk + Def + Mag > 10 or Atk + Def + Mag < 10:
    print("Doesn't add to ten!")
    Atk = int(input("Input a number for Attack:"))
    Def = int(input("Input a number for Defense:"))
    Mag = int(input("Input a number for Magic:"))

print(f"So Grumblin has {Atk} attack, {Def} defense, and {Mag} magic. Now, he can fight for his treasure! There's five rounds until Flim-bim, good luck!")
fight = 1
while fight < 6:
    fights()
    fight = fight + 1
def boon():
    boon_num = int(input("Before you fight Flim-Bim, a G O D grants you a B O O N.\n You can become S T R O N G E R and get twice your damage (input 1),\nYou can become B U L K I E R and gain 2.5 times your defence (input 2),\n or you can become A S C E N D E D and gain twice your magic (input 3)." ))
    global Atk, Def, Mag
    if boon_num == 1:
        Atk *= 2
    elif boon_num == 2:
        Def *= 2.5
    elif boon_num ==3:
        Mag *= 2    
boon()
BOSS()    


