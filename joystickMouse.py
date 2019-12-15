import pyautogui
import numpy as np
import time

pyautogui.PAUSE = 0.01 #0.1 by default, making it smaller for lower latency. Failsafe is still usable in this case.
scaling_factor = 100
movementVectorSum_threshold = 10 # Increase/decrease to make it easier/harder to stop the movement. If the sum of userMovementVectorLengths is less than this, it stops the pointer.
stopVector = np.array([0,0])

def getUnitVector(npArray):
    '''Returns the direction/unit vector of `npArray`(which is a `np.array`)'''
    unitVec = npArray/np.linalg.norm(npArray)
    # converting the `NaN`'s to 0 
    unitVec[np.isnan(unitVec)] = 0
    return unitVec

def normalize(movementMagnitude):
    '''Normalises the magnitude of movement. Returns a value between 0 and 1.'''
    # return (movementMagnitude-minimum)/(maximum-minimum)
    w, h = pyautogui.size()
    minimum, maximum = 0, int(np.sqrt(w**2 + h**2))
    return np.interp(movementMagnitude,[minimum, maximum],[4,50])

directionVector = stopVector # initially, so there's no movement
direction = getUnitVector(directionVector)*scaling_factor
direction_unit = getUnitVector(directionVector)

previous = pyautogui.position()
firstIteration = True

userMovementVectorLengths=[]
userPreviouslyMoved = False
while True:
    current = pyautogui.position()

    if not firstIteration:
        curDirectionVector = np.array([current.x-previous.x, current.y-previous.y])
        vectorLen = np.linalg.norm(curDirectionVector)
        movementVectorLengthSum = sum(userMovementVectorLengths)
        current_direction = getUnitVector(curDirectionVector)*normalize(movementVectorLengthSum)
        current_direction_unit = getUnitVector(curDirectionVector)
        # `np.allclose` sees if values are close enough
        same_as_old_dir = np.allclose(current_direction_unit, direction_unit) # TODO : will not be the same as current_direction changes wth magnitude
        # if it changes direction, make it go in a new direction
        if (same_as_old_dir == False):
            userPreviouslyMoved = True
            userMovementVectorLengths.append(vectorLen)
            # change direction
            # move fast/slow depending on magnitude of user-generated movement
            # if(np.linalg.norm(current_direction)!=0):
            #     direction = current_direction
            direction = current_direction  #*scaling_factor
            direction_unit = current_direction_unit
            # print(f'changed! vector : {direction}, normalised vector len {normalize(movementVectorLengthSum)}')
        # the conditions below impose that the below code is run only once after user has moved the pointer manually
        elif same_as_old_dir and  userPreviouslyMoved:
            movementVectorLengthSum = sum(userMovementVectorLengths)
            print(f'collected movement vector sum: => {movementVectorLengthSum}, scaling factor is {normalize(movementVectorLengthSum)}')
            if (sum(userMovementVectorLengths) < movementVectorSum_threshold):
                direction = stopVector
            # print(f'direction vector {direction}')
            userMovementVectorLengths=[]
            userPreviouslyMoved = False        

    pyautogui.moveRel(direction[0], direction[1])

    previous = current
    firstIteration = False