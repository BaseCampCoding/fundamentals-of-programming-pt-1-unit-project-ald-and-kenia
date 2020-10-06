print('Welcome! Try to guess the correct number to win the game!')
print("For your first round, you get three chances to guess the correct number")
import random
def level_one():
    """ (int) -> int:

    """
    guess = int(input("enter a number from 1 to 10: "))
    num1=random.randint(1,10)
    lives = 3 
    while num1 in range(1,10):
        if guess == num1:
            print("Correct!")
            quit()
        elif guess > num1 :
            print("Try again! Too high!")
            lives -= 1
            print("lives:" +str(lives))
            guess = int(input("enter a number from 1 to 10: "))
        else:
            print("Try Again! Too low")
            lives -= 1
            print("lives:" +str(lives))
            guess = int(input("enter a number from 1 to 10: "))
level_one()
def level_two():
    """ (int) -> int:

    """ 
    guess = int(input("enter a number from 1 to 10: "))
    num2 = random.randint(1,50)
    while num2 in range(1,50):
        if guess == num2:
            print("great job!")
            quit()
        elif guess > num2:
            print("that number was too high! take another shot")
            guess = int(input("enter a number from 1 to 50: "))
        else: 
            print("that number is too low! try again")
            guess = int(input("enter a number from 1 to 50: "))

if guess == num1:
    level_two()



