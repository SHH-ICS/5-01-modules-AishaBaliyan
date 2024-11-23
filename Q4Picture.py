# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.
import pygame
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Q4Picture")

PINK = (255, 192, 203)
PURPLE = (128, 0, 128)
BLUE = (0, 0, 255)

screen.fill((255, 255, 255)) 

diamond_points = [(200, 100), (250, 150), (200, 200), (150, 150)]
pygame.draw.polygon(screen, PINK, diamond_points)
pygame.draw.circle(screen, PURPLE, (100, 300), 50) 
pygame.draw.rect(screen, BLUE, (250, 250, 100, 50)) 
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
pygame.quit()
