import pyautogui
import keyboard
import time
import cv2

#pic de pedra 1.15s
#pic de ferro 0.75s
#pic de diamante 0.6s
#pic de Netherite 0.5s
#pic de ouro 0.4s


time.sleep(5)

while True:
    if keyboard.is_pressed("n") == False:
        pyautogui.mouseDown(button="left")
        keyboard.press("w")
        time.sleep(0.8)
        keyboard.release("w")

    elif keyboard.is_pressed("n") == True:
        break
    
    else:
        pass
        