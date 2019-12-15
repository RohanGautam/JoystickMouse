import pyautogui
import numpy as np
import time

pyautogui.PAUSE = 0.01 #0.1 by default, making it smaller for lower latency. Failsafe is still usable in this case.
scaling_factor = 5
movementVectorSum_threshold = 10 # Increase/decrease to make it easier/harder to stop the movement. If the sum of userMovementVectorLengths is less than this, it stops the pointer.
stopVector = np.array([0,0])

def getUnitVector(npArray):
    '''Returns the direction/unit vector of `npArray`(which is a `np.array`)'''
    unitVec = npArray/np.linalg.norm(npArray)
    # converting the `NaN`'s to 0 
    unitVec[np.isnan(unitVec)] = 0
    return unitVec

directionVector = stopVector # initially, so there's no movement
direction = getUnitVector(directionVector)*scaling_factor

previous = pyautogui.position()
firstIteration = True

userMovementVectorLengths=[]
userPreviouslyMoved = False
while True:
    current = pyautogui.position()

    if not firstIteration:
        curDirectionVector = np.array([current.x-previous.x, current.y-previous.y])
        vectorLen = np.linalg.norm(curDirectionVector)
        current_direction = getUnitVector(curDirectionVector)*scaling_factor
        same_as_old_dir = np.allclose(current_direction, direction) # `np.allclose` sees if values are close enough
        # if it changes direction, make it go in a new direction
        if (same_as_old_dir == False):
            userPreviouslyMoved = True
            userMovementVectorLengths.append(vectorLen)
            # change direction
            direction = current_direction
        # the conditions below impose that the below code is run only once after user has moved the pointer manually
        elif same_as_old_dir and  userPreviouslyMoved:
            print(f'collected movement vector sum: => {sum(userMovementVectorLengths)}')
            if (sum(userMovementVectorLengths) < movementVectorSum_threshold):
                direction = stopVector
            userMovementVectorLengths=[]
            userPreviouslyMoved = False        

    pyautogui.moveRel(direction[0], direction[1])

    previous = current
    firstIteration = False