import random
import time
import pygame
import math
from pynput import keyboard

wide = 450
height = 800

camera_x = 0
camera_y = 0
camera_z = 0
camera_direction = 0
distanceToScreen = 300

def ImgPosition(image, x_1, y_1):
    x_1 = x_1 + height / 2
    y_1 = y_1 * -1 + wide / 2
    image.center = (x_1, y_1)

def ImgSize(image, size):
    image.size = (size, size)

def projection3d(image, x, y, z):
    if z != 0:
        ImgPosition(image, x * (distanceToScreen / z), y * (distanceToScreen / z))
        ImgSize(image, 50 * (distanceToScreen / z))
    else:
        ImgPosition(image, 0, 0)
        ImgSize(image, 0)

def rotationMatrix_x(x, z, direction):
    rotated_x = (z * math.sin(math.radians(direction))) + (x * math.cos(math.radians(direction)))
    return rotated_x

def rotationMatrix_z(x, z, direction):
    rotated_z = (z * math.cos(math.radians(direction))) - (x * math.sin(math.radians(direction)))
    return rotated_z

def ObjectControler(image, object_x, object_y, object_z):
    projection3d(image, rotationMatrix_x(object_x - camera_x, object_z - camera_z, 0 - camera_direction), object_y -
                 camera_y, rotationMatrix_z(object_x - camera_x, object_z - camera_z, 0 - camera_direction))

def ObjectCreator(screen, image, x, y, z):
    ObjectControler(image, x, y, z)
    pygame.draw.rect(screen, (155, 155, 155), image)

def camera():
    global camera_x
    global camera_y
    global camera_z
    global camera_direction
    
    #char = 's'
    
    if char == 'd':
    	camera_direction += 5
    elif char == 'a':
    	camera_direction += -5
    elif char == 'w':
    	camera_x += 5 * math.sin(math.radians(camera_direction))
    	camera_z += 5 * math.cos(math.radians(camera_direction))
    elif char == 's':
    	camera_x += -5 * math.sin(math.radians(camera_direction))
    	camera_z += -5 * math.cos(math.radians(camera_direction))

    with keyboard.Events() as events:

        event = events.get(1e6)

    if event.key == keyboard.KeyCode.from_char('d'):
        camera_direction += 5
    elif event.key == keyboard.KeyCode.from_char('a'):
        camera_direction += -5
    elif event.key == keyboard.KeyCode.from_char('w'):
        camera_x += 5 * math.sin(math.radians(camera_direction))
        camera_z += 5 * math.cos(math.radians(camera_direction))
    elif event.key == keyboard.KeyCode.from_char('s'):
        camera_x += -5 * math.sin(math.radians(camera_direction))
        camera_z += -5 * math.cos(math.radians(camera_direction))

def main():
    screen = pygame.display.set_mode((height, wide))
    run = True

    pygame.init()
    pygame.display.set_caption("3D test")

    image_1 = pygame.Rect(0, 0, 1, 1)
    image_2 = pygame.Rect(0, 0, 1, 1)
    image_3 = pygame.Rect(0, 0, 1, 1)
    image_4 = pygame.Rect(0, 0, 1, 1)
    image_5 = pygame.Rect(0, 0, 1, 1)
    image_6 = pygame.Rect(0, 0, 1, 1)
    image_7 = pygame.Rect(0, 0, 1, 1)
    image_8 = pygame.Rect(0, 0, 1, 1)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill((0, 0, 0))

        #image = ImgSize(1)
        #ImgPositinn(image, 0, 0)
        ObjectCreator(screen, image_1,  100,  100, 300)
        ObjectCreator(screen, image_2, -100,  100, 300)
        ObjectCreator(screen, image_3,  100, -100, 300)
        ObjectCreator(screen, image_4, -100, -100, 300)
        ObjectCreator(screen, image_5,  100,  100, 100)
        ObjectCreator(screen, image_6, -100,  100, 100)
        ObjectCreator(screen, image_7,  100, -100, 100)
        ObjectCreator(screen, image_8, -100, -100, 100)
        camera()
        pygame.time.wait(1000)

        #pygame.draw.rect(screen, (100, 100, 100), image)
        #pygame.draw.rect(screen, (110, 110, 110), image_2)

        pygame.display.update()

if __name__ == "__main__":
    main()