import pygame, sys
from pygame.locals import*

pygame.init()


def button(title="", display=0, rect=0, position_x_title=0, position_y_title=0, colorWord = [255, 255, 255], colorBackground = [53, 75, 79], haveImage=False, hoverEffect=False, borderRadious=0, fontSize = 25):

    pygame.draw.rect(display, colorBackground, rect, border_radius=borderRadious)
    
    font = pygame.font.SysFont('Arial', fontSize, True, False)

    text = font.render(title, True, colorWord)

    display.blit(text, [position_x_title, position_y_title])
    
   
def popUp(display, image, msg, textX, textY, option1 = 'Não', option2 = 'Sim'):

    font = pygame.font.SysFont('Arial', 15, True, False)
    pygame.draw.rect(display, [100, 100, 100], [(1024/2) - 300/2, (576/2) - (150/2), 300, 150], border_radius=10)
    display.blit(image, [475, 210])

    text = font.render(msg, True, [255, 255, 255])

    display.blit(text, [textX, textY])
