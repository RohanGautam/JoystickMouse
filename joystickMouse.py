import pyautogui
import numpy as np
import time
pyautogui.PAUSE = 0.01 #0.1 by default, making it smaller for lower latency. Failsafe is still usable in this case.

scaling_factor = 5
# direction = np.array([1,1])
direction = np.array([0,0])
direction_normalized = direction/np.linalg.norm(direction)

direction = direction_normalized*scaling_factor
direction[np.isnan(direction)] = 0

previous = pyautogui.position()

firstIteration = True
while True:
    current = pyautogui.position()

    if not firstIteration:
        current_direction = np.array([current.x-previous.x, current.y-previous.y])
        current_direction_normalized = current_direction/np.linalg.norm(current_direction)
        vectorLen = np.linalg.norm(current_direction)
        current_direction = current_direction_normalized*scaling_factor
        current_direction[np.isnan(current_direction)] = 0
        # print(np.allclose(current_direction, direction)) # `np.allclose` sees if values are close enough
        same_as_old_dir = np.allclose(current_direction, direction)
        # if it changes direction, make it go in a new direction
        if (same_as_old_dir == False):
            print(f'length of movement vector is {vectorLen}')
            if(vectorLen <7):
                direction=np.array([0,0]) # stops it
            else:
                direction = current_direction

    pyautogui.moveRel(direction[0], direction[1])

    previous = current
    firstIteration = False