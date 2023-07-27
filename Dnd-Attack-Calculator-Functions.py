from random import random
from random import randint

def enem(num, die, dienum, mod):
    """ 
    Takes in the following values:
    num = number of monsters attacking, or iterations of attacks you want to calculate for. For example, if you have a battle with 6 Goblins, you can simulate 4 rounds by setting num to 24. 
    die = type of dice the monster uses (e.g. d6, d10, d20, etc.). 
    dienum = multiplier value for dice (e.g. monsters uses 4d6, so 'dienum' would be 4 and 'die' would be 6)
    mod = attack modification value, which is usually the last number listed in the format, '2' in this case: 1d6+2.
    """
    
    dmgsum = 0
    while num > 0:
        dienumb=dienum
        while dienumb > 0:
            dmgsum = dmgsum + randint(1,die)
            dienumb-=1
        num-=1
        print(dmgsum+mod)
        dmgsum = 0
