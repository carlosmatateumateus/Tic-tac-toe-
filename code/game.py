import pygame, sys
from pygame.locals import*

from components import button, popUp

import menu
from time import sleep

pygame.init()

size = (1024, 576)
color = (23, 35, 39)

image_of_x = pygame.image.load('../images/x.png')
image_of_o = pygame.image.load('../images/o.png')

display = pygame.display.set_mode(size)
pygame.display.set_caption('Tic Tac Toe')


pieces = [
    pygame.Rect(300, 100, 110, 110), pygame.Rect(450, 100, 110, 110), pygame.Rect(600, 100, 110, 110),
    pygame.Rect(300, 250, 110, 110), pygame.Rect(450, 250, 110, 110), pygame.Rect(600, 250, 110, 110),
    pygame.Rect(300, 400, 110, 110), pygame.Rect(450, 400, 110, 110), pygame.Rect(600, 400, 110, 110),
]

anotherButtons = [
    pygame.Rect(0, 0, 40, 40),
    pygame.Rect(50, 0, 40, 40),
    pygame.Rect(100, 0, 40, 40),
    pygame.Rect(140, 0, 40, 40)
]

imagesButtons = [
    pygame.transform.scale(pygame.image.load('../images/exit.png'), [30, 30]),
    pygame.transform.scale(pygame.image.load('../images/replay.png'), [30, 30]),
    pygame.transform.scale(pygame.image.load('../images/cpu.png'), [30, 30]),
    pygame.transform.scale(pygame.image.load('../images/player2.png'), [30, 30])
]

colorBackground = [
    [53, 75, 79], [53, 75, 79], [53, 75, 79],
    [53, 75, 79], [53, 75, 79], [53, 75, 79],
    [53, 75, 79], [53, 75, 79], [53, 75, 79],
    [53, 75, 79], [53, 75, 79], [53, 75, 79],
    [63, 90, 0]
]
def drawTable():

    ...


def game():

    pieceClick = [
        False, False, False,
        False, False, False,
        False, False, False
    ]


    exitNow = False
    win = False
    dont_winner = False

    playerGame = 'x'
    player = [
                image_of_o, image_of_o, image_of_o,
                image_of_o, image_of_o, image_of_o,
                image_of_o, image_of_o, image_of_o
             ]

    checked = [
        0, 0, 0,
        0, 0, 0,
        0, 0, 0
    ]

    winner = 'o'

    gamming = True

    colorBackgroundPopUp = [
        [100, 100, 100],
        [100, 100, 100]
    ]

    optionsPopUp = [
        pygame.Rect(400, 320, 80, 35),
        pygame.Rect(540, 320, 80, 35)

    ]
    while (True):
        mouse = pygame.Rect(pygame.mouse.get_pos()[0] + 3, pygame.mouse.get_pos()[1] + 3, 1, 1)
        display.fill(color)

        for events in pygame.event.get():
            if events.type == QUIT:
                pygame.quit()
                sys.exit()


        drawTable()

        button(display = display, rect=pieces[0], borderRadious=15, colorBackground=colorBackground[0])
        button(display = display, rect=pieces[1], borderRadious=15, colorBackground=colorBackground[1])
        button(display = display, rect=pieces[2], borderRadious=15, colorBackground=colorBackground[2])
        button(display = display, rect=pieces[3], borderRadious=15, colorBackground=colorBackground[3])
        button(display = display, rect=pieces[4], borderRadious=15, colorBackground=colorBackground[4])
        button(display = display, rect=pieces[5], borderRadious=15, colorBackground=colorBackground[5])

        button(display = display, rect=pieces[6], borderRadious=15, colorBackground=colorBackground[6])
        button(display = display, rect=pieces[7], borderRadious=15, colorBackground=colorBackground[7])
        button(display = display, rect=pieces[8], borderRadious=15, colorBackground=colorBackground[8])

        button(display = display, rect=anotherButtons[0], borderRadious=5, colorBackground=colorBackground[9])
        button(display = display, rect=anotherButtons[1], borderRadious=5, colorBackground=colorBackground[10])
        button(display = display, rect=anotherButtons[2], borderRadious=0, colorBackground=colorBackground[11])
        button(display = display, rect=anotherButtons[3], borderRadious=0, colorBackground=colorBackground[12])

        if (gamming == True):
            if (mouse.colliderect(pieces[0])):
                colorBackground[0] =[13, 45, 49]

                if pygame.mouse.get_pressed()[0]:
                    if (pieceClick[0] == False):
                        if (playerGame == 'x'):
                            player[0] = image_of_o
                            playerGame = 'o'
                            print('Click! '+playerGame)
                            checked[0] = playerGame
                        else:
                            player[0] = image_of_x
                            playerGame = 'x'
                            print('Click! '+playerGame)
                            checked[0] = playerGame

                    pieceClick[0] = True

            else:
                colorBackground[0] = [53, 75, 79]

            if (mouse.colliderect(pieces[1])):
                colorBackground[1] =[13, 45, 49]

                if pygame.mouse.get_pressed()[0]:
                    if (pieceClick[1] == False):
                        if (playerGame == 'x'):
                            player[1] = image_of_o
                            playerGame = 'o'
                            checked[1] = playerGame
                        else:
                            player[1] = image_of_x
                            playerGame = 'x'
                            checked[1] = playerGame
                    pieceClick[1] = True

            else:
                colorBackground[1] = [53, 75, 79]
            
            if (mouse.colliderect(pieces[2])):
                colorBackground[2] =[13, 45, 49]

                if pygame.mouse.get_pressed()[0]:
                    if (pieceClick[2] == False):
                        if (playerGame == 'x'):
                            player[2] = image_of_o
                            playerGame = 'o'
                            checked[2] = playerGame
                        else:
                            player[2] = image_of_x
                            playerGame = 'x'
                            checked[2] = playerGame

                    pieceClick[2] = True

            else:
                colorBackground[2] = [53, 75, 79]

            if (mouse.colliderect(pieces[3])):
                colorBackground[3] =[13, 45, 49]

                if pygame.mouse.get_pressed()[0]:
                    if (pieceClick[3] == False):
                        if (playerGame == 'x'):
                            player[3] = image_of_o
                            playerGame = 'o'
                            checked[3] = playerGame
                        else:
                            player[3] = image_of_x
                            playerGame = 'x'
                            checked[3] = playerGame
                    pieceClick[3] = True

            else:
                colorBackground[3] = [53, 75, 79]

            if (mouse.colliderect(pieces[4])):
                colorBackground[4] =[13, 45, 49]

                if pygame.mouse.get_pressed()[0]:
                    if (pieceClick[4] == False):
                        if (playerGame == 'x'):
                            player[4] = image_of_o
                            playerGame = 'o'
                            checked[4] = playerGame
                        else:
                            player[4] = image_of_x
                            playerGame = 'x'
                            checked[4] = playerGame
                    pieceClick[4] = True

            else:
                colorBackground[4] = [53, 75, 79]

            if (mouse.colliderect(pieces[5])):
                colorBackground[5] =[13, 45, 49]

                if pygame.mouse.get_pressed()[0]:
                    if (pieceClick[5] == False):
                        if (playerGame == 'x'):
                            player[5] = image_of_o
                            playerGame = 'o'
                            checked[5] = playerGame
                        else:
                            player[5] = image_of_x
                            playerGame = 'x'
                            checked[5] = playerGame
                    pieceClick[5] = True

            else:
                colorBackground[5] = [53, 75, 79]

            if (mouse.colliderect(pieces[6])):
                colorBackground[6] =[13, 45, 49]

                if pygame.mouse.get_pressed()[0]:
                    if (pieceClick[6] == False):
                        if (playerGame == 'x'):
                            player[6] = image_of_o
                            playerGame = 'o'
                            checked[6] = playerGame
                        else:
                            player[6] = image_of_x
                            playerGame = 'x'
                            checked[6] = playerGame
                    pieceClick[6] = True

            else:
                colorBackground[6] = [53, 75, 79]

            if (mouse.colliderect(pieces[7])):
                colorBackground[7] =[13, 45, 49]

                if pygame.mouse.get_pressed()[0]:
                    if (pieceClick[7] == False):
                        if (playerGame == 'x'):
                            player[7] = image_of_o
                            playerGame = 'o'
                            checked[7] = playerGame
                        else:
                            player[7] = image_of_x
                            playerGame = 'x'
                            checked[7] = playerGame    
                    pieceClick[7] = True

            else:
                colorBackground[7] = [53, 75, 79]

            if (mouse.colliderect(pieces[8])):
                colorBackground[8] =[13, 45, 49]

                if pygame.mouse.get_pressed()[0]:
                    if (pieceClick[8] == False):
                        if (playerGame == 'x'):
                            player[8] = image_of_o
                            playerGame = 'o'
                            checked[8] = playerGame
                        else:
                            player[8] = image_of_x     
                            playerGame = 'x'
                            checked[8] = playerGame
                    pieceClick[8] = True

            else:
                colorBackground[8] = [53, 75, 79]

        
        pygame.draw.rect(display, "#000000", mouse)

        display.blit(imagesButtons[0], [5, 5])
        display.blit(imagesButtons[1], [55, 5]) 
        display.blit(imagesButtons[2], [105, 5])    
        display.blit(imagesButtons[3], [145, 5])

        display.blit(pygame.transform.scale(image_of_x, [20, 20]), [900, 30])
        display.blit(pygame.transform.scale(image_of_o, [20, 20]), [900, 80])

        if (pieceClick[0]):
            display.blit(player[0], [305, 110])
        if (pieceClick[1]):
            display.blit(player[1], [455, 110])
        if (pieceClick[2]):
            display.blit(player[2], [605, 110])     
        if (pieceClick[3]):
            display.blit(player[3], [305, 260])
        if (pieceClick[4]):
            display.blit(player[4], [455, 260])
        if (pieceClick[5]):
            display.blit(player[5], [605, 260])
        if (pieceClick[6]):
            display.blit(player[6], [305, 410])
        if (pieceClick[7]):
            display.blit(player[7], [455, 410])
        if (pieceClick[8]):
            display.blit(player[8], [605, 410])

        if (mouse.colliderect(anotherButtons[0]) and pygame.mouse.get_pressed()[0] == True):
            exitNow = True

        if (mouse.colliderect(anotherButtons[1]) and pygame.mouse.get_pressed()[0] == True):
            pieceClick = [
                False, False, False,
                False, False, False,
                False, False, False
                ]
            checked = [
                0, 0, 0,
                0, 0, 0,
                0, 0, 0
            ]
        if (exitNow):

            gamming = False
            popUp(display, pygame.transform.scale(pygame.image.load('../images/warning.png'), [80, 80]), 'Queres realmente deixar essa partida?', 370, 295)
            option1 = button("Sair", display, optionsPopUp[0], 423, 327, [75, 75, 75], [200, 250, 200], borderRadious=3, fontSize=17)
            option2 = button("Fechar", display, optionsPopUp[1], 563, 327, [75, 75, 75], [200, 250, 200], borderRadious=3, fontSize=17)
            
            if (mouse.colliderect(optionsPopUp[0])):
                if (pygame.mouse.get_pressed()[0] == True):
                    menu.menu()

            if (mouse.colliderect(optionsPopUp[1])):
                if (pygame.mouse.get_pressed()[0] == True):
                    exitNow = False
                    gamming = True

        if (win == True):            
            gamming = False
            popUp(display, pygame.transform.scale(pygame.image.load('../images/winner.png'), [80, 80]), f'Parabens! "{winner.upper()}" ganhou está partida.', 370, 295, option1='Sair', option2='Jogar')

            option1 = button("Sair", display, optionsPopUp[0], 423, 327, [75, 75, 75], [200, 250, 200], borderRadious=3, fontSize=17)
            option2 = button("Fechar", display, optionsPopUp[1], 563, 327, [75, 75, 75], [200, 250, 200], borderRadious=3, fontSize=17)
            
            if (mouse.colliderect(optionsPopUp[0])):
                if (pygame.mouse.get_pressed()[0] == True):
                    menu.menu()

            if (mouse.colliderect(optionsPopUp[1])):
                if (pygame.mouse.get_pressed()[0] == True):
                    win = False
                    gamming = True
                    pieceClick = [
                        False, False, False,
                        False, False, False,
                        False, False, False
                        ]
                    checked = [
                        0, 0, 0,
                        0, 0, 0,
                        0, 0, 0
                    ]

        if (dont_winner):
            gamming = False
            popUp(display, pygame.transform.scale(pygame.image.load('../images/lose.png'), [80, 80]), 'Já não há possíveis jogadas!', 370, 295, option1='Sair', option2='Continuar')

            option1 = button("Sair", display, optionsPopUp[0], 423, 327, [75, 75, 75], [200, 250, 200], borderRadious=3, fontSize=17)
            option2 = button("Fechar", display, optionsPopUp[1], 563, 327, [75, 75, 75], [200, 250, 200], borderRadious=3, fontSize=17)
            
            if (mouse.colliderect(optionsPopUp[0])):
                if (pygame.mouse.get_pressed()[0] == True):
                    menu.menu()

            if (mouse.colliderect(optionsPopUp[1])):
                if (pygame.mouse.get_pressed()[0] == True):
                    dont_winner = False
                    gamming = True
                    pieceClick = [
                        False, False, False,
                        False, False, False,
                        False, False, False
                        ]
                    checked = [
                        0, 0, 0,
                        0, 0, 0,
                        0, 0, 0
                    ]
        #winner

        #player o

        if (checked[0] == 'o' and checked[1] == 'o' and checked[2] == 'o'):
            winner = 'o'
            win = True

        if (checked[3] == 'o' and checked[4] == 'o' and checked[5] == 'o'):
            winner = 'o'
            win = True

        if (checked[6] == 'o' and checked[7] == 'o' and checked[8] == 'o'):
            winner = 'o'
            win = True


        if (checked[0] == 'o' and checked[3] == 'o' and checked[6] == 'o'):
            winner = 'o'
            win = True
            
        if (checked[1] == 'o' and checked[4] == 'o' and checked[7] == 'o'):
            winner = 'o'
            win = True

        if (checked[2] == 'o' and checked[5] == 'o' and checked[8] == 'o'):
            winner = 'o'
            win = True


        if (checked[0] == 'o' and checked[4] == 'o' and checked[8] == 'o'):
            winner = 'o'
            win = True

        if (checked[2] == 'o' and checked[4] == 'o' and checked[6] == 'o'):
            winner = 'o'
            win = True

         #player x

        if (checked[0] == 'x' and checked[1] == 'x' and checked[2] == 'x'):
            winner = 'x'
            win = True

        if (checked[3] == 'x' and checked[4] == 'x' and checked[5] == 'x'):
            winner = 'x'
            win = True

        if (checked[6] == 'x' and checked[7] == 'x' and checked[8] == 'x'):
            winner = 'x'
            win = True


        if (checked[0] == 'x' and checked[3] == 'x' and checked[6] == 'x'):
            winner = 'x'
            win = True
            
        if (checked[1] == 'x' and checked[4] == 'x' and checked[7] == 'x'):
            winner = 'x'
            win = True

        if (checked[2] == 'x' and checked[5] == 'x' and checked[8] == 'x'):
            winner = 'x'
            win = True


        if (checked[0] == 'x' and checked[4] == 'x' and checked[8] == 'x'):
            winner = 'x'
            win = True

        if (checked[2] == 'x' and checked[4] == 'x' and checked[6] == 'x'):
            winner = 'x'
            win = True

        #Dont Winner

        if ((pieceClick[0] == True and pieceClick[1] == True and pieceClick[2] == True and pieceClick[3] == True and pieceClick[4] == True and pieceClick[5] == True and pieceClick[6] == True and pieceClick[7] == True and pieceClick[8] == True) and win == False):
            dont_winner = True

        pygame.draw.rect(display, "#ffffff", mouse)
        pygame.display.flip()

if __name__ == '__main__':
    game()