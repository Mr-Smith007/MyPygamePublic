import pygame

pygame.init()
pygame.display.set_mode((640, 480))
pygame.display.set_caption("Ventana Basica")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()