import pyautogui
from time import time

# pyautogui.moveRel(0, 100, duration=5)

startPosition = pyautogui.position()
previous = startPosition
counter, startCount, endCount = 0, 0, 0

startVector, endVector = startPosition, startPosition  # initially
while True:
    current = pyautogui.position()

    if (current != previous) and (startCount == 0):
        print("Started")
        startVector = current
        startCount += 1
        endCount = 0
    # counter%2000==0 to intruduce some delay. make this dependant on time maybe
    elif (current == previous) and (counter % 10000 == 0) and (endCount == 0):
        print("Ended")
        endVector = current
        startCount = 0
        endCount += 1
        # determining the direction vector based on the start and  end vector. Direction and magnitude based on start and end vectors
        direction = pyautogui.Point(endVector.x - startVector.x, endVector.y - startVector.y)
        pyautogui.moveRel(direction.x, direction.y, duration=1) 

    previous = current
    counter += 1
