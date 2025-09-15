#dice rolling

import random


diceroll=True

while diceroll :
    print(random.randint(1,6))
    playagain=input("want to roll again")

    if playagain=="yes":
        continue
    else:print("game over")
    break