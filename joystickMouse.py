import pyautogui
from time import time

# pyautogui.moveRel(0, 100, duration=5)

start = pyautogui.position()
previous = start
counter, startCount, endCount = 0, 0, 0

while True:
    current = pyautogui.position()

    if (current != previous) and (startCount == 0):
        print("Started")
        startCount += 1
        endCount = 0
    # counter%2000==0 to intruduce some delay. make this dependant on time maybe
    elif (current == previous) and (counter % 2000 == 0) and (endCount == 0):
        print("Ended")
        startCount = 0
        endCount += 1
    previous = current
    counter += 1
