import pygame
import random
from player import Player
from controller import Controller
from bullet import Bullet
from enemy import Enemy
#import your controller

def main():
    pygame.init()
    WIDTH = 600
    HEIGHT = 800
    scale = 50
    speed = 10
    enemy_health = 4
    player_lives = 3
    score = 0
    damage = 1
    black = (0,0,0)
    white = (255,255,255)
    w = pygame.K_w
    s = pygame.K_s
    a = pygame.K_a
    d = pygame.K_d
    shoot = pygame.K_SPACE
    bullet = "bullet.png"
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Battle Aircraft!")
    background = black
    clock = pygame.time.Clock()
    player = Player(player_lives,score, damage)
    control = Controller(WIDTH/2, HEIGHT - scale, speed , w, s, a, d, shoot, "plane.png")
    enemy1 = Enemy(random.randint(0,WIDTH), scale+10, speed/10, enemy_health,"enemy_plane1.png" )
    font = pygame.font.SysFont('arial', 20)
    score_text = font.render("Score:" + str(player.score), True, white)
    player_lives_text = font.render("player_lives:" + str(player.lives), True, white)
    scaled_plane = pygame.transform.scale(control.image, (scale,scale))
    scaled_enemy1 = pygame.transform.scale(enemy1.enemy, (scale,scale))
    enemy1_bullet = Bullet(enemy1.rect.x, enemy1.rect.y, 10, damage, speed, bullet)
    enemy1_bullet = pygame.transform.scale(enemy1_bullet.bullet, (scale/5,scale/5))
    player_bullet = Bullet(control.rect.centerx, control.rect.centery, 10,  damage, speed, bullet)
    player_bullet_picture = pygame.transform.scale(player_bullet.bullet, (scale/5, scale/5))
     
    #Create an instance on your controller object
    #Call your mainloop
    shoot = True
    running = True
    while running:
        screen.fill(background)
        enemy1_plane = pygame.transform.rotate(scaled_enemy1,180)
        screen.blit(score_text, (0,0))
        screen.blit(player_lives_text,(0, scale/2))
        screen.blit(scaled_plane, control.rect)
        screen.blit(enemy1_bullet, (enemy1.rect.x, enemy1.rect.y))
        screen.blit(enemy1_plane, enemy1.rect)
        pygame.draw.rect(screen, white, (0,scale,WIDTH,10))
        enemy1.move1()
        if enemy1.rect.x >= WIDTH - scale:
            enemy1.rect.x = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  
            if pygame.key.get_pressed()[control.up]:
                if control.rect.y > scale:
                    control.move_up()
                else:
                    pass
            if pygame.key.get_pressed()[control.shoot]:
                player_bullet.move()
            if pygame.key.get_pressed()[control.down]:
                if control.rect.y < HEIGHT - scale:
                    control.move_down()
                else:
                    pass
            if pygame.key.get_pressed()[control.left]:
                if control.rect.x > 0:
                    control.move_left()
                else:
                    pass
            if pygame.key.get_pressed()[control.right]:
                if control.rect.x < WIDTH - scale:
                    control.move_right()
                else:
                    pass
        
                    
        pygame.display.update()
        clock.tick(60)
        
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
