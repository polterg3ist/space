from space_ship import SpaceShip
from pygame.sprite import Group
from stats import Stat
import pygame
import controls



def main():
    pygame.init()
    audio_connection = controls.is_connection()
    FPS = 60
    start_ticks = pygame.time.get_ticks()
    now = 0
    stats = Stat()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((900, 800))
    pygame.display.set_caption("Space Warrior")
    background = pygame.image.load("img/bg_stars_2.jpg").convert()
    background = pygame.transform.smoothscale(background, screen.get_size())
    player = SpaceShip(screen)
    bullets = Group()
    imos = Group()

  
    while True:
        controls.events(player, bullets, screen, audio_connection)
        if player.alive:
            clock.tick(FPS)
            now = controls.spawn_enemy(start_ticks, now, screen, imos, stats.score)
            player.update()
            controls.update(background, player, screen, bullets, imos, stats, audio_connection)
            controls.update_bullets(bullets, imos, audio_connection, stats)
            controls.update_imos_pos(imos, screen, player, bullets, stats, audio_connection)
            controls.show_stats(stats)


if __name__ == '__main__':
    main()
