print('Welcome! Try to guess the correct number to win the game!')
print("For your first round, you get three chances to guess the correct number.")
print('Win the level and win a life. Guess incorrect and its Game Over!')
import random
def level_one():
    """ (int) -> int:

    """
    guess = int(input("Enter a number from 1 to 10: "))
    num1=random.randint(1,10)
    while num1 in range(1,10):
        if guess == num1:
            print("Correct!")
            break
        elif guess > num1 :
            print("Try again! Too high!")
            guess = int(input("Enter a number from 1 to 10: "))
        else:
            print("Try Again! Too low")
            guess = int(input("Enter a number from 1 to 10: "))

level_one()
def level_two():
    """ (int) -> int:

    """ 
    print("Congratulations! You made it to level two!")
    guess = int(input("Enter a number from 1 to 50: "))
    num2 = random.randint(1,50)
    while num2 in range(1,50):
        if guess == num2:
            print("great job!")
            break
        elif guess > num2:
            print("That number was too high! Take another shot!")
            guess = int(input("Enter a number from 1 to 50: "))
        else: 
            print("That number is too low! Try again")
            guess = int(input("Enter a number from 1 to 50: "))
level_two()

def level_three():
    """ (int) -> int:

    """ 
    guess = int(input("Enter a number from 1 to 100: "))
    num3 = random.randint(1,100)
    while num3 in range(1,100):
        if guess == num3:
            print("Great job!")
            break
        elif guess > num3:
            print("That number was too high! Take another shot")
            guess = int(input("Enter a number from 1 to 100: "))
        else: 
            print("That number is too low! Try again")
            guess = int(input("Enter a number from 1 to 100: "))

level_three()

def level_four():
    """ (int) -> int:

    """ 
    guess = int(input("enter a number from 1 to 500: "))
    num4 = random.randint(1,500)
    while num4 in range(1,500):
        if guess == num4:
            print("Awesome job!")
            break
        elif guess > num4:
            print("That number was too high! Try guessing lower!")
            guess = int(input("Enter a number from 1 to 500: "))
        else: 
            print("That number is too low! Try a higher number!")
            guess = int(input("Enter a number from 1 to 500: "))

level_four()