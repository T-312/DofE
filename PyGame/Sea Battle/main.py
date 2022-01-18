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
        Shape.draw_rectangle(WIN, ORANGE, point[0]+3, point[1]+3, 55, 55)

def gen_long_ship():
    tx, ty = random.choice(range(0, 361, 60)), random.choice(range(0, 361, 60))
    orientation = random.choice(['vert', 'hor'])
    if orientation == 'hor':
        points = [(tx, ty), (tx+60, ty), (tx+120, ty), (tx+180, ty)]

    if orientation == 'vert':
        points = [(tx, ty), (tx, ty+60), (tx, ty+120), (tx, ty+180)]

    return points

def gen_double_ship(all_points):
    tx, ty = random.choice(range(0, 361, 60)), random.choice(range(0, 361, 60))
    while (tx, ty) in all_points:
        tx, ty = random.choice(range(0, 361, 60)), random.choice(range(0, 361, 60))

    orientation = random.choice(['vert', 'hor'])
    if orientation == 'hor':
        points = [(tx, ty), (tx+60, ty)]

    if orientation == 'vert':
        points = [(tx, ty), (tx, ty+60)]

    return points

def gen_triple_ship(all_points):
    tx, ty = random.choice(range(0, 361, 60)), random.choice(range(0, 361, 60))
    while (tx, ty) in all_points or (tx+180, ty) in all_points or (tx-180, ty) in all_points or (tx, ty+180) in all_points or (tx, ty-180) in all_points:
        tx, ty = random.choice(range(0, 361, 60)), random.choice(range(0, 361, 60))

    orientation = random.choice(['vert', 'hor'])
    if orientation == 'hor':
        points = [(tx, ty), (tx+60, ty), (tx+120, ty)]

    if orientation == 'vert':
        points = [(tx, ty), (tx, ty+60), (tx, ty+120)]

    return points


def main():
    running = True
    clock = pygame.time.Clock()
    px, py = 0, 0
    points = []
    found = []
    wrong = []

    #Make sure randomly generated ships don't overlay each over
    for c in gen_long_ship():
        points.append(c)

    for i in range(4):
        for c in gen_double_ship(points):
            points.append(c)

    for i in range(4):
        for c in gen_triple_ship(points):
            points.append(c)


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
            if (px, py) in points:
                found.append((px, py))

            else:
                wrong.append((px, py))

        draw_lines()
        mark_user(px, py, RED)
        mark_found(found, wrong)

        if sorted(list(set(found))) == sorted(points):
            print("Victory")
            exit()

        pygame.display.update()
        WIN.fill(BLACK)
    pygame.quit()

if __name__ == "__main__":
    main()