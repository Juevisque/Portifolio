import pyautogui
import time
import keyboard


time.sleep(5)
frase = "ENTRA AI"
res = frase.split(" ")
while keyboard.is_pressed("p") == False:
    for word in res:
        pyautogui.write(word)
        pyautogui.press("Enter")
        time.sleep(0.05)
    
