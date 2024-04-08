import pyautogui
import keyboard

color = [(0, 0, 0), (172, 172, 172)]
while True:
    pixel1 = pyautogui.pixel(500, 660)
    pixel2 = pyautogui.pixel(500, 579)
    
    if pixel1 in color or pixel2 in color:
        keyboard.press("up")