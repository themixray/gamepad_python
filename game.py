from gamepad import gamepad
import pygame

pygame.init()

pygame.display.set_caption('Game')
win = pygame.display.set_mode((500,500))

player = [0, 0]
speed = 5
clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.JOYBUTTONDOWN:
            print(event.button)
    if gamepad.isPressed('east'):
        run = False
    win.fill((0,0,0))
    if gamepad.isPressed('left') or gamepad.leftJoystick[0] < 0:
        player[0] -= speed
    if gamepad.isPressed('right') or gamepad.leftJoystick[0] > 0:
        player[0] += speed
    if gamepad.isPressed('up') or gamepad.leftJoystick[1] > 0:
        player[1] -= speed
    if gamepad.isPressed('down') or gamepad.leftJoystick[1] < 0:
        player[1] += speed
    if gamepad.isPressed('r2'):
        speed = 15
    else:
        speed = 5
    if gamepad.isPressed('start'):
        gamepad.reset()

    if player[0] >= 500:
        player[0] = -15
    if player[0] < -15:
        player[0] = 500

    if player[1] >= 500:
        player[1] = -15
    if player[1] < -15:
        player[1] = 500

    pygame.draw.rect(win,(255,255,255),pygame.Rect(player,[15,15]))
    clock.tick(25)
    pygame.display.update()
pygame.quit()
