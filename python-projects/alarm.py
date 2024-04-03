import time
from tkinter import *
from datetime import datetime
import contextlib
with contextlib.redirect_stdout(None):
    import pygame

pygame.init()
pygame.mixer.music.load("Python\\Projects\\sound.mp3")

current_time = datetime.now().time()

def alarm():
    current_time = datetime.now().time() 
    def internal():
        current_time = datetime.now().time()
        data = f"{hour.get()}:{min.get()}:{current_time.strftime("%S")}"
        
        if current_time.strftime("%H:%M:%S") == data:
            message.config(text="Alarm ringing...")
            pygame.mixer.music.play(1)
        
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            
            message.config(text=f"The alarm rang at {hour.get()}:{min.get()}")
            
        else:
            window.after(1000, internal)
    
    try:
        if int(hour.get()) in range(24) and int(min.get()) in range(60) and min.get() > current_time.strftime("%M") and hour.get() >= current_time.strftime("%H"):
            internal()
            message.config(text=f"Alarm set at {hour.get()}:{min.get()}")
        
        else:
            message.config(text="Invalid time")
            hour.delete(0, END)
            min.delete(0, END)
            
    except:
            message.config(text="Invalid time")
            hour.delete(0, END)
            min.delete(0, END)
            

    
window = Tk()

label = Label(window, text="Set the alarm hour")
label.grid(row=0, columnspan=3, )

point = Label(window, text=":")
point.grid(row=1, column=1)

hour = Entry(window, width=3, borderwidth=2)
hour.grid(row=1, column=0)

min = Entry(window, width=3, borderwidth=2)
min.grid(row=1, column=2)

message = Label(window, text="")
message.grid(row=3, column=1)

button = Button(window, text="Set alarm",width=8, command=alarm)
button.grid(row=2, column=1)

window.mainloop()