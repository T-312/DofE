from consts import *
from colors import *

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

def gen_hp(num):
    for i in range(num):
        color = random.choice([(255, 255, 255), (0, 255, 0), (255, 255, 0), (0, 0, 255), (255, 165, 0)])
        x, y = random.randint(2, 598), random.randint(2, 598)
        yield [color, (x, y)]

def main():
    running = True
    clock = pygame.time.Clock()
    px, py = 290, 290
    psize = 5

    points = list(gen_hp(500))

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for elem in points:
            color = elem[0]
            x, y = elem[1]
            Shape.draw_circle(WIN, color, x, y, 8, 8)

            if px+psize in range(x, x+9) or px-psize in range(x-8, x+1) or px in range(x-8, x+9):
                if py+psize in range(y, y+8) or py-psize in range(y-8, y):
                    points.remove(elem)
                    psize+=2

                if len(points) == 0:
                    print("Victory")
                    exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and py > 0:
            py-=2

        if keys[pygame.K_DOWN] and py+psize < 600:
            py+=2

        if keys[pygame.K_LEFT] and px > 0:
            px-=2

        if keys[pygame.K_RIGHT] and px+psize < 600:
            px+=2

        Shape.draw_circle(WIN, RED, px, py, psize, psize)

        pygame.display.flip()
        WIN.fill(BLACK)
    pygame.quit()

if __name__ == "__main__":
    main()