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

print(f"So Grumblin has {Atk} attack, {Def} defense, and {Mag} magic. Now, he can fight for his treasure!")
Hp = 10
card1 = Atk * 2
card2 = Atk + turn
card3 = Mag * 2
card4 = Mag + turn
card5 = Def * 2
card6 = Def + turn
Mults = [card1, card2, card3, card4, card5, card6]
card7 = Hp * 2
card8 = Hp + turn
Heals = [card7, card8] 

turn = 1

while act != True:
    turn + 1


def Damage():

start()