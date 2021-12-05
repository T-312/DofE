from consts import *
from colors import *
from string import ascii_uppercase
import random

class Shape:
    def __init__(self):
        self = Shape.__init__(self)

    def draw_rectangle(window, color, x_pos, y_pos, width, height):
        pygame.draw.rect(window, color, (x_pos, y_pos, width, height))

    def draw_circle(window, color, x_pos, y_pos, radius, thickness):
        pygame.draw.circle(window, color, (x_pos, y_pos), radius, thickness)

    def draw_line(window, color, x_start_pos, y_start_pos, x_end_pos, y_end_pos, width):
        pygame.draw.line(window, color, (x_start_pos, y_start_pos), (x_end_pos, y_end_pos), width)

    def draw_lines(window, color, points, width):
        pygame.draw.lines(window, color, False, points, width)

def particle(color, x, y, radius, thickness, angle, direction):
    Shape.draw_circle(WIN, color, x, y, radius, thickness)
    x+=direction
    y+=angle

    if x == 700:
        a = random.randint(0, 1)
        if a == 0:
            angle = -2

        if a == 1:
            angle = 5
            direction = -5
    return (angle, direction)

def main():
    running = True
    clock = pygame.time.Clock()

    x, y = 0, 285

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        foil = Shape.draw_rectangle(WIN, YELLOW, 700, 250, 15, 80)
        cover = Shape.draw_circle(WIN, GREEN, 715, 285, 150, 12)
        entrance = Shape.draw_rectangle(WIN, BLACK, 565, 250, 20, 60)

        angle = particle(BLUE, x, y, 20, 20)[0]
        direction = particle(BLUE, x, y, 20, 20)[1]
        particle(BLUE, x, y, 20, 20, angle, direction)
        print(angle)

        x+=5

        pygame.display.update()
        WIN.fill(BLACK)

    pygame.quit()

if __name__ == "__main__":
    main()