import pygame, sys
from pygame.locals import*

pygame.init()

def popUp(display, image, msg, textX, textY, option1 = 'Não', option2 = 'Sim'):

    font = pygame.font.SysFont('Arial', 15, True, False)
    pygame.draw.rect(display, [100, 100, 100], [(1024/2) - 300/2, (576/2) - (150/2), 300, 150], border_radius=10)
    display.blit(image, [475, 210])

    text = font.render(msg, True, [255, 255, 255])

    display.blit(text, [textX, textY])
