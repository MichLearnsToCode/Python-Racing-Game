import pygame
import time
import math

GRASS = pygame.image.load("img/grass.png")
TRACK = pygame.image.load("img/track.png")

TRACK_BORDER = pygame.image.load("img/track-border.png")
FINISH = pygame.image.load("img/FinishLine.png")

RED_CAR = pygame.image.load("img/red-car.png")
GREEN_CAR = pygame.image.load("img/green-car.png")
GREY_CAR = pygame.image.load("img/grey-car.png")
PURPLE_CAR = pygame.image.load("img/purple-car.png")
WHITE_CAR = pygame.image.load("img/white-car.png")

WIDTH,HEIGHT=TRACK.get_width(),TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Racing Game!")