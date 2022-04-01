import pygame


class SpaceShip:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('img/ship_3.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.alive = True
        self.move_right = False
        self.move_left = False
        self.turbo = False

    def output(self):
        """Printing spaceship on the screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update location of ship on screen"""
        if self.turbo:
            speed = 12.5
        else:
            speed = 6.5
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += speed
        if self.move_left and self.rect.left > 0:
            self.center -= speed
        self.rect.centerx = self.center
