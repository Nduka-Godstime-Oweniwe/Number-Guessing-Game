import os
import time
import random

def clear():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")
#x is user prompt
def try_int(x,y):
    while True:
        try:
            return int(input(x))
        except ValueError:
            print("Invalid",y)
#easy= 3tries-10
#medium=4tries-20
#hard=4tries-30
#veryhard=5tries-50
#Master=5tries -70
#Legend=6tries - 100
def play_game(tries,range):
    


outer_loop1=True
while outer_loop1:
    clear()
    print("Number Guessing Game\n1. Play Game\n2. High Score\n3. How to Play\n4. Exit")
    while True:
        user_option=try_int("Select and option: ","option")
        if user_option>4:
            print("Invalid Option")
        else:
            break
    #User exits Game
    if user_option==1:
        print("1. Easy\n2. Medium\n3. Hard\n4. Very Hard\n5. Master\n6. Legend")    
        while True:
            difficulty_level=try_int("Select a Difficulty Level: ","option") 
            if difficulty_level>6:
                print("Invalid Option")
            else:
                break
    elif user_option==4:
        clear()
        time.sleep(0.5)
        print("Exiting Game...")
        time.sleep(1)
        print("Bye!!!...")
        time.sleep(1)
        outer_loop1=False   
    elif user_option==3:
        print("1. The computer generates a random number between 1 and 10,20,30 depending on the level you choose")
        print("1. Guess the number")
        print("2. You have limited number of trials depending on the difficulty level you choose")

    



