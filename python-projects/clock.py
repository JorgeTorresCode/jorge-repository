import tkinter as tk
from datetime import datetime

def hour_updater():
    current_time = datetime.now().strftime("%H:%M:%S")
    
    #Update the text with the current time
    label_hour.config(text=current_time)
    
    #Update time (microseconds)
    window.after(1000, hour_updater)
    

def font_updater(event=None):
    new_font = max(24, window.winfo_width() // 10)
    label_hour.config(font=("Bookman Old Style", new_font))


#Creating black window with title clock
window = tk.Tk()
window.configure(bg="black")
window.title("Clock")

#Making a label to show the hour
label_hour = tk.Label(window, font=("Bookman Old Style", 50), fg="white", bg="black")
label_hour.grid(row=0, column=0, padx=15, pady=15)

#Configure grid weights to make label size in proportion to window size
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

#When the geometry is modified, the lambda event execute. F11 and Esc events
window.bind("<Configure>", lambda event: font_updater())
window.bind("<F11>", lambda event: window.attributes("-fullscreen", True))
window.bind("<Escape>", lambda event: window.attributes("-fullscreen", False))

#Start the clock and the loop
hour_updater()
window.mainloop()