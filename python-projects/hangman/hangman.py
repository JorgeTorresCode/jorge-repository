from termcolor import colored
import random
from Words import words
import re

def getvalidword(words):
    word = random.choice(words)
    while "-" in word or " " in word or "_" in word:
        word = random.choice(words)
    
    return word.upper()


def hangman():
    word = getvalidword(words)
    word_letters = set(word) #Letters in the word
    used_letters = set()
    attempts = 10
    
    #User input
    while len(word_letters) > 0:
        #Letters used
        print("\nYou have used this letters:", ", ".join(used_letters))
        
        #Current word
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))
        
        #Attempts
        print(colored(f"Remaining attempts: {attempts}"))
        
        #Guessed
        
        userletter = input("\nGuess a letter: ").upper()
        
        if userletter.isalpha() and not userletter in used_letters and (len(re.findall(r"\S", userletter)) == 1) and userletter != "Ñ":
            used_letters.add(userletter)
            
            if userletter in word_letters:
                
                word_letters.remove(userletter)
                
                if len(word_letters) == 0:
                    print(colored(f"\n{word}", "light_yellow"))
                    print(colored(f"You guessed the word with {attempts} remaining attempts!\n", "light_green"))
                
                else:
                    print(colored("This letter is in the word", "light_green" ))
                
            else:
                
                if attempts == 1:
                    print(colored(f"\nYou died, the word was {word}", "light_magenta"))
                    break
                
                else:
                    print(colored("This letter is not in the word", "light_red"))
                    attempts -= 1
                
        elif userletter in used_letters:
            print(colored("You have already used that letter", "light_cyan"))
        
        else:
            print(colored("Invalid letter or more than one letters written", "light_red"))

hangman()