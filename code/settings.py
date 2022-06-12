import pygame, sys
from pygame.locals import*
from components import button, popUp
import menu
from time import sleep

pygame.init()


size = (1024, 576)
color = (23, 35, 39)

display = pygame.display.set_mode(size)
pygame.display.set_caption('Tic Tac Toe')

backgrounMusic = pygame.mixer.music.load('../sounds/Awaken.mp3')
pygame.mixer.music.play()
anotherButtons = [
    pygame.Rect(0, 0, 40, 40),
]

button_color = [
    [53, 75, 79],
    [13, 45, 49],
    [13, 45, 49],
    [13, 45, 49],
]

buttons = {
    'music': pygame.Rect(330, 210, 50, 40),
    'sound': pygame.Rect(330, 260, 50, 40),
    'language1': pygame.Rect(390, 345, 30, 30),
    'language2': pygame.Rect(430, 345, 30, 30),
    'language3': pygame.Rect(470, 345, 30, 30),
    'apply': pygame.Rect(590, 340, 80, 40)
}

flags = [
    pygame.transform.scale(pygame.image.load('../images/usa.png'), [30, 30]),
    pygame.transform.scale(pygame.image.load('../images/espanha.png'), [30, 30]),
    pygame.transform.scale(pygame.image.load('../images/portugal.png'), [30, 30]),
]

font = pygame.font.SysFont('Arial', 16, True, False)

imagesButtons = [
        pygame.transform.scale(pygame.image.load('../images/exit.png'), [30, 30]),
        pygame.transform.scale(pygame.image.load('../images/music.png'), [30, 30]),
        pygame.transform.scale(pygame.image.load('../images/sound.png'), [30, 30]),
        pygame.transform.scale(pygame.image.load('../images/language.png'), [30, 30]),
        pygame.transform.scale(pygame.image.load('../images/not-sound.png'), [30, 30]),
        pygame.transform.scale(pygame.image.load('../images/not-sound.png'), [30, 30]),
    ]

def saveData():
    ...

def settings(music='play', sound='play', language='en'):
    imagesButtons_ = [
        pygame.transform.scale(pygame.image.load('../images/music.png'), [30, 30]),
         pygame.transform.scale(pygame.image.load('../images/sound.png'), [30, 30]),
    ]

    while True:
        mouse = pygame.Rect(pygame.mouse.get_pos()[0] + 3, pygame.mouse.get_pos()[1] + 3, 1, 1)
        display.fill(color)

        for event in pygame.event.get():
            if (event.type == QUIT):
                pygame.quit()
                sys.exit()
        
        if (mouse.colliderect(anotherButtons[0])):
            if (pygame.mouse.get_pressed()[0] == True):
                menu.menu()

        button(display = display, rect=anotherButtons[0], borderRadious=0, colorBackground= button_color[0])
        display.blit(imagesButtons[0], [5, 5])

        pygame.draw.rect(display, "#ffffff", mouse)
        pygame.draw.rect(display, [53, 75, 79], [1024/2 - 370/2, 576/2-200/2, 370, 200], border_radius=10)

        
        button(display=display, rect=buttons['music'], borderRadious=2, colorBackground=button_color[3])
        
        button(display=display, rect=buttons['sound'], borderRadious=2, colorBackground=button_color[3])
        button(display=display, rect=buttons['apply'], borderRadious=2, colorBackground=button_color[1])

        button(display=display, rect=buttons['language1'], borderRadious=2, colorBackground=button_color[1])
        button(display=display, rect=buttons['language2'], borderRadious=2, colorBackground=button_color[1])
        button(display=display, rect=buttons['language3'], borderRadious=2, colorBackground=button_color[1])
        
        display.blit(flags[0], [390, 345])
        display.blit(flags[1], [430, 345])
        display.blit(flags[2], [470, 345])

        display.blit(font.render('Musica', True, "#ffffff"), [400, 220])
        display.blit(font.render('Efeitos sonóros', True, "#ffffff"), [400, 270])
        display.blit(font.render('Linguagens', True, "#ffffff"), [400, 320])

        display.blit(font.render('Aplicar', True, "#ffffff"), [608, 350])

        display.blit(imagesButtons[1], [340, 215])
        display.blit(imagesButtons[2], [340, 265])
        display.blit(imagesButtons[3], [340, 315])
        
        if (mouse.colliderect(buttons['apply'])):
            if (pygame.mouse.get_pressed()[0] == True):
                menu.menu()
        if (mouse.colliderect(buttons['music'])):
            if (pygame.mouse.get_pressed()[0] == True):
                if (imagesButtons[1] == imagesButtons[4]):
                     imagesButtons[1] = imagesButtons_[0]
                     sleep(0.4)
                else:
                    imagesButtons[1] = imagesButtons[4]
                    sleep(0.4)
        if (mouse.colliderect(buttons['sound'])):
            if (pygame.mouse.get_pressed()[0] == True):
                if (imagesButtons[2] == imagesButtons[5]):
                    imagesButtons[2] = imagesButtons_[1]
                    sleep(0.4)
                else:
                    imagesButtons[2] = imagesButtons[5]
                    sleep(0.4)
                

        pygame.display.flip()

if __name__=='__main__':
    settings()
