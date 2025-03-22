import pyautogui
import win32api, win32con
import time
import keyboard
import random

# 255, 219, 195

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed("n") == False:

    pic = pyautogui.screenshot(region=(678,332,1274,748))

    width,height = pic.size

    for x in range(0, width, 5):
        for y in range(0,height,5):
            r,g,b = pic.getpixel((x,y))

            if b == 195:
                click(x+678,y+332)
                time.sleep(0.05)
                break

