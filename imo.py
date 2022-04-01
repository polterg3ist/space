import pygame


class Imo(pygame.sprite.Sprite):

    def __init__(self, screen, deaths):
        super(Imo, self).__init__()
        self.screen = screen
        self.speed = deaths / 30
        self.image = pygame.image.load('img/imo2.1.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """Draw enemy"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += 1.1 + self.speed
        self.rect.y = self.y
