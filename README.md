# JoystickMouse 🕹️
A script to emulate joystick-like cursor movement using a mouse/trackpad.

## Requirements
* pyautogui, `pip install pyautogui`
* numpy, `pip install numpy`

> By default, moving the mouse to any corner of the screen stops the script, owing to `pyautogui`'s built in fail safe. You can set  `pyautogui.FAILSAFE` to `False` to avoid this, but it is *not recommended.*

## How it works
* Cursor continues in the direction that the user moves it in.
* Small movement in a direction = cursor continues moving slowly
* Large movement in a direction = cursor continues moving fast
* making a small movement in an opposing direction (while the cursor is moving) stops the movement.
