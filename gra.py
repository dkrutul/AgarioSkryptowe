import pygame
import gui
import inside_game
import consts

pygame.font.init()


def main_menu(win):
    run = True
    while run:
        win.fill((0, 0, 0))
        gui.draw_text_middle(win, 'Press any key to play', 60, (50, 100, 150))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
            if event.type == pygame.KEYDOWN:
                inside_game.main(win)

    pygame.display.quit()


win = pygame.display.set_mode((consts.s_width, consts.s_height))
pygame.display.set_caption('Tetris')
main_menu(win)

