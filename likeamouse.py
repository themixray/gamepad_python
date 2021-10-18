from pynput.mouse import Button, Controller
from gamepad import gamepad
import keyboard
import time

mouse = Controller()
def b():
    keyboard.press('ctrl+z')
    time.sleep(0.01)
    keyboard.release('ctrl+z')
gamepad.eastPressCallback = b
gamepad.northPressCallback = lambda: mouse.press(Button.middle)
gamepad.northReleaseCallback = lambda: mouse.release(Button.middle)
gamepad.R2PressCallback = lambda: mouse.press(Button.left)
gamepad.R2ReleaseCallback = lambda: mouse.release(Button.left)
gamepad.L2PressCallback = lambda: mouse.press(Button.right)
gamepad.L2ReleaseCallback = lambda: mouse.release(Button.right)
def up(): mouse.position = (mouse.position[0], mouse.position[1]-25)
def down(): mouse.position = (mouse.position[0], mouse.position[1]+25)
def left(): mouse.position = (mouse.position[0]-25, mouse.position[1])
def right(): mouse.position = (mouse.position[0]+25, mouse.position[1])
gamepad.upPressCallback = up
gamepad.downPressCallback = down
gamepad.leftPressCallback = left
gamepad.rightPressCallback = right

while True:
    mouse.position = (mouse.position[0]+int(gamepad.leftJoystick[0]/1500),
                      mouse.position[1]-int(gamepad.leftJoystick[1]/1500))
    time.sleep(0.02)
