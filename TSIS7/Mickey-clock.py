import pygame, sys, datetime

pygame.init()

display = pygame.display.set_mode((1000, 800))

def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)

    return rotated_image, new_rect

#images
back = pygame.image.load('Mickey.jpeg')
right = pygame.image.load('m-right-hand.png')
left = pygame.image.load('s-left-hand.png')

back = pygame.transform.scale(back, (1000, 800))
right = pygame.transform.scale(right, (500, 400))
left = pygame.transform.scale(left, (500, 400))

left = pygame.transform.flip(left, 180, 180)

while True:
    #Time
    sec = datetime.datetime.now().second
    min = datetime.datetime.now().minute

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #angle
    x = (-min* 6)%360
    y = (180 + (-6)*sec)%360

    #rot_center
    rot_right, x = rot_center(right, x, 500, 400)
    rot_left, y = rot_center(left, y, 500, 400)

    #set
    display.blit(back, (0, 0))
    display.blit(rot_right, x)
    display.blit(rot_left, y)

    pygame.display.update()
