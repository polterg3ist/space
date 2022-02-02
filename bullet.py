import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, player):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 240, 14, 14
        self.speed = 6.5
        self.rect.centerx = player.ship_rect.centerx
        self.rect.top = player.ship_rect.top
        self.position = float(self.rect.y)

    def update(self):
        """Updating bullet position"""
        self.position -= self.speed
        self.rect.y = self.position

    def draw(self):
        """Drawing bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)
