import pygame

pygame.font.init()


def print_text(screen, info, stats=None):
    if info == 'Game Over':
        font = pygame.font.SysFont('serif', 80)
        text = font.render('Game Over', True, (0, 100, 55))
        place = text.get_rect(center=(450, 400))
        screen.blit(text, place)
    elif info == 'scores':
        color = (169, 32, 62)
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"SC: {stats.score}", True, color)
        best_score = font.render(f"BS: {stats.best_score}", True, color)
        screen.blit(score, (0, 0))
        screen.blit(best_score, (0, score.get_rect().bottom))
    elif info == 'Earned Score':
        color = (255, 191, 0)
        font = pygame.font.SysFont('serif', 55)
        over_score = font.render(f"SCORE {stats.score}", True, color)
        place = over_score.get_rect(center=(450, 465))
        screen.blit(over_score, place)
