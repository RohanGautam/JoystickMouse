import pyautogui
from time import time

# pyautogui.moveRel(0, 100, duration=5)

start = pyautogui.position()
while True:
    # print(pyautogui.position())
    current = pyautogui.position()
    previous = start

    if current!=previous:
        print("Started")

