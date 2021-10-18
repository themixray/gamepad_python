import inputs
import threading
import time

class _gamepad:
    def __init__(self):
        self._lasty = ''
        self._lastx = ''
        self.founded = False
        self.buttons = []
        self.leftJoystick = [0, 0]
        self.rightJoystick = [0, 0]
        self.start()
    def tick(self):
        def exc(self):
            if self.founded == False:
                raise Exception('Gamepad not found!')
        threading.Timer(10, lambda: exc(self)).start()
        events = inputs.get_gamepad()
        self.founded = True
        if events:
            for event in events:
                if event.code == 'ABS_X':
                    self.leftJoystickCallback(x=event.state)
                    self.leftJoystick[0] = event.state
                elif event.code == 'ABS_Y':
                    self.leftJoystickCallback(y=event.state)
                    self.leftJoystick[1] = event.state
                elif event.code == 'ABS_RY':
                    self.rightJoystickCallback(y=event.state)
                    self.rightJoystick[1] = event.state
                elif event.code == 'ABS_RX':
                    self.rightJoystickCallback(x=event.state)
                    self.rightJoystick[0] = event.state
                elif event.code == 'BTN_THUMBL':
                    if event.state:
                        self.leftJoystickPressCallback()
                        self.buttons.append('left-joystick')
                    else:
                        self.leftJoystickReleaseCallback()
                        try:
                            self.buttons.remove('left-joystick')
                        except:
                            pass
                elif event.code == 'BTN_THUMBR':
                    if event.state:
                        self.rightJoystickPressCallback()
                        self.buttons.append('right-joystick')
                    else:
                        self.rightJoystickReleaseCallback()
                        try:
                            self.buttons.remove('right-joystick')
                        except:
                            pass
                elif event.code == 'BTN_TL':
                    if event.state:
                        self.L1PressCallback()
                        self.buttons.append('l1')
                    else:
                        self.L1ReleaseCallback()
                        try:
                            self.buttons.remove('l1')
                        except:
                            pass
                elif event.code == 'BTN_TR':
                    if event.state:
                        self.R1PressCallback()
                        self.buttons.append('r1')
                    else:
                        self.R1ReleaseCallback()
                        try:
                            self.buttons.remove('r1')
                        except:
                            pass
                elif event.code == 'ABS_Z':
                    if event.state == 255:
                        self.L2PressCallback()
                        self.buttons.append('l2')
                    elif event.state == 0:
                        self.L2ReleaseCallback()
                        try:
                            self.buttons.remove('l2')
                        except:
                            pass
                elif event.code == 'ABS_RZ':
                    if event.state == 255:
                        self.R2PressCallback()
                        self.buttons.append('r2')
                    elif event.state == 0:
                        self.R2ReleaseCallback()
                        try:
                            self.buttons.remove('r2')
                        except:
                            pass
                elif event.code == 'BTN_WEST':
                    if event.state:
                        self.westPressCallback()
                        self.buttons.append('west')
                    else:
                        self.westReleaseCallback()
                        try:
                            self.buttons.remove('west')
                        except:
                            pass
                elif event.code == 'BTN_NORTH':
                    if event.state:
                        self.northPressCallback()
                        self.buttons.append('north')
                    else:
                        self.northReleaseCallback()
                        try:
                            self.buttons.remove('north')
                        except:
                            pass
                elif event.code == 'BTN_EAST':
                    if event.state:
                        self.eastPressCallback()
                        self.buttons.append('east')
                    else:
                        self.eastReleaseCallback()
                        try:
                            self.buttons.remove('east')
                        except:
                            pass
                elif event.code == 'BTN_SOUTH':
                    if event.state:
                        self.southPressCallback()
                        self.buttons.append('south')
                    else:
                        self.southReleaseCallback()
                        try:
                            self.buttons.remove('south')
                        except:
                            pass
                elif event.code == 'ABS_HAT0Y':
                    if event.state == 1:
                        self.downPressCallback()
                        self.buttons.append('down')
                        self._lasty = 'down'
                    elif event.state == -1:
                        self.upPressCallback()
                        self.buttons.append('up')
                        self._lasty = 'up'
                    else:
                        if self._lasty == 'up':
                            self.upReleaseCallback()
                            try:
                                self.buttons.remove('up')
                            except:
                                pass
                        elif self._lasty == 'down':
                            self.downReleaseCallback()
                            try:
                                self.buttons.remove('down')
                            except:
                                pass
                elif event.code == 'ABS_HAT0X':
                    if event.state == 1:
                        self.rightPressCallback()
                        self.buttons.append('right')
                        self._lastx = 'right'
                    elif event.state == -1:
                        self.leftPressCallback()
                        self.buttons.append('left')
                        self._lastx = 'left'
                    else:
                        if self._lastx == 'right':
                            self.rightReleaseCallback()
                            try:
                                self.buttons.remove('right')
                            except:
                                pass
                        elif self._lastx == 'left':
                            self.leftReleaseCallback()
                            try:
                                self.buttons.remove('left')
                            except:
                                pass
                elif event.code == 'BTN_START':
                    if event.state:
                        self.selectPressCallback()
                        self.buttons.append('select')
                    else:
                        self.selectReleaseCallback()
                        try:
                            self.buttons.remove('select')
                        except:
                            pass
                elif event.code == 'BTN_SELECT':
                    if event.state:
                        self.startPressCallback()
                        self.buttons.append('start')
                    else:
                        self.startReleaseCallback()
                        try:
                            self.buttons.remove('start')
                        except:
                            pass
    def start(self):
        self.founded = False
        self._started = True
        def ttcb(self):
            while self._started:
                self.tick()
        threading.Thread(target=lambda:ttcb(self),
                         daemon=True).start()
    def stop(self):
        self._started = False
    def isPressed(self, btn):
        return btn in self.buttons
    def reset(self):
        self._lasty = ''
        self._lastx = ''
        self.buttons = []
        self.leftJoystick = [0, 0]
        self.rightJoystick = [0, 0]
    def leftJoystickCallback(self, x=None, y=None): pass
    def rightJoystickCallback(self, x=None, y=None): pass
    def leftJoystickPressCallback(self): pass
    def leftJoystickReleaseCallback(self): pass
    def rightJoystickPressCallback(self): pass
    def rightJoystickReleaseCallback(self): pass
    def L1PressCallback(self): pass
    def L1ReleaseCallback(self): pass
    def R1PressCallback(self): pass
    def R1ReleaseCallback(self): pass
    def R2PressCallback(self): pass
    def R2ReleaseCallback(self): pass
    def L2PressCallback(self): pass
    def L2ReleaseCallback(self): pass
    def westPressCallback(self): pass
    def westReleaseCallback(self): pass
    def northPressCallback(self): pass
    def northReleaseCallback(self): pass
    def eastPressCallback(self): pass
    def eastReleaseCallback(self): pass
    def southPressCallback(self): pass
    def southReleaseCallback(self): pass
    def southReleaseCallback(self): pass
    def selectPressCallback(self): pass
    def selectReleaseCallback(self): pass
    def startPressCallback(self): pass
    def startReleaseCallback(self): pass
    def upPressCallback(self): pass
    def upReleaseCallback(self): pass
    def downPressCallback(self): pass
    def downReleaseCallback(self): pass
    def leftPressCallback(self): pass
    def leftReleaseCallback(self): pass
    def rightPressCallback(self): pass
    def rightReleaseCallback(self): pass
gamepad = _gamepad()
