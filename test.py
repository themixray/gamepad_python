from gamepad import gamepad
import pygame

pygame.init()

pygame.display.set_caption('Gamepad Test')
win = pygame.display.set_mode((500,600))

def scale(surf, width=None, height=None):
    if height != None and width == None:
        width = int(surf.get_width()*(height/surf.get_height()))
    elif height == None and width != None:
        height = int(surf.get_height()*(width/surf.get_width()))
    return pygame.transform.scale(surf,(width,height))
gamepadsurf = scale(pygame.image.load('test/gamepad.png'), 500)
joysticksurf = scale(pygame.image.load('test/joystick.png'), 75)

clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((255,255,255))
    win.blit(gamepadsurf, (0, 600/2-gamepadsurf.get_height()/2))
    win.blit(joysticksurf, (140+gamepad.leftJoystick[0]/4000,
                            400+int(0-gamepad.leftJoystick[1]/4000)))
    win.blit(joysticksurf, (284+gamepad.rightJoystick[0]/4000,
                            400+int(0-gamepad.rightJoystick[1]/4000)))
    for i in gamepad.buttons:
        try:
            surf = scale(pygame.image.load(f'test/{i}.png'), 500)
            win.blit(surf, (0, 600/2-surf.get_height()/2))
        except:
            pass

    pygame.display.update()
pygame.quit()
