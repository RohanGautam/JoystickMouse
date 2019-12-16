import pyautogui
import numpy as np
import time

pyautogui.PAUSE = 0.01 #0.1 by default, making it smaller for lower latency. Failsafe is still usable in this case.
movementVectorSum_threshold = 10 # Increase/decrease to make it easier/harder to stop the movement. If the sum of userMovementVectorLengths is less than this, it stops the pointer.
stopVector = np.array([0,0])

def getUnitVector(npArray):
    '''Returns the direction/unit vector of `npArray`(which is a `np.array`)'''
    unitVec = npArray/np.linalg.norm(npArray)
    # converting the `NaN`'s to 0 
    unitVec[np.isnan(unitVec)] = 0
    return unitVec

def getScalingFactor(movementMagnitude, rangeLower = 4, rangeUpper = 50):
    '''interpolates `movementMagnitude` to within the range [`rangeLower`, `rangeUpper`]'''
    w, h = pyautogui.size()
    minimum, maximum = 0, int(np.sqrt(w**2 + h**2))
    return np.interp(movementMagnitude,[minimum, maximum],[rangeLower,rangeUpper])

# initially, so there's no movement
direction, direction_unit = stopVector, stopVector

previous = pyautogui.position()
firstIteration = True

userMovementVectorLengths=[]
userPreviouslyMoved = False
while True:
    current = pyautogui.position()

    if not firstIteration:
        curMovementVector = np.array([current.x-previous.x, current.y-previous.y])
        curVectorLen = np.linalg.norm(curMovementVector)
        movementVectorLengthSum = sum(userMovementVectorLengths)
        # scale the unit vector by movement magnitude-based scaling factor
        curDirection = getUnitVector(curMovementVector)*getScalingFactor(movementVectorLengthSum)
        curDirection_unit = getUnitVector(curMovementVector)
        # `np.allclose` sees if unit vectors of previous and current directions are "close enough"
        same_as_old_dir = np.allclose(curDirection_unit, direction_unit)
        # if it changes direction, make it go in a new direction
        if (same_as_old_dir == False):
            userPreviouslyMoved = True
            userMovementVectorLengths.append(curVectorLen)
            # change direction
            direction = curDirection # this is the unit vector, scaled relative to some movement-dependant amount
            # update the direction unit vector
            direction_unit = curDirection_unit
        # the conditions below impose that the below code is run only once after user has moved the pointer manually
        elif same_as_old_dir and  userPreviouslyMoved:
            movementVectorLengthSum = sum(userMovementVectorLengths)
            # if it's a small movement(determined by `movementVectorSum_threshold`), stop movement
            if (sum(userMovementVectorLengths) < movementVectorSum_threshold):
                direction = stopVector
            userMovementVectorLengths=[]
            userPreviouslyMoved = False        

    pyautogui.moveRel(direction[0], direction[1])

    previous = current
    firstIteration = False