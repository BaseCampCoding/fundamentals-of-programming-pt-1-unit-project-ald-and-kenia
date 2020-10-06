print('Welcome! Try to guess the correct number to win the game!')
print("For your first round, you get three chances to guess the correct number. Win the level and win a life. Guess incorrect and its Game Over!")
import random
def level_one():
    """ (int) -> int:

    """
    guess = int(input("enter a number from 1 to 10: "))
    num1=random.randint(1,10)
    while num1 in range(1,10):
        if guess == num1:
            print("Correct!")
            quit()
        elif guess > num1 :
            print("Try again! Too high!")
            guess = int(input("enter a number from 1 to 10: "))
        else:
            print("Try Again! Too low")
            guess = int(input("enter a number from 1 to 10: "))

level_one()
def level_two():
    """ (int) -> int:

    """ 
    guess = int(input("enter a number from 1 to 50: "))
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



def level_three():
    """ (int) -> int:

    """ 
    guess = int(input("enter a number from 1 to 100: "))
    num3 = random.randint(1,100)
    while num2 in range(1,100):
        if guess == num3:
            print("great job!")
            quit()
        elif guess > num3:
            print("that number was too high! take another shot")
            guess = int(input("enter a number from 1 to 100: "))
        else: 
            print("that number is too low! try again")
            guess = int(input("enter a number from 1 to 100: "))

