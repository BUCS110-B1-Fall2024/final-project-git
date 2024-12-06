import pygame
class Player:
    def __init__(self, lives, score, damage):
        self.lives = lives
        self.score = score
        self.damage = damage
    def __str__(self):
            return "Game Over"
    def update_scores(self, enemy_destroyed):
        self.score += 100*enemy_destroyed
    def power_up(self):
        self.damage += 1
    