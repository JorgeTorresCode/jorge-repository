import pyautogui
import keyboard

while True:
    pixel1 = pyautogui.pixel(510, 665)
    pixel2 = pyautogui.pixel(510, 579)
    
    if pixel1 == (0, 0, 0) or pixel1 == (172, 172, 172) or pixel2 == (0, 0, 0) or pixel2 == (172, 172, 172):
        keyboard.press("space")