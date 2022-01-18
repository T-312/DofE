import pygame, time, random

pygame.font.init()

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
title = pygame.display.set_caption("Sea Battle")
FPS = 10
FONT = pygame.font.Font(pygame.font.get_default_font(), 46)