import pygame
class Controller:
    def __init__(self, x, y, speed, up, down, left, right, shoot, image):
        self.x = x
        self.y = y
        self.speed = speed
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.shoot = shoot
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
    def move_up(self):
        self.rect.y -= self.speed
    def move_down(self):
        self.rect.y += self.speed
    def move_left(self):
        self.rect.x -= self.speed
    def move_right(self):
        self.rect.x += self.speed
    