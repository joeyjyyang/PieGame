#!/usr/bin/python2.7

import pygame
import os
from random import seed, randint
from hitbox import HitBox
from window import Window
from enemy import Enemy
from projectile import Projectile
from player import Player


'''
        Author: Joey Yang
'''

ENEMY_COUNT = 1

class Game:
        def __init__(self):
                self.windowHeight = 500
                self.windowWidth = 500
                self.fps = 54
                self.run = True
                self.clock = pygame.time.Clock()
                self.player = Player(250, 410, 64, 64)
                
                self.enemies = []
                #self.enemy2 = Enemy(50, 417, 64, 64, 300)
                #self.enemies = [self.enemy1, self.enemy2]
                self.window = Window(self.windowHeight, self.windowWidth, self.player, self.enemies)
                
        def spawnEnemies(self, enemyCount):
                seed(14)

                for enemy in range(enemyCount):  
                        self.enemies.append(Enemy(randint(10, 100), 417, 64, 64, randint(300, 400)))

        def updateGameWindow(self):
                self.window.updateWindow()
                
        def startGame(self):
                pygame.init()
                
                self.spawnEnemies(ENEMY_COUNT)

                while self.run:
                        self.clock.tick(self.fps) # 54 fps
                        
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        run = False

                        #player - enemy collision
                        for enemy in self.enemies:
                                if enemy.alive:
                                        if (self.player.hitbox[1] >= enemy.hitbox[1] and self.player.hitbox[1] <= enemy.hitbox[1] + enemy.hitbox[3]) or (self.player.hitbox[1] + self.player.hitbox[3] >= enemy.hitbox[1] and self.player.hitbox[1] + self.player.hitbox[3] <= enemy.hitbox[1] + enemy.hitbox[3]):
                                                if (self.player.hitbox[0] <= enemy.hitbox[0] + enemy.hitbox[2] and self.player.hitbox[0] >= enemy.hitbox[0]) or (self.player.hitbox[0] + self.player.hitbox[2] >= enemy.hitbox[0] and self.player.hitbox[0] + self.player.hitbox[2] <= enemy.hitbox[0] + enemy.hitbox[2]):
                                                        self.player.hit()


                        #check player ammo cooldown
                        if self.player.ammoCooldown > 0:
                                self.player.ammoCooldown += 1
                        if self.player.ammoCooldown > 5:
                                self.player.ammoCooldown = 0
                        
                        #projectile hit enemy
                        for projectile in self.player.projectiles:
                                for enemy in self.enemies:
                                        if enemy.alive:
                                                if (projectile.hitbox[1] >= enemy.hitbox[1] and projectile.hitbox[1] <= enemy.hitbox[1] + enemy.hitbox[3]) or (projectile.hitbox[1] + projectile.hitbox[3] >= enemy.hitbox[1] and projectile.hitbox[1] + projectile.hitbox[3] <= enemy.hitbox[1] + enemy.hitbox[3]):
                                                        if (projectile.hitbox[0] <= enemy.hitbox[0] + enemy.hitbox[2] and projectile.hitbox[0] >= enemy.hitbox[0]) or (projectile.hitbox[0] + projectile.hitbox[2] >= enemy.hitbox[0] and projectile.hitbox[0] + projectile.hitbox[2] <= enemy.hitbox[0] + enemy.hitbox[2]):
                                                                enemy.hit()
                                                                self.player.projectiles.pop(self.player.projectiles.index(projectile))

                                if projectile.x < self.windowWidth and projectile.x > 0: #projectile onscreen
                                        projectile.x += projectile.vel
                                else: #projectile offscreen
                                        self.player.projectiles.pop(self.player.projectiles.index(projectile))
                                        
                                
                        keys = pygame.key.get_pressed() #array of keyboard keys

                        if keys[pygame.K_ESCAPE]:
                                self.run = False
                                
                        if keys[pygame.K_SPACE] and self.player.ammoCooldown == 0: #wait for cooldown before shooting
                                if self.player.left: #facing left then jump
                                        self.player.direction = -1
                                else: #facing right then jump or upon spawn
                                        self.player.direction = 1
         
                                if len(self.player.projectiles) < self.player.ammoCount:
                                        self.player.projectiles.append(Projectile(int(self.player.x + self.player.width//2), int(self.player.y + 17), self.player.direction))
                                        
                        if keys[pygame.K_LEFT] and self.player.x > self.player.vel:
                                self.player.x -= self.player.vel
                                self.player.left = True
                                self.player.right = False
                                self.player.standing = False
                        elif keys[pygame.K_RIGHT] and self.player.x < self.windowWidth - self.player.width - self.player.vel:
                                self.player.x += self.player.vel
                                self.player.left = False
                                self.player.right = True
                                self.player.standing = False
                        else:
                                self.player.standing = True
                                self.player.walkCount = 0

                        if not(self.player.isJump):
                                #platform game - disabling upwards and downwards movement
                                '''if keys[pygame.K_UP] and y > vel:
                                        y -= vel
                                if keys[pygame.K_DOWN] and y < screenHeight - height - vel:                                 y += vel'''
                                #enabling jumping
                                if keys[pygame.K_UP]:
                                        self.player.isJump = True
                                        self.player.walkCount = 0
                        else: #jumping
                                if self.player.jumpCount >= -10: #parabolic jump
                                        self.player.y -= (self.player.jumpCount * abs(self.player.jumpCount)) * 0.5 
                                        self.player.jumpCount -= 1
                                else: #end of jump
                                        self.player.isJump = False
                                        self.player.jumpCount = 10

                        self.updateGameWindow()
                        
                self.stopGame()
                
        def stopGame(self):
                pygame.quit()
                     
def main():
        game = Game()
        game.startGame()
 
if __name__ == "__main__":
        main()
        
                
