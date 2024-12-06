import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__ (self, x, y, size ,damage, velocity, bullet):
        self.x = x
        self.y = y  
        self.size = size
        self.damage = damage
        self.velocity = velocity
        self.bullet = pygame.image.load(bullet)
        self.rect = self.bullet.get_rect()
        self.rect.center = (self.x, self.y)
    def move(self):
        self.rect.y -= self.velocity
    def update(self):
        self.rect.y -= self.velocity
        if self.rect.y > 750:
            self.kill()