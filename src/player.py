import pygame
import os
from hitbox import HitBox

class Player:
        walkRight = [pygame.image.load(os.path.join('sprites', 'R1.png')), pygame.image.load(os.path.join('sprites', 'R2.png')), pygame.image.load(os.path.join('sprites', 'R3.png')), pygame.image.load(os.path.join('sprites', 'R5.png')), pygame.image.load(os.path.join('sprites', 'R5.png')), pygame.image.load(os.path.join('sprites', 'R6.png')), pygame.image.load(os.path.join('sprites', 'R7.png')), pygame.image.load(os.path.join('sprites', 'R8.png')), pygame.image.load(os.path.join('sprites', 'R9.png'))]
        walkLeft = [pygame.image.load(os.path.join('sprites', 'L1.png')), pygame.image.load(os.path.join('sprites', 'L2.png')), pygame.image.load(os.path.join('sprites', 'L3.png')), pygame.image.load(os.path.join('sprites', 'L4.png')), pygame.image.load(os.path.join('sprites', 'L5.png')), pygame.image.load(os.path.join('sprites', 'L6.png')), pygame.image.load(os.path.join('sprites', 'L7.png')), pygame.image.load(os.path.join('sprites', 'L8.png')), pygame.image.load(os.path.join('sprites', 'L9.png'))]
        #char = pygame.image.load('standing.png')
        
        def __init__(self, x, y, width, height):
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.vel = 5 
                self.left = False
                self.right = False
                self.direction = 0
                self.isJump = False
                self.jumpCount = 10
                self.walkCount = 0
                self.standing = True
                self.projectiles = []
                self.ammoCount = 1
                self.ammoCooldown = 0 #ammo cooldown used for basic timer
                self.hitbox = HitBox(self.x + 18, self.y + 12, 26, 52).rectangle #rectangular hitbox - (left, top, width, height)                

        def animate(self, window):
                if self.walkCount + 1 >= 54: #indexing through sprite array, based on fps
                        self.walkCount = 0

                if not(self.standing): #moving
                        #display each of the 9 sprites for 6 frames - total 54 fps
                        if self.left: #walking left
                                window.blit(self.walkLeft[self.walkCount//6], (self.x, self.y)) #integer divison
                                self.walkCount += 1
                        else: #walking right
                                window.blit(self.walkRight[self.walkCount//6], (self.x, self.y))
                                self.walkCount += 1
                #default entry point upon start
                else: #standing or jumping
                        if self.left: #facing left
                                window.blit(self.walkLeft[0], (self.x, self.y))
                        else: #facing right or upon spawn
                                window.blit(self.walkRight[0], (self.x, self.y))
                                
                self.hitbox = HitBox(self.x + 18, self.y + 12, 26, 52).rectangle
                pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2) #draw hitbox - pygame.draw.rect(screen, color, (left, top, width, height), thickness)
        
        def hit(self):
                print("player hit")     
