print('Welcome! Try to guess the correct number to win the game!')
print("For your first round, you get three chances to guess the correct number")
lives = 3 
import random
guess = int(input("enter a number from 1 to 10: "))
def level_one():
    """ (int) -> int:
    
    """
    num=random.randint(1,10)
    if guess == num:
        print("Correct!")
        quit()
    elif guess > num :
        print("Try again! Too high!")
        lives -= 1
        print("lives:" +str(lives))
    else:
        print("Try Again! Too low")
        lives -= 1
        print("lives:" +str(lives))







