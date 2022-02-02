import pygame


class SpaceShip:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('img/ship_3.png')
        self.ship_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ship_rect.centerx = self.screen_rect.centerx
        self.center = float(self.ship_rect.centerx)
        self.ship_rect.bottom = self.screen_rect.bottom
        self.move_right = False
        self.move_left = False

    def output(self):
        """Printing spaceship on the screen"""
        self.screen.blit(self.image, self.ship_rect)

    def update(self):
        """Update location of ship on screen"""
        if self.move_right and self.ship_rect.right < self.screen_rect.right:
            self.center += 6.5
        if self.move_left and self.ship_rect.left > 0:
            self.center -= 6.5
        self.ship_rect.centerx = self.center
