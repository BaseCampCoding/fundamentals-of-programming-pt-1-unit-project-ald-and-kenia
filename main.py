import colorama
from colorama import Fore, Style, Back 
colorama.init()
print(Fore.LIGHTGREEN_EX +'Welcome! Try to guess the correct number to win the game! \n '+ Style.RESET_ALL)
print(Fore.LIGHTMAGENTA_EX + "For your first round, you get three chances to guess the correct number. \n"+ Style.RESET_ALL)
print(Fore.LIGHTGREEN_EX +'Win the level and win a life. Guess incorrect and its Game Over! \n '+ Style.RESET_ALL)
print(Fore.RED +"WARNING! THIS GAME IS EXTREMELY HARD. \n " + Style.RESET_ALL)