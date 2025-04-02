import pygame
import random

from pygame.examples.resizing_new import screen

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
scren = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("Игра в Тир")
icon =  pygame.image.load("img/Tir.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_rect = target_img.get_rect()
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running= True
while running:
    pass


pygame.quit()