import pygame, sys

from pygame.locals import*

from components import button, popUp
from random import randint

import settings, game, loading


pygame.init()

size = (1024, 576)
color = (23, 35, 39)

display = pygame.display.set_mode(size)
pygame.display.set_caption('Tic Tac Toe')

image_of_x = pygame.image.load('../images/x.png')
image_of_x = pygame.transform.scale(image_of_x, [55, 55])

image_of_o = pygame.image.load('../images/o.png')
image_of_o = pygame.transform.scale(image_of_o, [55, 55])


button_game = pygame.Rect(size[0]/2 - (350/2), 90, 350, 80)
button_settings = pygame.Rect(size[0]/2 - (350/2), 250, 350, 80)
button_exit = pygame.Rect(size[0]/2 - (350/2), 400, 350, 80)

button_color = [[70, 212, 106], [70, 212, 106], [70, 212, 106]]

backgroundSound = pygame.mixer.music.load('../sounds/Awaken.mp3')

pygame.mixer.music.play(-1)

music = 'play'

def drawMain(color):

    font = pygame.font.SysFont('Arial', 15, True, False)

    text1 = font.render("Jogo desenvolvido por Carlos Mateus", True, color)
    text2 = font.render("Visita a minha conta do github: carlosmatateumateus", True, color)
    
    
    display.blit(image_of_x, [size[0]/2 - (350/2), 25])
    display.blit(image_of_o, [size[0]/2 - (350/2) + 50, 25])
    display.blit(text1, [390, 510])
    display.blit(text2, [330, 540])
   

def menu(playMusic = False):

    optionsPopUp = [
        pygame.Rect(400, 320, 80, 35),
        pygame.Rect(540, 320, 80, 35)

    ]
    exitNow = False
    
    

    colorBackgroundPopUp = [
        [100, 100, 100],
        [100, 100, 100]
    ]


    while (True):

        mouse = pygame.Rect(pygame.mouse.get_pos()[0] - 5, pygame.mouse.get_pos()[1] - 5, 1, 1)

        display.fill(color)

        for events in pygame.event.get():
            if events.type == QUIT:
               exitNow = True
            

        drawMain([202, 202, 202]
)

        button(title="Jogar", display=display, rect=button_game, position_x_title=485, position_y_title=123, colorBackground=button_color[0], borderRadious=15)
        button(title="Definições", display=display, rect=button_settings, position_x_title=453, position_y_title=280, colorBackground=button_color[1], borderRadious=15)
        button(title="Sair", display=display, rect=button_exit, position_x_title=493, position_y_title=430, colorBackground=button_color[2], borderRadious=15)

        pygame.draw.rect(display, "#000000", mouse)
        if (exitNow == False):
            if (mouse.colliderect(button_game)):
                button_color[0] = [100, 172, 236]

                if pygame.mouse.get_pressed()[0]:
                    loading.loading()
                    game.game()

            else:
                button_color[0] = [70, 212, 106]

            if (mouse.colliderect(button_settings)):
                button_color[1] = [115, 115, 115]
                
                if pygame.mouse.get_pressed()[0]:
                    settings.settings()
            else:
                button_color[1] = [70, 212, 106]

            if (mouse.colliderect(button_exit)):
                button_color[2] = [230, 62, 76]

                if pygame.mouse.get_pressed()[0]:
                    exitNow = True
            else:
                button_color[2] = [70, 212, 106]


        if (exitNow):
            popUp(display, pygame.transform.scale(pygame.image.load('../images/warning.png'), [80, 80]), 'Queres realmente sair?', 430, 295)
            option1 = button("Não", display, optionsPopUp[0], 423, 327, [75, 75, 75], [200, 250, 200], borderRadious=3, fontSize=17)
            option2 = button("Sim", display, optionsPopUp[1], 563, 327, [75, 75, 75], [200, 250, 200], borderRadious=3, fontSize=17)
            
            if (mouse.colliderect(optionsPopUp[0])):
                if (pygame.mouse.get_pressed()[0] == True):
                    exitNow = False

            if (mouse.colliderect(optionsPopUp[1])):
                if (pygame.mouse.get_pressed()[0] == True):
                    pygame.quit()
                    exit()

        pygame.display.flip()

if __name__ == '__main__':
    menu()