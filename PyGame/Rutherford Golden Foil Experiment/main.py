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
    
def main():
    running = True
    clock = pygame.time.Clock()
    
    angle = 0
    x, y, z = 0, 285, 0
    current = 0
    particle_num = 10

    angles = [1] * particle_num
    movement = [random.randint(0, 3) for i in range(particle_num+1)]

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        foil = Shape.draw_rectangle(WIN, YELLOW, 700, 250, 15, 80)
        cover = Shape.draw_circle(WIN, GREEN, 715, 285, 150, 12)
        entrance = Shape.draw_rectangle(WIN, BLACK, 565, 250, 20, 60)

        for i in range(particle_num):
            if x-current >= 700:
                if movement[i] == 0:
                    angle = 0
                    angles[i]+=1

                if movement[i] == 1:
                    angle = 2*angles[i]
                    angles[i]+=1

                if movement[i] == 2:
                    angle = -2*angles[i]
                    angles[i]+=1

                if movement[i] == 3:
                    angle = 2*angles[i]
                    angles[i]+=1
                    Shape.draw_circle(WIN, BLUE, x-z, y+angle, 10, 10)

            # Shape.draw_circle(WIN, BLUE, x-current, y+angle, 10, 10)
            current-=60

        if x+current >= 900:
            x, y = 0, 285
            angles = [1] * particle_num
            movement = [random.randint(0, 2) for i in range(particle_num+1)]

        current = 0
        angle = 0

        x+=5
        if x >= 695:
            z+=10

        pygame.display.update()
        WIN.fill(BLACK)

    pygame.quit()

if __name__ == "__main__":
    main()