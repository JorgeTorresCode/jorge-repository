import random
from termcolor import colored

system = random.randint(1,10)

user = input("\nGuess the number between 1 to 10: ")

try:
    user = int(user)
    choose = colored(f"\nThe system choose: {system}\nYou choose: {user}","light_yellow")

    if user == system:
        print(choose)
        print(colored("\nYou won!","light_green"))
        
    elif user != system and user in range(1,11):
        print(choose)
        print(colored("\nYou lost!","light_red"))
        
    else:
        print(colored("\nNumber not between 1 to 10","light_red"))
    
except:
    print(colored("\nThis is not a number","light_red"))