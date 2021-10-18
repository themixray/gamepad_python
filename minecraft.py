from pynput.mouse import Button, Controller
from gamepad import gamepad
import keyboard
import time

mouse = Controller()
def b():
    keyboard.press('escape')
    time.sleep(0.01)
    keyboard.release('escape')
gamepad.eastPressCallback = b
gamepad.startPressCallback = b

gamepad.L1PressCallback = lambda: mouse.scroll(0, 2)
gamepad.R1PressCallback = lambda: mouse.scroll(0, -2)

gamepad.northPressCallback = lambda: keyboard.press('e')
gamepad.northReleaseCallback = lambda: keyboard.release('e')

gamepad.leftJoystickPressCallback = lambda: keyboard.press('shift')
gamepad.leftJoystickReleaseCallback = lambda: keyboard.release('shift')

gamepad.rightJoystickPressCallback = lambda: keyboard.send('f5')

gamepad.southPressCallback = lambda: keyboard.press('space')
gamepad.southReleaseCallback = lambda: keyboard.release('space')

gamepad.R2PressCallback = lambda: mouse.press(Button.left)
gamepad.R2ReleaseCallback = lambda: mouse.release(Button.left)

gamepad.L2PressCallback = lambda: mouse.press(Button.right)
gamepad.L2ReleaseCallback = lambda: mouse.release(Button.right)

while True:
    mouse.position = (mouse.position[0]+int(gamepad.rightJoystick[0]/1500),
                      mouse.position[1]+int(0-gamepad.rightJoystick[1]/1500))
    if gamepad.rightJoystick != [0,0]:
        if gamepad.rightJoystick[0] < 0:
            mouse.position = (mouse.position[0]-25, mouse.position[1])
        elif gamepad.rightJoystick[0] > 0:
            mouse.position = (mouse.position[0]+25, mouse.position[1])
        elif gamepad.rightJoystick[1] > 0:
            mouse.position = (mouse.position[0], mouse.position[1]-25)
        elif gamepad.rightJoystick[1] < 0:
            mouse.position = (mouse.position[0], mouse.position[1]+25)
    if gamepad.leftJoystick != [0,0]:
        if gamepad.leftJoystick[0] < 0:
            keyboard.press('a')
        elif gamepad.leftJoystick[0] > 0:
            keyboard.press('d')
        elif gamepad.leftJoystick[1] > 0:
            keyboard.press('w')
        elif gamepad.leftJoystick[1] < 0:
            keyboard.press('s')
    else:
        keyboard.release('w')
        keyboard.release('s')
        keyboard.release('d')
        keyboard.release('a')
    time.sleep(0.02)
