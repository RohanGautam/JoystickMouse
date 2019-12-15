import pyautogui
import numpy as np
import time
pyautogui.PAUSE = 0.01 #0.1 by default, making it smaller for lower latency. Failsafe is still usable in this case.

def getUnitVector(npArray):
    '''Returns the direction/unit vector of `npArray`(which is a `np.array`)'''
    unitVec = npArray/np.linalg.norm(npArray)
    # converting the `NaN`'s to 0 
    unitVec[np.isnan(unitVec)] = 0
    return unitVec

scaling_factor = 5
directionVector = np.array([0,0])
direction = getUnitVector(directionVector)*scaling_factor

previous = pyautogui.position()
firstIteration = True
while True:
    current = pyautogui.position()

    if not firstIteration:
        curDirectionVector = np.array([current.x-previous.x, current.y-previous.y])
        vectorLen = np.linalg.norm(curDirectionVector)
        current_direction = getUnitVector(curDirectionVector)*scaling_factor
        # print(np.allclose(current_direction, direction)) # `np.allclose` sees if values are close enough
        same_as_old_dir = np.allclose(current_direction, direction)
        # if it changes direction, make it go in a new direction
        if (same_as_old_dir == False):
            print(f'length of movement vector is {vectorLen}')
            direction = current_direction

    pyautogui.moveRel(direction[0], direction[1])

    previous = current
    firstIteration = False