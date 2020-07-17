import pygame as pg
from os import path

bg = pg.image.load('/Users/dewdr/Documents/Niha/pythongames/Ocean Mania/Seabed Free Vector.jpg')
bgw,bgh = bg.get_rect().size
print(bgw,bgh)
# rect=bg.get_rect()
# print(rect.x)
# print(rect.bottomleft)
# player = pg.image.load('/Users/dewdr/Documents/Niha/pythongames/Ocean Mania/player/playerL.png')
# player = pg.transform.scale(player, (300,100))
# pw,ph = player.get_rect().size
# print(pw,ph)