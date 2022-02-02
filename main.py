from space_ship import SpaceShip
from pygame.sprite import Group
from device_test import is_connection
import pygame
import controls


def main():
    pygame.init()
    in_game = True
    audio_connection = is_connection()
    FPS = 60
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Space Warrior")
    background = pygame.image.load("img/bg_stars_2.jpg").convert()
    #background = pygame.transform.smoothscale(background, screen.get_size())
    player = SpaceShip(screen)
    bullets = Group()
    imos = Group()
    controls.create_enemies(screen, imos, audio_connection)

    while True:
        clock.tick(FPS)
        controls.events(player, bullets, screen, audio_connection)
        player.update()
        controls.update(background, player, screen, bullets, imos)
        controls.update_bullets(bullets, imos)
        controls.update_imos_pos(imos)


if __name__ == '__main__':
    main()
