print('Welcome! Try to guess the correct number to win the game! \n ')
print("For your first round, you get three chances to guess the correct number. \n")
print('Win the level and win a life. Guess incorrect and its Game Over! \n ')
print("WARNING! THIS GAME IS EXTREMELY HARD. \n ")
import time
def time_convert(sec):
        mins = sec // 60
        sec = sec % 60
        print("Time took to complete: ")
        print("Time Lapsed = {0}:{1}".format(int(mins),sec))
start= input("Press Enter to start the timer")
start_time = time.time()


import random
lives=3
def level_one():
    """ 

    """
    global lives
    print("☆ LEVEL ONE!☆")
    print(" You have " +str(lives)+ ' lives left!\n' )
    while True:
        guess = input("Enter a number from 1 to 10: ")
        if guess.isdigit():
            guess= int(guess)
            break
        else:
            print('Please select a value of 0 or greater')
    num1=random.randint(1,10)
    while num1 in range(1,10):
        if guess == num1:
            print("Correct! A life was added.")
            lives += 1
            break
        elif guess > num1 :
            lives -= 1
            print("lives:" +str(lives))
            print("Try again! Too high! \n ")
            while True:
                guess = input("Enter a number from 1 to 10: ")
                if guess.isdigit():
                    guess= int(guess)
                    break
                else:
                    print("Please select a value of 0 or greater \n ")
        else:
            lives -= 1
            print("lives:" +str(lives))
            print("Try Again! Too low \n ")
            while True:
                guess = input("Enter a number from 1 to 10:  ")
                if guess.isdigit():
                    guess= int(guess)
                    break 
                else:
                    print('Please select a value of 0 or greater')

        while lives == 0:
            end_time = time.time()
            print("GAME OVER. The correct number was " +str(num1))
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
            response = input("Do you want to play again? Y/N: ")
            if response != 'Y':
                quit()
            if response == 'Y':
                lives = 3
                starting_game()


def level_two():
    """ (int) -> int:

    """ 
    global lives
    print("☆ LEVEL TWO!☆")
    print(" You have " +str(lives)+ ' lives left!\n' )
    while True:
        guess = input("Enter a number from 1 to 50: ")
        if guess.isdigit():
            guess= int(guess)
            break
        else:
            print('Please select a value of 0 or greater \n ')
    num2 = random.randint(1,50)
    while num2 in range(1,50):
        if guess == num2:
            print("Great job! A life was added")
            lives+=1
            break
        elif guess > num2:
            lives -= 1
            print("lives:" +str(lives))
            print("Too high! Take another shot! \n ")
            while True:
                guess = input("Enter a number from 1 to 50: ")
                if guess.isdigit():
                    guess= int(guess)
                    break
                else:
                    print("Please select a value of 0 or greater")
        else: 
            lives -= 1
            print("lives:" +str(lives))
            print("Too low! Try again \n ")
            while True:
                guess = input("Enter a number from 1 to 50: ")
                if guess.isdigit():
                    guess= int(guess)
                    break
                else:
                    print("Please select a value of 0 or greater")


        while lives == 0:
            end_time = time.time()
            print("GAME OVER. The correct number was " +str(num2))
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
            response = input("Do you want to play again? Y/N: ")
            if response != 'Y':
                quit()
            if response == 'Y':
                lives = 3
                starting_game()
    
def level_three():
    """ (int) -> int:

    """ 
    global lives
    print("☆ LEVEL THREE!☆ \n ")
    print("Just when you though this game was easy \n ")
    print(" You have " +str(lives)+ ' lives left! \n ' )
    lives += 1
    while True:
        guess = input("Enter a number from 1 to 100: ")
        if guess.isdigit():
            guess= int(guess)
            break
        else:
            print('Please select a value of 0 or greater')
    num3 = random.randint(1,100)
    while num3 in range(1,100):
        if guess == num3:
            print("Great job!")
            lives += 1
            break
        elif guess % 2 == 0:
            lives -= 1
            print("lives:" +str(lives))
            print("Hint: The correct number is even ! Take another shot! \n ")
            while True:
                guess = input("Enter a number from 1 to 100: ")
                if guess.isdigit():
                    guess= int(guess)
                    break
                else:
                    print("Please select a value of 0 or greater")

        else: 
            lives -= 1
            print("lives:" +str(lives))
            print("Hint: The correct number is odd. Try again \n ")
            while True:
                guess = input("Enter a number from 1 to 100: ")
                if guess.isdigit():
                    guess= int(guess)
                    break
                else:
                    print("Please select a value of 0 or greater")

        while lives <= 0:
            end_time = time.time()
            print("GAME OVER. The correct number was " +str(num3))
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
            response = input("Do you want to play again? Y/N: ")
            if response != 'Y':
                quit()
            if response == 'Y':
                starting_game()
                

            
def level_four():
    """ (int) -> int:

    """ 
    global lives
    print("☆ LEVEL FOUR!☆")
    print(" You have " +str(lives)+ ' lives left! \n ' )
    lives += 1
    while True:
        guess = input("Enter a number from 1 to 500: ")
        if guess.isdigit():
            guess= int(guess)
            break
        else:
            print('Please select a value of 0 or greater \n')
    num4 = random.randint(1,500)
    while num4 in range(1,500):
        if guess == num4:
            print("Awesome job! A life was added")
            lives += 1
            break
        elif num4 % 2 == 0:
            lives -= 1
            print("lives:" +str(lives))
            print("Hint: The correct number is even! Try guessing lower! \n")
            while True:
                guess = input("Enter a number from 1 to 500: ")
                if guess.isdigit():
                    guess= int(guess)
                    break
                else:
                    print("Please select a value of 0 or greater")
        else: 
            lives -= 1
            print("lives:" +str(lives))
            print("Hint: The correct number is odd! Try a higher number! \n ")
            while True:
                guess = input("Enter a number from 1 to 500: ")
                if guess.isdigit():
                    guess= int(guess)
                    break
                else:
                    print("Please select a value of 0 or greater")

        while lives == 0:
            end_time = time.time()
            print("GAME OVER. The correct number was " +str(num4))
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
            response = input("Do you want to play again? Y/N: ")
            if response != 'Y':
                quit()
            if response == 'Y':
                lives = 3
                starting_game()
                
def level_five():
    """ (int) -> int:

    """ 
    global lives
    print("☆ LEVEL FIVE!☆")
    print(" You have " +str(lives)+ ' lives left! \n ' )
    lives += 1
    while True:
        guess = input("Enter a number from 1 to 1000: ")
        if guess.isdigit():
            guess= int(guess)
            break
        else:
            print('Please select a value of 0 or greater')
    num5 = random.randint(1,1000)
    while num5 in range(1,1000):
        if guess == num5:
            print("You win!")
            lives += 1
            break
        elif num5 % 2 == 0:
            lives -= 1
            print("lives:" +str(lives))
            reply = input("Do you want a hint? Y/N:")
            if reply == 'Y':
                print("The correct number is a divisible by 2! Try guessing lower! \n ")
            
            while True:
                guess = input("Enter a number from 1 to 1000: ")
                if guess.isdigit():
                    guess= int(guess)
                    break
                else:
                    print("Please select a value of 0 or greater")
        elif num5 % 3 == 0:
            lives -= 1
            print("lives:" +str(lives))
            reply = input("Do you want a hint? Y/N:")
            if reply == 'Y':
                print("The correct number is a divisible by 3! Try guessing lower! \n ")
            
            while True:
                guess = input("Enter a number from 1 to 1000: ")
                if guess.isdigit():
                    guess= int(guess)
                    break
                else:
                    print("Please select a value of 0 or greater")
            
        
        while lives == 0:
            end_time = time.time()
            print("GAME OVER. The correct number was " +str(num5))
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
            response = input("Do you want to play again? Y/N: ")
            if response != 'Y':
                quit()
            if response == 'Y':
                lives = 3
                starting_game()
                

def starting_game():
    
    print("What level do you want to start at?")
    print("Level [1] - beginner, Level [2] - easy, Level [3] - intermediate, Level [4]- hard, Level [5] - extreme")
    start_level= input("> ")
    while True:
        if start_level.isdigit():
            start_level= int(start_level)
            break
        else:
            print("Please enter a digit")
            print("Level [1] - beginner, Level [2] - easy, Level [3] - intermediate, Level [4]- hard, Level [5] - extreme")
            start_level= input("> ")
    if start_level == 1:
        level_one()
        level_two()
        level_three()
        level_four()
        level_five()
    if start_level == 2:
        level_two()
        level_three()
        level_four()
        level_five()
    if start_level == 3:
        level_three()
        level_four()
        level_five()
    if start_level == 4:
        level_four()
        level_five()
    if start_level == 5:
        level_five()
starting_game()

while lives == 0:

    print("GAME OVER")
    response = input("Do you want to play again? Y/N: ").lower
    if response != 'y':
        quit()
    if response == 'y':
        starting_game()
    input("Press Enter to stop")
    end_time = time.time() 

    
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)