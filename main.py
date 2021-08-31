import pygame
pygame.init()
GREEN = ( 0, 255, 0)

Size = (700, 500)
Screen = pygame.display.set_mode(Size)
pygame.display.set_caption("I am the best player world")

Continue = True
clock = pygame.time.Clock()

while Continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Continue = False
