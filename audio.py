import pygame

pygame.init()
volume = 0.1 


def is_connection():
    try:
        start_sound = pygame.mixer.Sound("sounds/start_sound.wav")
        start_sound.set_volume(volume)
        start_sound.play()
    except pygame.error as ex:
        print("No sound device detected", ex)
        return False
    return True
