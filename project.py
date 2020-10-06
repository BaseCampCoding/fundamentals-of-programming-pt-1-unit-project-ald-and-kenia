print('Welcome! Try to guess the correct number to win the game!')
print("For your first round, you get three chances to guess the correct number.")
print('Win the level and win a life. Guess incorrect and its Game Over!')
import random
lives=3
def level_one():
    """ 

    """
    global lives
    guess = int(input("Enter a number from 1 to 10: "))
    num1=random.randint(1,10)
    while num1 in range(1,10):
        if guess == num1:
            print("Correct!")
            break
        elif guess > num1 :
            lives -= 1
            print("lives:" +str(lives))
            print("Try again! Too high!")
            guess = int(input("Enter a number from 1 to 10: "))
        else:
            lives -= 1
            print("lives:" +str(lives))
            print("Try Again! Too low")
            guess = int(input("Enter a number from 1 to 10: "))

level_one()
def level_two():
    """ (int) -> int:

    """ 
    global lives
    print("☆ Congratulations! You made it to level two!☆")
    guess = int(input("Enter a number from 1 to 50: "))
    num2 = random.randint(1,50)
    while num2 in range(1,50):
        if guess == num2:
            print("great job!")
            break
        elif guess > num2:
            lives -= 1
            print("lives:" +str(lives))
            print("That number was too high! Take another shot!")
            guess = int(input("Enter a number from 1 to 50: "))
        else: 
            lives -= 1
            print("lives:" +str(lives))
            print("That number is too low! Try again")
            guess = int(input("Enter a number from 1 to 50: "))
level_two()

def level_three():
    """ (int) -> int:

    """ 
    global lives
    print("☆ Awesome! You made it to level three!☆")
    guess = int(input("Enter a number from 1 to 100: "))
    num3 = random.randint(1,100)
    while num3 in range(1,100):
        if guess == num3:
            print("Great job!")
            break
        elif guess > num3:
            lives -= 1
            print("lives:" +str(lives))
            print("That number was too high! Take another shot")
            guess = int(input("Enter a number from 1 to 100: "))
        else: 
            lives -= 1
            print("lives:" +str(lives))
            print("That number is too low! Try again")
            guess = int(input("Enter a number from 1 to 100: "))

level_three()

def level_four():
    """ (int) -> int:

    """ 
    global lives
    print("☆ Great job! Welcome to level four!☆")
    guess = int(input("enter a number from 1 to 500: "))
    num4 = random.randint(1,500)
    while num4 in range(1,500):
        if guess == num4:
            print("Awesome job!")
            break
        elif guess > num4:
            lives -= 1
            print("lives:" +str(lives))
            print("That number was too high! Try guessing lower!")
            guess = int(input("Enter a number from 1 to 500: "))
        else: 
            lives -= 1
            print("lives:" +str(lives))
            print("That number is too low! Try a higher number!")
            guess = int(input("Enter a number from 1 to 500: "))

level_four()

def level_five():
    """ (int) -> int:

    """ 
    global lives
    print("You have made it to the Ultimate Level!")
    guess = int(input("enter a number from 1 to 500: "))
    num5 = random.randint(1,1000)
    while num5 in range(1,1000):
        if guess == num5:
            print("Awesome job!")
            break
        elif guess > num5:
            lives -= 1
            print("lives:" +str(lives))
            print("That number was too high! Try guessing lower!")
            guess = int(input("Enter a number from 1 to 1000: "))
        else: 
            lives -= 1
            print("lives:" +str(lives))
            print("That number is too low! Try a higher number!")
            guess = int(input("Enter a number from 1 to 1000: "))

level_five()