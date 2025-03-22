# My version --------------------------------------

# import pyautogui as pau
# import keyboard as key
# import time 

# time.sleep(5)
# cps = 35
# while True:
#     pau.click()
#     time.sleep(1/cps)


#     if key.is_pressed("k"):
#         break



# Internet v1

# import time
# import threading
# from pynput.mouse import Controller, Button
# from pynput.keyboard import Listener, KeyCode

# toggle_key = KeyCode(char="k")
# clicking = False
# mouse = Controller

# def clicker():
#     while True:
#         if clicking:
#             mouse.click(Button.left, 1)
#         time.sleep(0.001)

# def toggle_event(key):
#     if key == toggle_key:
#         global clicking
#         clicking = not clicking

# click_thread = threading.Thread(target=clicker)
# click_thread.start()

# with Listener(on_press=toggle_event) as listener:
#     listener.join()

#internet v2

# import pyautogui as pau
# from pynput.keyboard import *

# delay = 0.1
# trigger_key = KeyCode.from_char("k")
# exit_key = Key.f1
# paused = True
# running = True

# def on_press(key):
#     global paused, running
#     if key == trigger_key:
#         if paused:
#             paused = False
#         else:
#             paused = True

#     elif key == exit_key:
#         running = False

# def main():
#     lis = Listener(on_press=on_press)
#     lis.start()

#     while running:
#         if not running:
#             pau.click(pau.position())
#             pau.PAUSE = delay
#     lis.stop()

# if __name__ == "__main__":
#     main()