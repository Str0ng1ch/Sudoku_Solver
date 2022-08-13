import pygame

pygame.init()
pygame.font.init()
SCREEN_SIZE, BACKGROUND_COLOR, LINE_COLOR = 603 // 9 * 9, (240, 240, 240), (0, 0, 0)
FONT_SIZE = int(SCREEN_SIZE // 9 * 0.7)
BLACK, GRAY = (0, 0, 0), (126, 126, 126)
GRAY_LINE_WIDTH, BLACK_LINE_WIDTH = 1, 3
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))


def draw_lines(number, color, width):
    for i in range(SCREEN_SIZE // number, SCREEN_SIZE, SCREEN_SIZE // number):
        pygame.draw.line(screen, color, (0, i), (SCREEN_SIZE, i), width)
        pygame.draw.line(screen, color, (i, 0), (i, SCREEN_SIZE), width)


def draw_numbers(field):
    font = pygame.font.SysFont('Comic Sans MS', FONT_SIZE)
    for i in range(9):
        y_cords = SCREEN_SIZE // 9 * i
        for j in range(9):
            x_cords = SCREEN_SIZE // 9 * j + SCREEN_SIZE // 18 - FONT_SIZE // 3.2
            if field[i][j] == 1:
                x_cords += FONT_SIZE // 12.8
            text = font.render(str(field[i][j]), False, LINE_COLOR)
            screen.blit(text, (x_cords, y_cords))


def graphics_main(field):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            pygame.draw.rect(screen, BACKGROUND_COLOR, (0, 0, SCREEN_SIZE, SCREEN_SIZE))
            draw_lines(9, GRAY, GRAY_LINE_WIDTH)
            draw_lines(3, BLACK, BLACK_LINE_WIDTH)
            draw_numbers(field)
            pygame.display.flip()
    pygame.font.quit()
    pygame.quit()
