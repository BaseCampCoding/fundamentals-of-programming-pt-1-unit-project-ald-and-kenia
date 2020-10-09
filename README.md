# number guessing
The game allows you to go through levels guessing a number. Each level is harder than the last, the first being the easiest, and the fifth being the hardest. 
The user has the option to pick each level when they start the game, and has three chances to guess the correct number. 
They're given hints throughout each level, and if they guess correctly, they get another chance added. If they use all of their chances, the game ends. 


# usage
def level_five():
    """ (int) -> int:
    return whether the player wins or loses or continues to the next level based on their input

    >>>("Enter a number from 1 to 1000: 566")
    "The correct number is divisible by 2! Try guessing lower.

    >>>("Enter a number from 1 to 1000: 500")
    ("You win!")

    """ 
    global lives
    print(Fore.LIGHTMAGENTA_EX+"☆ LEVEL FIVE!☆"+ Style.RESET_ALL)
    print(" You have " +str(lives)+ ' lives left! \n ' )
    lives += 1
    while True:
        guess = input("Enter a number from 1 to 1000: ")
        if guess.isdigit():
            guess= int(guess)
            if guess <= 1000:
                break
            else:
                print('Please enter a number from 1 to 1000 \n ')
                

           
