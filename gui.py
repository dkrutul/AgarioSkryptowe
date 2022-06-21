import consts
import pygame


def create_grid(locked_pos={}):
    grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]  # kolorowanie planszy 10 x 20

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                grid[i][j] = locked_pos[(j, i)]  # kolorujemy na dany kolor jesli juz cos stoi w danym polu
    return grid


def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions


def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont("Arial", size, bold=True)
    label = font.render(text, True, color)

    surface.blit(label, (consts.top_left_x + consts.play_width / 2 - (label.get_width() / 2),
                         consts.top_left_y + consts.play_height / 2 - label.get_height() / 2))


def draw_grid(surface, grid):
    sx = consts.top_left_x
    sy = consts.top_left_y

    for i in range(len(grid)):
        pygame.draw.line(surface, (0, 200, 100), (sx, sy + i * consts.block_size),
                         (sx + consts.play_width, sy + i * consts.block_size))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (0, 200, 100), (sx + j * consts.block_size, sy),
                             (sx + j * consts.block_size, sy + consts.play_height))


def clear_rows(grid, locked):
    inc = 0  # ilosc rzedow
    for i in range(len(grid) - 1, -1, -1):  # czyscimy rzędy od dołu
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue

    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:  # sortujemy po y i odwracamy
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)

    return inc


def update_score(newScore):
    score = max_score()

    with open('scores.txt', 'w') as file:
        if newScore > int(score):
            file.write(str(newScore))
        else:
            file.write(str(score))


def max_score():
    with open('scores.txt', 'r') as file:
        lines = file.readlines()
        score = lines[0].strip()

    return score


def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('Arial', 30)
    label = font.render('Next Shape:', True, (30, 60, 90))

    sx = consts.top_left_x + consts.play_width + 50
    sy = consts.top_left_y + consts.play_height / 2

    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color,
                                 (sx + j * consts.block_size, sy + i * consts.block_size,
                                  consts.block_size, consts.block_size), 0)

    surface.blit(label, (sx - 20, sy - 50))


def draw_window(surface, grid, score=0, last_score=0):
    surface.fill((0, 0, 0))

    pygame.font.init()

    font = pygame.font.SysFont('Arial', 60)
    label = font.render('Tetris vibes', True, (144, 132, 13))

    surface.blit(label, (consts.top_left_x + consts.play_width / 2 - (label.get_width() / 2), 30))
    # zabawa zeby to bylo na srodku

    #curr score
    font = pygame.font.SysFont('Arial', 30)
    label = font.render('Score: ' + str(score), True, (30, 60, 90))

    sx = consts.top_left_x + consts.play_width + 50
    sy = consts.top_left_y + consts.play_height / 2

    surface.blit(label, (sx + 10, sy + 140))

    #last score
    label = font.render('High Score: ' + str(last_score), True, (30, 60, 90))

    sx = consts.top_left_x - 250
    sy = consts.top_left_y + 200

    surface.blit(label, (sx + 10, sy + 140))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j],
                             (consts.top_left_x + j * consts.block_size,
                              consts.top_left_y + i * consts.block_size, consts.block_size, consts.block_size),
                             0)  # block_size = 30 default

    pygame.draw.rect(surface, (0, 255, 0), (consts.top_left_x, consts.top_left_y,
                                            consts.play_width, consts.play_height), 5)

    draw_grid(surface, grid)
    # pygame.display.update()
