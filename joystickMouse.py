import pyautogui
from time import time

# pyautogui.moveRel(0, 100, duration=5)

start = pyautogui.position()
previous = start
counter = 1
while True:
    # print(pyautogui.position())
    current = pyautogui.position()

    if current != previous:
        print("Started") # TODO : show once when started, show "ended" once when ended.
    elif current == previous and counter%2000==0:
        print("Ended")
    previous = current
    counter+=1
