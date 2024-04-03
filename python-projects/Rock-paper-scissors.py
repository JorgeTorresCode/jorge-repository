from termcolor import colored
import random

attempts = []

def rock_paper_scissors():
    
    options = ["rock", "paper", "scissors"]
    
    system = random.choice(options)
    
    while True:
        
        print("\nRock, paper or scissors?")
        user = input("Choose one: ")
        
        if user == "1":
            user = options[0]
        
        elif user == "2":
            user = options[1]
            
        elif user == "3":
            user = options[2]
        
        if user.lower() in options:
            break
        
        elif len(attempts) >= 4:
            print(colored("Attemps limit reached, closing the program","light_magenta"))
            exit()
            
        else:
            print(colored("Invalid answer","light_red"))
            attempts.append(1)

    attempts.clear()

    color_user = colored(user.capitalize(),"light_blue")
    color_system = colored(system.capitalize(),"light_blue")
    
    print(f"\nYou chose: {color_user}")
    print(f"The system chose: {color_system}\n",)
    
    user.lower()
    system.lower()
    
    if user == system:
        print(colored("¡Draw!","light_yellow"))
        
    elif (
        (user == "rock" and system == "scissors") or
        (user == "paper" and system == "rock") or
        (user == "scissors" and system == "paper")
        ):
        print(colored("You won!","light_green"))
        
    else:
        print(colored("¡You lost!","light_red"))


while True:
    rock_paper_scissors()
    
    while True:
        Y = colored("Y","light_green")
        N = colored("N","light_red")
        
        print("\nPlay again?")
        selection = input(f"({Y}/{N}): ")
        
        if selection.upper() == "Y":
            break
        
        elif selection.upper() == "N":
            print(colored("\n¡Game over!","light_blue"))
            exit()
            
        elif len(attempts) >= 4:
            print(colored("Attemps limit reached, closing the program","light_magenta"))
            exit()
        
        else:
            print(colored("Invalid answer","light_red"))
            attempts.append(1)