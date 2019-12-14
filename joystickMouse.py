import pyautogui
import time
import threading

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
        # the movement below needs to be carried out in the background so that start and end for this thing's movement can be picked up by start and end
        # moveMouse_thread = threading.Thread(target=moveMouse, args=(direction,))
        # moveMouse_thread.daemon = True  
        # moveMouse_thread.start()
    
    if(startCount==0 and endCount != 0):
        print("moving")
        # # determining the direction vector based on the start and  end vector. Direction and magnitude based on start and end vectors
        # directionVector = pyautogui.Point(endVector.x - startVector.x, endVector.y - startVector.y)
        # startVector = endVector
        # pyautogui.moveRel(directionVector.x, directionVector.y, duration=1)
        # endVector = pyautogui.position()
        # current = pyautogui.position()



    previous = current
    counter += 1

# how to change direction by user once mouse is moving?
# look at joystick drivers https://github.com/ros-drivers/joystick_drivers_tutorials/blob/master/turtle_teleop/scripts/turtle_teleop_joy.py
# look at if current follows line, if breaks line, form a new line from old pos to new point