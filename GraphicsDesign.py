import pygame
from SolveField import SolveField
from GlobalValues import sudoku

pygame.init()
pygame.font.init()
SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR = 603 // 9 * 9, 750, (240, 240, 240)
FONT_SIZE = int(SCREEN_WIDTH // 9 * 0.7)
BLACK, GRAY, RED, BLUE = (0, 0, 0), (126, 126, 126), (255, 0, 0), (0, 0, 255)
GRAY_LINE_WIDTH, BLACK_LINE_WIDTH = 1, 3
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
numbers_font = pygame.font.SysFont('Comic Sans MS', FONT_SIZE)
text_font = pygame.font.SysFont('Comic Sans MS', 25)
rect_backward = pygame.draw.rect(screen, GRAY, (20, 650, 161, 50))
rect_step_by_step = pygame.draw.rect(screen, GRAY, (221, 650, 161, 50))
rect_forward = pygame.draw.rect(screen, GRAY, (422, 650, 161, 50))
current, cords = 0, [(-1, -1)]


def draw_lines(number, color, width):
    for i in range(SCREEN_WIDTH // number, SCREEN_WIDTH + 1, SCREEN_WIDTH // number):
        pygame.draw.line(screen, color, (0, i), (SCREEN_WIDTH, i), width)
        pygame.draw.line(screen, color, (i, 0), (i, SCREEN_WIDTH), width)


def draw_button(rect_cords, text_cords, color, text):
    pygame.draw.rect(screen, GRAY, (rect_cords[0], rect_cords[1], 161, 50))
    text = text_font.render(text, False, color)
    screen.blit(text, (text_cords[0], text_cords[1]))


def draw_text(number, color, x_cords, y_cords):
    text = numbers_font.render(number, False, color)
    screen.blit(text, (x_cords, y_cords))


def draw_numbers(field, special):
    for i in range(9):
        y_cords = SCREEN_WIDTH // 9 * i
        for j in range(9):
            x_cords = SCREEN_WIDTH // 9 * j + SCREEN_WIDTH // 18 - FONT_SIZE // 3.3
            if field[i][j] == 1:
                x_cords += FONT_SIZE // 3.3 // 4
            if len(special) > 0 and (i, j) == special[-1]:
                draw_text(str(field[i][j]), RED, x_cords, y_cords)
            elif (i, j) in special:
                draw_text(str(field[i][j]), BLUE, x_cords, y_cords)
            elif len(str(field[i][j])) == 1 and field[i][j] != 0:
                draw_text(str(field[i][j]), BLACK, x_cords, y_cords)


def graphics_main(field):
    global rect_forward, rect_backward, rect_step_by_step, current, cords

    running = True
    flag = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            pygame.draw.rect(screen, BACKGROUND_COLOR, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
            if flag:
                draw_button((20, 650), (42, 655), BLACK, 'step back')
                draw_button((422, 650), (427, 655), BLACK, 'step forward')
            else:
                draw_button((221, 650), (227, 655), BLACK, 'step by step')
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_forward.collidepoint(pygame.mouse.get_pos()) and flag:
                    if current <= len(arr) - 1:
                        field[arr[current][1]][arr[current][2]] = arr[current][0]
                        cords = ([(arr[i][1], arr[i][2]) for i in range(current + 1)])
                    current += 1 if current < len(arr) else 0
                elif rect_backward.collidepoint(pygame.mouse.get_pos()) and flag:
                    current -= 1 if current > 0 else 0
                    field[arr[current][1]][arr[current][2]] = 0
                    cords = ([(arr[i][1], arr[i][2]) for i in range(current)])
                elif rect_step_by_step.collidepoint(pygame.mouse.get_pos()) and not flag:
                    field = sudoku
                    arr = SolveField(field).step_by_step
                    flag = True
            draw_lines(9, GRAY, GRAY_LINE_WIDTH)
            draw_lines(3, BLACK, BLACK_LINE_WIDTH)
            draw_numbers(field, cords)
            pygame.display.flip()
