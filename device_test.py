import pygame

pygame.init()


def is_connection():
    try:
        pygame.mixer.Sound("sounds/start_sound.wav").play()
    except pygame.error:
        print("No sound device detected")
        return False
    else:
        return True