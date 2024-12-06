import pygame
class Enemy:
    def __init__(self, x, y, speed, health, enemy):
        self.x = x
        self.y = y
        self.speed = speed
        self.health = health
        self.enemy = pygame.image.load(enemy)
        self.rect = self.enemy.get_rect()
        self.rect.topleft = (self.x,self.y)
    def move1(self):
        self.rect.x += self.speed
    def move2(self):
        self.rect.x -= self.speed
    def move3(self):
        self.rect.y += self.speed
        self.rect.x += self.speed
    def move4(self):
        self.rect.y += self.speed
        self.rect.x -= self.speed