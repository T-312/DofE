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

def draw_lines():
    for x in range(0, 601, 60):
        for y in range(0, 601, 60):
            Shape.draw_line(WIN, WHITE, x, y, x+60, y, 5)
            Shape.draw_line(WIN, WHITE, x, y, x, y+60, 5)

def mark_user(x, y, color):
    Shape.draw_rectangle(WIN, color, x+3, y+3, 55, 55)

def mark_found(found, wrong):
    for point in found:
        Shape.draw_rectangle(WIN, GREEN, point[0]+3, point[1]+3, 55, 55)

    for point in wrong:
        Shape.draw_line(WIN, RED, point[0]+5, point[1]+5, point[0]+55, point[1]+55, 5)
        Shape.draw_line(WIN, RED, point[0]+55, point[1]+5, point[0]+5, point[1]+55, 5)

def gen_squares(num):
    points = []
    while len(points) != num:
        tx, ty = random.choice(range(0, 361, 60)), random.choice(range(0, 361, 60))
        if (tx, ty) not in points:
            points.append((tx, ty))

    return points

def main():
    running = True
    clock = pygame.time.Clock()

    px, py = 0, 0
    target = 40
    turn = 0
    
    turns = {'0' : 1, '1' : 0}
    points = gen_squares(target)
    found = []
    wrong = []

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and py > 0:
            py-=60

        if keys[pygame.K_DOWN] and py+60 < 600:
            py+=60

        if keys[pygame.K_RIGHT] and px+60 < 600:
            px+=60

        if keys[pygame.K_LEFT] and px > 0:
            px-=60

        if keys[pygame.K_RETURN]:
            if (px, py) in points and (px, py) not in found:
                found.append((px, py))
                if len(found) == target:
                    if turn == 0:
                        print("Red Won!")

                    if turn == 1:
                        print("Blue Won!")
                    exit()

            if (px, py) not in points and (px, py) not in wrong:
                wrong.append((px, py))
                turn = turns[str(turn)]

        draw_lines()
        mark_found(found, wrong)
        if turn == 0:
            mark_user(px, py, RED)

        if turn == 1:
            mark_user(px, py, BLUE)

        pygame.display.update()
        WIN.fill(BLACK)
    pygame.quit()

if __name__ == "__main__":
    main()