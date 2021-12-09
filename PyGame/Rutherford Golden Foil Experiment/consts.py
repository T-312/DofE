import pygame

WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE = pygame.display.set_caption("Rutherford Golden Experiment")
FPS = 70

def coordinates(particles, x, y):
    for i in range(particles):
        yield (-60*i, y)

for i in coordinates(2, 0, 285):
    print(i)