import random

def compare_numbers(number, user_guess):
    ## your code here
    return cowbull

playing = True #gotta play the game
number = str(random.randint(1000,9999)) #random 4 digit number
guesses = 0

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")


def compare_numbers(num,guess):
    bulls=0
    cows=0
    for i in range(len(num)):
        if guess[i] == num[i]:
            bulls+=1
        else:
            for j in range(len(guess)):
                if guess[i]==num[j]:
                    cows+=1
                    print(cows,i)
    return cows,bulls

while playing:
    user_guess = str(input("Give me your best guess!"))
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "guesses! The number was "+str(number))
    
    else:
        print("Your guess isn't quite right, try again.")



        
