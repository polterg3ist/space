import pygame
import audio
import texts
from sys import exit as close_game
from bullet import Bullet
from imo import Imo
from random import randint


AUDIO_CONNECTION = audio.is_connection()


def events(player, bullets, screen):
    """Handler of all events in the game"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_game()
        elif not player.alive and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.alive = True
            continue
        if player.alive:    
            if event.type == pygame.KEYDOWN:
                # turbo speed 
                if event.key == pygame.K_LCTRL:
                    player.turbo = True
                # moving right
                elif event.key == pygame.K_d:
                    player.move_right = True
                # moving left
                elif event.key == pygame.K_a:
                    player.move_left = True
                elif event.key == pygame.K_SPACE:
                    new_bullet = Bullet(screen, player)
                    bullets.add(new_bullet)
                    play_sound("sounds/shot3.wav")

            elif event.type == pygame.KEYUP:
                # stop turbo
                if event.key == pygame.K_LCTRL:
                    player.turbo = False
                # stop moving right
                elif event.key == pygame.K_d:
                    player.move_right = False
                # stop moving left
                elif event.key == pygame.K_a:
                    player.move_left = False


def update(background, player, screen, bullets, imos, stats):
    """Updating screen"""
    screen.blit(background, (0, 0))
    for bullet in bullets.sprites():
        bullet.draw()
    player.output()
    for imo in imos.sprites():
        imo.draw()
    if pygame.sprite.spritecollideany(player, imos):
        plr_death(screen, player, imos, bullets, stats)
    pygame.display.flip()


def update_bullets(bullets, imos, stats):
    """Updating bullets"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, imos, True, True)
    if collisions:
        stats.score += 1
        play_sound("sounds/shot2.wav")


def update_imos_pos(imos, screen, player, bullets, stats):
    imos.update()
    for imo in imos:
        if imo.rect.top > 800:
            plr_death(screen, player, imos, bullets, stats)


def plr_death(screen, player, imos, bullets, stats):
    play_sound("sounds/die1.wav")
    imos.empty()
    bullets.empty()
    player.alive = False
    player.move_right = False
    player.move_left = False
    player.turbo = False
    if int(stats.best_score) < stats.score:
        stats.set_best_score()
    texts.print_text(screen, 'Game Over')
    texts.print_text(screen, 'Earned Score', stats)
    stats.score = 0
    pygame.display.flip()
       

def play_sound(path):
    if AUDIO_CONNECTION:
        sound = pygame.mixer.Sound(path)
        sound.set_volume(audio.volume)
        sound.play()
    else:
        print(f"Sound {path[7::]} was ignored because audio connection is disabled")


def create_enemy(screen, imos, deaths):
    # print(f"SPEED NOW= {1.1 + deaths/30}")
    imo = Imo(screen, deaths)
    imo_width = imo.rect.width + 20
    imo_height = imo.rect.height
    max_imos_x = int((900 - 2 * imo_width) / imo_width)
    max_imos_y = int((800 - 2 * imo_height) / imo_height)
    imo.x = imo_width + imo_width * randint(0, max_imos_x)
    imo.rect.x = imo.x
    imos.add(imo)


def spawn_enemy(start_ticks, now, screen, imos, deaths):
    seconds = int((pygame.time.get_ticks()-start_ticks)/1000)
    if seconds != now and int(seconds) % 0.5 == 0:
        now = seconds                              
        create_enemy(screen, imos, deaths)
    return now


def show_stats(screen, stats):
    texts.print_text(screen, "scores", stats)
    pygame.display.flip()

