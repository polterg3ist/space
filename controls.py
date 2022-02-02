import pygame
from sys import exit as close_game
from bullet import Bullet
from imo import Imo


def events(player, bullets, screen, audio_connection):
    """Handler of all events in the game"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_game()
        elif event.type == pygame.KEYDOWN:
            # moving right
            if event.key == pygame.K_d:
                player.move_right = True
            # moving left
            elif event.key == pygame.K_a:
                player.move_left = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, player)
                bullets.add(new_bullet)
                if audio_connection:
                    play_sound("sounds/shot.wav")

        elif event.type == pygame.KEYUP:
            # stop moving right
            if event.key == pygame.K_d:
                player.move_right = False
            # stop moving left
            elif event.key == pygame.K_a:
                player.move_left = False


def update(background, player, screen, bullets, imos):
    """Updating screen"""
    screen.blit(background, (0, 0))
    for bullet in bullets.sprites():
        bullet.draw()
    player.output()
    for imo in imos.sprites():
        imo.draw()
    pygame.display.flip()


def update_bullets(bullets, imos):
    """Updating bullets"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, imos, True, True)


def update_imos_pos(imos):
    imos.update()


def play_sound(path):
    pygame.mixer.Sound(path).play()


def create_enemies(screen, imos, audio_connection):
    "Creating army of enemies"
    imo = Imo(screen, audio_connection)
    imo_width = imo.rect.width + 20
    imo_height = imo.rect.height
    max_imos_x = int((700 - 2 * imo_width) / imo_width)
    max_imos_y = int((800 - 2 * imo_height) / imo_height)

    
    for imo_num in range(max_imos_x):
        imo = Imo(screen, audio_connection)
        imo.x = imo_width + imo_width * imo_num
        imo.rect.x = imo.x
        imos.add(imo) 

    
