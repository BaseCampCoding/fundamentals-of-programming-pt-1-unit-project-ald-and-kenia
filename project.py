print('Welcome! Try to guess the correct number to win the game!')
print("For your first round, you get three chances to guess the correct number")
import random
def level_one():
    """ (int) -> int:

    """
    guess = int(input("enter a number from 1 to 10: "))
    num=random.randint(1,10)
    lives = 3 
    while num in range(1,10):
        if guess == num:
            print("Correct!")
            quit()
        elif guess > num :
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
    num = random.randint(1,50)
    lives = 4 
    while num in range(1,50):
        if guess == num:
            print("great job!")
            quit()
        elif guess > num:
            print("that number was too high! take another shot")
            lives -= 1
            print("lives:" +str(lives))
        else: 
            print("that number is too low! try again")
            lives -= 1 
            print("lives:" +str(lives))




