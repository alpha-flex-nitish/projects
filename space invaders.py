#!/usr/bin/env python

import pygame,sys
from pygame.locals import *

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1600,900)) #800*600,1600*900

pygame.mouse.set_visible(0)
ship = pygame.image.load("C:\\Users\\Nitish Shankar\\PycharmProjects\\pythonTuts\\image\\shiplal.png")
# ship = pygame.image.loads("image/ship.png")
# ship = pygame.image.load("ship")
ship_top = screen.get_height() - ship.get_height()
ship_left = screen.get_width()/2 - ship.get_width()/2

screen.blit(ship, (ship_left,ship_top))

shot = pygame.image.load("C:\\Users\\Nitish Shankar\\PycharmProjects\\pythonTuts\\image\\laldot.png")
shoot_y = 0

while True:
    clock.tick(60)
    screen.fill((0,0,0))
    x,y = pygame.mouse.get_pos()
    screen.blit(ship,(x-ship.get_width()/2,ship_top))
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                shoot_y = 500
                shoot_x = x
    if shoot_y > 0:
        screen.blit(shot,(shoot_x, shoot_y))
        shoot_y -= 10

    pygame.display.update()

