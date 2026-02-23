import os
import time
import random
import json

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

#1. Easy - 5 tries, Range(1,20)
#2. Medium- 5 tries, Range(1,40)
#3. Hard - 5 tries, Range(1,60)
#4. Master - 5 tries, Range(1,80)
#5. Legend - 5 tries, Range(1,100)


def play_game(range):
    if os.path.exists("score.json"):
        try:
            with open("score.json","r") as f:
                High_score=json.load(f)
        except:
            os.remove("score.json")
    else:
        High_score=0
    game_loop=True
    score=0
    while game_loop:
        tries=5
        ans=random.randint(1,20*range)
        print(f"I am a number between between 1 and {20*range}")
        print(ans)
        while tries!=0:
            user_guess=try_int("Guess the number: ","number")
            tries-=1
            time.sleep(0.5)
            if user_guess>20*range or user_guess<0:
                print("Your guess is is out of range")
            elif user_guess>ans:
                print("Ooops!!! Too high! Try again")
            
            elif user_guess<ans:
                print("Ooops!!! Too low! Try again")
            else:
                print("Correct! you're a genius")
              
                score+=range
                break
        if score>High_score:
            print(f"Congratulations!!! You have the new High Score: {score}")
            time.sleep(1)
            with open("score.json","w") as f:
                json.dump(score,f)
        clear()
        print("Replay Game?\n1. Yes\n2. No")
        loop2=True
        while loop2:
            user_option=try_int("Select an option: ","option")
            if user_option==1:
                clear()
                loop2=False
            elif user_option==2:
                print("Exiting Game...")
                time.sleep(1)           
                game_loop=False
                loop2=False
            else:
                print("Invalid Option")
                time.sleep(1)
    
    


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


    clear()
    if user_option==1:
        score=0
        print("1. Easy\n2. Medium\n3. Hard\n4. Master\n5. Legend")    
        while True:
            difficulty_level=try_int("Select a Difficulty Level: ","option") 
            if difficulty_level>5:
                print("Invalid Option")
            else:
                time.sleep(0.5)
                clear()
                play_game(difficulty_level)
                outer_loop1=False
                break
    elif user_option==2:
        if os.path.exists("score.json"):
            try:
                with open("score.json","r")as f:
                    score=json.load(f)
                    print(f"Your High Score is: {score}")   
                    time.sleep(3)
            except:
                os.remove("score.json")
        else:
            print("Your High Score is: 0")
            time.sleep(2)
    elif user_option==4:
        time.sleep(0.5)
        print("Exiting Game...")
        time.sleep(1)
        print("Bye!!!...")
        time.sleep(1)
        outer_loop1=False   
    elif user_option==3:
        print("1. The computer generates a random number between 1 and 20,40,60 depending on the level you choose")
        print("2. Guess the number")
        print("3. You have only 5 tries")
        input("Press any key to go back: ")

    



