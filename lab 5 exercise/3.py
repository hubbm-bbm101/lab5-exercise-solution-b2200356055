#lab 5 exercise-3
#name - İbrahim Enes Köse
#id -   2200356055

import random
picked_number = random.randint(0,100)

def loop():
    guessed_number = int(input())
    if guessed_number > picked_number:
        print("decrease your number")
        loop()
    elif guessed_number < picked_number:
        print("increase your number")
        loop()
    else:
        print("correct guess")

loop()