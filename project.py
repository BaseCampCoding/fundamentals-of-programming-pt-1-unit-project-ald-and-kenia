print('Welcome! Try to guess the correct number to win the game!')
print("For your first round, you get three chances to guess the correct number.")
print('Win the level and win a life. Guess incorrect and its Game Over!')
import random
lives=3
def level_one():
    """ 

    """
    global lives
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
            print("Correct!")
            lives += 1
            break
        elif guess > num1 :
            lives -= 1
            print("lives:" +str(lives))
            print("Try again! Too high!")
            while True:
                guess = input("Enter a number from 1 to 10: ")
                if guess.isdigit():
                    guess= int(guess)
                    break
                else:
                    print("Please select a value of 0 or greater")
        else:
            lives -= 1
            print("lives:" +str(lives))
            print("Try Again! Too low")
            while True:
                guess = input("Enter a number from 1 to 10: ")
                if guess.isdigit():
                    guess= int(guess)
                    break 
                else:
                    print('Please select a value of 0 or greater')

    while lives == 0:
        print("GAME OVER")
        response = input("Do you want to play again? Y/N: ")
    if response != 'Y':
        quit()
    if response == 'Y':
        level_one()

def level_two():
    """ (int) -> int:

    """ 
    global lives
    print("☆ Congratulations! You made it to level two!☆")
    print("A life was added. You have " +str(lives)+ ' lives left!' )
    while True:
        guess = input("Enter a number from 1 to 50: ")
        if guess.isdigit():
            guess= int(guess)
            break
        else:
            print('Please select a value of 0 or greater')
    num2 = random.randint(1,50)
    while num2 in range(1,50):
        if guess == num2:
            print("Great job!")
            lives+=1
            break
        elif guess > num2:
            lives -= 1
            print("lives:" +str(lives))
            print("Too high! Take another shot!")
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
            print("Too low! Try again")
            while True:
                guess = input("Enter a number from 1 to 50: ")
                if guess.isdigit():
                    guess= int(guess)
                    break
                else:
                    print("Please select a value of 0 or greater")


        if lives == 0:
            print("GAME OVER")
            quit()
    
def level_three():
    """ (int) -> int:

    """ 
    global lives
    print("☆ Awesome! You made it to level three!☆")
    print("A life was added. You have " +str(lives)+ ' lives left!' )
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
            print("Hint: The correct number is even ! Take another shot!")
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
            print("Hint: The correct number is odd. Try again")
            while True:
                guess = input("Enter a number from 1 to 10: ")
                if guess.isdigit():
                    guess= int(guess)
                    break
                else:
                    print("Please select a value of 0 or greater")
            
def level_four():
    """ (int) -> int:

    """ 
    global lives
    print("☆ Great job! Welcome to level four!☆")
    print("A life was added. You have " +str(lives)+ ' lives left!' )
    while True:
        guess = input("Enter a number from 1 to 500: ")
        if guess.isdigit():
            guess= int(guess)
            break
        else:
            print('Please select a value of 0 or greater')
    num4 = random.randint(1,500)
    while num4 in range(1,500):
        if guess == num4:
            print("Awesome job!")
            lives += 1
            break
        elif guess % 2 == 0:
            lives -= 1
            print("lives:" +str(lives))
            print("Hint: The correct number is even! Try guessing lower!")
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
            print("The correct number is odd! Try a higher number!")
            while True:
                guess = input("Enter a number from 1 to 500: ")
                if guess.isdigit():
                    guess= int(guess)
                    break
                else:
                    print("Please select a value of 0 or greater")
            
def level_five():
    """ (int) -> int:

    """ 
    global lives
    print("You have made it to the Ultimate Level!")
    print("A life was added. You have " +str(lives)+ ' lives left!' )
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
            print("Awesome job!")
            lives += 1
            break
        elif guess % 2 == 0:
            lives -= 1
            print("lives:" +str(lives))
            print("The correct number is a divisible by 2! Try guessing lower!")
            while True:
                guess = input("Enter a number from 1 to 1000: ")
                if guess.isdigit():
                    guess= int(guess)
                    break
                else:
                    print("Please select a value of 0 or greater")
            
        else: 
            lives -= 1
            print("lives:" +str(lives))
            print("That number is too low! Try a higher number!")
            while True:
                guess = input("Enter a number from 1 to 1000: ")
                if guess.isdigit():
                    guess= int(guess)
                    break
                else:
                    print("Please select a value of 0 or greater")

while lives == 0:

    print("GAME OVER")
    response = input("Do you want to play again? Y/N: ").upper
    if response != 'Y':
        quit()
    if response == 'Y':
        level_one()
print("What level do you want to start at?")
start_level=int(input("Level [1] - beginner, Level [2] - easy, Level [3] - intermediate, Level [4]- hard, Level [5] - extreme"))
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