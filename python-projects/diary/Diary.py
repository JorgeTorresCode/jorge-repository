#Diary app where users can write and save their thoughts and also read their entry. Put date

import pandas as pd
from termcolor import colored
from datetime import datetime
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

current_time = datetime.now().replace(second=0 ,microsecond=0)

path = "C:/Users/jorgi/OneDrive/Documentos/Git/jorge-repository/python-projects/diary/Diary.csv"
df = pd.read_csv(path)


def write():
    df = pd.read_csv(path)
    
    while True:
        thought = input("\nWrite here: ")
        thoughti = thought.replace(" ","")
        
        if len(thoughti) > 0:
            break
                    
        else:
            print(colored("You have to write anything","light_red"))


    new_row = pd.DataFrame({"date": [current_time], "thoughts": [thought]})

    #Concatenate df's to write the new_row into diary.csv
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(path, index=False)
    
    print(colored("\nSuccessfully written\n","light_green"))


def show():
    #Read the file again to show the things you write in the same code execution
    df = pd.read_csv(path)
    
    if df.empty:
        print(colored("\nYour diary is empty","light_cyan"))
    
    else:
        df['date'] = pd.to_datetime(df['date'])
        
        print(colored("\nHere is your diary:\n","light_magenta"))

        for index, row in df.iterrows():
            #Delete seconds
            formatted_time = row['date'].strftime("%H:%M")
            
            print(f"The day {colored(row['date'].date(),"light_cyan")} at {colored(formatted_time,"light_cyan")} you wrote:\n{colored(row['thoughts'],"yellow")}\n")


while True:
    print(colored("\nYou opened your diary", "light_blue"))
    
    while True:
        
        print("""\n1. Write something in your diary\n2. Read your diary\n3. Close your diary\n""")
    
        selection = input(f"Choose an option: ")

        if selection == "1":
            write()
    
        elif selection == "2":
            show()
        
        elif selection == "3":
            print(colored("Closed","light_blue"))
            exit()
    
        else:
            print(colored("Non-existent option","light_red"))