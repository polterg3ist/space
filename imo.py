import pygame


class Imo(pygame.sprite.Sprite):

    def __init__(self, screen, audio_connection):
        super(Imo, self).__init__()
        self.screen = screen
        self.audio_connection = audio_connection
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
        self.y += 1.1 
        self.rect.y = self.y
    
    def __del__(self):
        if self.audio_connection:
            pygame.mixer.Sound("sounds/shot2.wav").play()
