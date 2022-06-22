import gui
import shape
import pygame
import rules


def main(win):
    locked_positions = {}
    grid = gui.create_grid(locked_positions)
    last_score = gui.max_score()

    change_piece = False
    run = True
    current_piece = shape.get_shape(shape.shapes)
    next_piece = shape.get_shape(shape.shapes)
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.3
    level_time = 0
    score = 0

    gui.draw_window(win, grid, score, last_score)

    while run:
        grid = gui.create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        if level_time / 1000 > 5: #co 5s gra przyspiesza
           if fall_speed > 0.006:
               fall_speed -= 0.005
           level_time = 0

        if fall_time / 1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (rules.valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not (rules.valid_space(current_piece, grid)):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not (rules.valid_space(current_piece, grid)):
                        current_piece.x -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not (rules.valid_space(current_piece, grid)):
                        current_piece.y -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not (rules.valid_space(current_piece, grid)):
                        current_piece.rotation -= 1

        shape_pos = gui.convert_shape_format(current_piece)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color  # np [ (1,2):(155,233,233) ]

            current_piece = next_piece
            next_piece = shape.get_shape(shape.shapes)
            change_piece = False
            score += gui.clear_rows(grid, locked_positions) * 10

        gui.draw_window(win, grid, score, last_score)
        gui.draw_next_shape(next_piece, win)
        pygame.display.update()

        if rules.check_lost(locked_positions):
            gui.draw_text_middle(win, " You lost :( ", 80, (200, 100, 50))
            gui.update_score(score)
            gui.draw_window(win, grid, score, last_score)
            pygame.display.update()
            pygame.time.delay(1500)
            run = False
            #gui.update_score(score)
