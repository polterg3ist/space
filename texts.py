import pygame
pygame.font.init()

font = pygame.font.SysFont('serif', 68)


def print_text(screen, info):
    if info == 'Game Over':
        text = font.render('Game Over', True, (0, 100, 55))
        place = text.get_rect(center=(450, 400))
        screen.blit(text, place)
