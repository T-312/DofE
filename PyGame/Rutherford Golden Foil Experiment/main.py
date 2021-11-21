from consts import *
from colors import *
from string import ascii_uppercase

def draw_rectangle(window, color, x_pos, y_pos, width, height):
    pygame.draw.rect(window, color, (x_pos, y_pos, width, height))

def draw_circle(window, color, x_pos, y_pos, radius, thickness):
    pygame.draw.circle(window, color, (x_pos, y_pos), radius, thickness)

def draw_line(window, color, x_start_pos, y_start_pos, x_end_pos, y_end_pos, width):
    pygame.draw.line(window, color, (x_start_pos, y_start_pos), (x_end_pos, y_end_pos), width)

def draw_lines(window, color, points, width):
    pygame.draw.lines(window, color, False, points, width)

def gen_particles(color, radius, width, start_pos):
    pass

def main():
    running = True
    px,py = 100, 300
    clock = pygame.time.Clock()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_circle(WIN, GREEN, px, py, 10, 10)
        px+=5
        if px == 400:
            py+=100

        foil = draw_rectangle(WIN, YELLOW, 400, 250, 15, 80)

        pygame.display.update()
        WIN.fill(BLACK)

    pygame.quit()

if __name__ == "__main__":
    main()