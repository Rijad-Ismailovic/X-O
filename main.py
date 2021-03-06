import pygame
from numpy import *

pygame.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
BG = (50, 50, 50)
BLUE = (27, 74, 226)
RED = (176, 10, 10)

grid_img = pygame.image.load("images/grid.png")
x_img = pygame.image.load("images/x.png")
o_img = pygame.image.load("images/o.png")
x_img = pygame.transform.scale(x_img, (75, 75))
o_img = pygame.transform.scale(o_img, (75, 75))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("X/O")
pygame.display.set_icon(grid_img)

def draw(img, coor):
    screen.blit(img, coor)

def fade():
    fade = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    fade = fade.convert()
    fade.fill(BG)
    for i in range(255):
        fade.set_alpha(255-i)
        screen.fill(BG)
        screen.blit(grid_img, (0, 0))
        screen.blit(fade, (0, 0))
        pygame.display.update()

def instructions():
    #font = pygame.font.Font('misc/Made Tommy.otf', 32)
    font = pygame.font.Font('C:/Users/rijad/AppData/Local/Microsoft/Windows/Fonts/8-bit Arcade In.ttf', 25)
    text_1 = font.render("Press R for restart", False, (255, 255, 255))
    text_2 = font.render("goes first", False, (255, 255, 255))
    screen.fill(BG)
    screen.blit(text_1, (35, 100))
    screen.blit(text_2, (105, 150))
    o_img = pygame.transform.scale(pygame.image.load("images/o.png"), (30, 30))
    screen.blit(o_img, (65, 146))
    pygame.display.update()


def run():
    screen.fill(BG)
    screen.blit(grid_img, (0, 0))
    clock = pygame.time.Clock()
    clock.tick(30)

    click = False
    win = False
    turn = 1

    check_11 = True
    check_12 = True
    check_13 = True
    check_21 = True
    check_22 = True
    check_23 = True
    check_31 = True
    check_32 = True
    check_33 = True

    m = array([
        ['/', '/', '/'],
        ['/', '/', '/'],
        ['/', '/', '/']
    ])
    print(m)

    while run:

        mx, my = pygame.mouse.get_pos()

        rect_11 = pygame.Rect(20, 20, 75, 75)
        rect_12 = pygame.Rect(105, 20, 90, 75)
        rect_13 = pygame.Rect(205, 20, 75, 75)
        rect_21 = pygame.Rect(20, 105, 75, 90)
        rect_22 = pygame.Rect(105, 105, 90, 90)
        rect_23 = pygame.Rect(205, 105, 75, 90)
        rect_31 = pygame.Rect(20, 205, 75, 75)
        rect_32 = pygame.Rect(105, 205, 90, 75)
        rect_33 = pygame.Rect(205, 205, 75, 75)

        if rect_11.collidepoint((mx, my)):
            if click:
                if check_11:
                    if not win:
                        if turn == 1:
                            draw(o_img, (20, 20))
                            turn = 2
                            click = False
                            m[0][0] = 'O'
                            check_11 = False
                        elif turn == 2:
                            draw(x_img, (20, 20))
                            turn = 1
                            click = False
                            m[0][0] = 'X'
                            check_11 = False
                else:
                    click = False
                print(m)
        if rect_12.collidepoint((mx, my)):
            if click:
                if check_12:
                    if not win:
                        if turn == 1:
                            draw(o_img, (112, 20))
                            turn = 2
                            click = False
                            m[0][1] = 'O'
                            check_12 = False
                        elif turn == 2:
                            draw(x_img, (112, 20))
                            turn = 1
                            click = False
                            m[0][1] = 'X'
                            check_12 = False
                else:
                    click = False
                print(m)
        if rect_13.collidepoint((mx, my)):
            if click:
                if check_13:
                    if not win:
                        if turn == 1:
                            draw(o_img, (205, 20))
                            turn = 2
                            click = False
                            m[0][2] = 'O'
                            check_13 = False
                        elif turn == 2:
                            draw(x_img, (205, 20))
                            turn = 1
                            click = False
                            m[0][2] = 'X'
                            check_13 = False
                else:
                    click = False
                print(m)
        if rect_21.collidepoint((mx, my)):
            if click:
                if check_21:
                    if not win:
                        if turn == 1:
                            draw(o_img, (20, 112))
                            turn = 2
                            click = False
                            m[1][0] = 'O'
                            check_21 = False
                        elif turn == 2:
                            draw(x_img, (20, 112))
                            turn = 1
                            click = False
                            m[1][0] = 'X'
                            check_21 = False
                click = False
                print(m)
        if rect_22.collidepoint((mx, my)):
            if click:
                if check_22:
                    if not win:
                        if turn == 1:
                            draw(o_img, (112, 112))
                            turn = 2
                            click = False
                            m[1][1] = 'O'
                            check_22 = False
                        elif turn == 2:
                            draw(x_img, (112, 112))
                            turn = 1
                            click = False
                            m[1][1] = 'X'
                            check_22 = False
                else:
                    click = False
                print(m)
        if rect_23.collidepoint((mx, my)):
            if click:
                if check_23:
                    if not win:
                        if turn == 1:
                            draw(o_img, (205, 112))
                            turn = 2
                            click = False
                            m[1][2] = 'O'
                            check_23 = False
                        elif turn == 2:
                            draw(x_img, (205, 112))
                            turn = 1
                            click = False
                            m[1][2] = 'X'
                            check_23 = False
                click = False
                print(m)
        if rect_31.collidepoint((mx, my)):
            if click:
                if check_31:
                    if not win:
                        if turn == 1:
                            draw(o_img, (20, 205))
                            turn = 2
                            click = False
                            m[2][0] = 'O'
                            check_31 = False
                        elif turn == 2:
                            draw(x_img, (20, 205))
                            turn = 1
                            click = False
                            m[2][0] = 'X'
                            check_31  = False
                click = False
                print(m)
        if rect_32.collidepoint((mx, my)):
            if click:
                if check_32:
                    if not win:
                        if turn == 1:
                            draw(o_img, (112, 205))
                            turn = 2
                            click = False
                            m[2][1] = 'O'
                            check_32 = False
                        elif turn == 2:
                            draw(x_img, (112, 205))
                            turn = 1
                            click = False
                            m[2][1] = 'X'
                            check_32 = False
                else:
                    click = False
                print(m)
        if rect_33.collidepoint((mx, my)):
            if click:
                if check_33:
                    if not win:
                        if turn == 1:
                            draw(o_img, (205, 205))
                            turn = 2
                            click = False
                            m[2][2] = 'O'
                            check_33 = False
                        elif turn == 2:
                            draw(x_img, (205, 205))
                            turn = 1
                            click = False
                            m[2][2] = 'X'
                            check_33 = False
                click = False
                print(m)

        #provjera pobjede
        #blue
        if m[0][0] == 'O' and m[0][1] == 'O' and m[0][2] == 'O': #1 - vodoravno - blue
            pygame.draw.line(screen, BLUE, (25, 57), (275, 57), 10)
            win = True
        elif m[1][0] == 'O' and m[1][1] == 'O' and m[1][2] == 'O': #2 - vodoravno - blue
            pygame.draw.line(screen, BLUE, (25, 150), (275, 150), 10)
            win = True
        elif m[2][0] == 'O' and m[2][1] == 'O' and m[2][2] == 'O': #3 - vodoravno - blue
            pygame.draw.line(screen, BLUE, (25, 243), (275, 243), 10)
            win = True
        elif m[0][0] == 'O' and m[1][0] == 'O' and m[2][0] == 'O': #1 - vertikalno - blue
            pygame.draw.line(screen, BLUE, (57, 25), (57, 275), 10)
            win = True
        elif m[0][1] == 'O' and m[1][1] == 'O' and m[2][1] == 'O': #2 - vertikalno - blue
            pygame.draw.line(screen, BLUE, (150, 25), (150, 275), 10)
            win = True
        elif m[0][2] == 'O' and m[1][2] == 'O' and m[2][2] == 'O': #3 - vertikalno - blue
            pygame.draw.line(screen, BLUE, (243, 25), (243, 275), 10)
            win = True
        elif m[0][0] == 'O' and m[1][1] == 'O' and m[2][2] == 'O': #11-5 - dijagonalno - blue
            pygame.draw.line(screen, BLUE, (25, 25), (275, 275), 10)
            win = True
        elif m[2][0] == 'O' and m[1][1] == 'O' and m[0][2] == 'O': #8-2 - dijagonalno - blue
            pygame.draw.line(screen, BLUE, (25, 275), (275, 25), 10)
            win = True
        #red
        elif m[0][0] == 'X' and m[0][1] == 'X' and m[0][2] == 'X': #1 - vodoravno - blue
            pygame.draw.line(screen, RED, (25, 57), (275, 57), 10)
            win = True
        elif m[1][0] == 'X' and m[1][1] == 'X' and m[1][2] == 'X': #2 - vodoravno - blue
            pygame.draw.line(screen, RED, (25, 150), (275, 150), 10)
            win = True
        elif m[2][0] == 'X' and m[2][1] == 'X' and m[2][2] == 'X': #3 - vodoravno - blue
            pygame.draw.line(screen, RED, (25, 243), (275, 243), 10)
            win = True
        elif m[0][0] == 'X' and m[1][0] == 'X' and m[2][0] == 'X': #1 - vertikalno - blue
            pygame.draw.line(screen, RED, (57, 25), (57, 275), 10)
            win = True
        elif m[0][1] == 'X' and m[1][1] == 'X' and m[2][1] == 'X': #2 - vertikalno - blue
            pygame.draw.line(screen, RED, (150, 25), (150, 275), 10)
            win = True
        elif m[0][2] == 'X' and m[1][2] == 'X' and m[2][2] == 'X': #3 - vertikalno - blue
            pygame.draw.line(screen, RED, (243, 25), (243, 275), 10)
            win = True
        elif m[0][0] == 'X' and m[1][1] == 'X' and m[2][2] == 'X': #11-5 - dijagonalno - blue
            pygame.draw.line(screen, RED, (25, 25), (275, 275), 10)
            win = True
        elif m[2][0] == 'X' and m[1][1] == 'X' and m[0][2] == 'X': #8-2 - dijagonalno - blue
            pygame.draw.line(screen, RED, (25, 275), (275, 25), 10)
            win = True


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    run()

        pygame.display.update()

for i in range(0, 4000):
    instructions()
fade()
run()
