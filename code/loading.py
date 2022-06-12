import pygame, sys
from pygame.locals import*
from time import sleep

pygame.init()

size = (1024, 576)
color = (23, 35, 39)

display = pygame.display.set_mode(size)
pygame.display.set_caption('Tic Tac Toe')

image_of_x = pygame.image.load('../images/x.png')
image_of_x = pygame.transform.scale(image_of_x, [10, 10])

image_of_o = pygame.image.load('../images/o.png')
image_of_o = pygame.transform.scale(image_of_o, [10, 10])

font = pygame.font.SysFont('Arial', 15, True, False)
text = font.render('loading', True, [100, 100, 100])


def loading():
    cont = 2
    while (True):
        cont += 0.5
        display.fill(color)

        for events in pygame.event.get():
            if events.type == QUIT:
                pygame.quit()
                sys.exit()

        if (cont == 15):
            break

        if (cont%2 == 0):
            display.blit(image_of_x, [1000, 520])
            display.blit(image_of_o, [990, 530])

        if (cont%2 == 0):
            display.blit(image_of_x, [1000, 540])
            display.blit(image_of_o, [1010, 530])
            

        display.blit(text, [930, 528])
        pygame.display.flip()
        sleep(0.25)

if __name__ == '__main__':
    loading()