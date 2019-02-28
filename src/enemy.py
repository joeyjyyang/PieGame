import pygame
import os
from hitbox import HitBox

class Enemy:
        walkRight = [pygame.image.load(os.path.join('sprites', 'R1E.png')), pygame.image.load(os.path.join('sprites', 'R2E.png')), pygame.image.load(os.path.join('sprites', 'R3E.png')), pygame.image.load(os.path.join('sprites', 'R4E.png')), pygame.image.load(os.path.join('sprites', 'R5E.png')), pygame.image.load(os.path.join('sprites', 'R6E.png')), pygame.image.load(os.path.join('sprites', 'R7E.png')), pygame.image.load(os.path.join('sprites', 'R8E.png')), pygame.image.load(os.path.join('sprites', 'R9E.png')), pygame.image.load(os.path.join('sprites', 'R10E.png')), pygame.image.load(os.path.join('sprites', 'R11E.png'))]
        walkLeft = [pygame.image.load(os.path.join('sprites', 'L1E.png')), pygame.image.load(os.path.join('sprites', 'L2E.png')), pygame.image.load(os.path.join('sprites', 'L3E.png')), pygame.image.load(os.path.join('sprites', 'L4E.png')), pygame.image.load(os.path.join('sprites', 'L5E.png')), pygame.image.load(os.path.join('sprites', 'L6E.png')), pygame.image.load(os.path.join('sprites', 'L7E.png')), pygame.image.load(os.path.join('sprites', 'L8E.png')), pygame.image.load(os.path.join('sprites', 'L9E.png')), pygame.image.load(os.path.join('sprites', 'L10E.png')), pygame.image.load(os.path.join('sprites', 'L11E.png'))]

        def __init__(self, x, y, width, height, end):
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.end = end
                self.path = [self.x, self.end] #start and end of path
                self.walkCount = 0
                self.vel = 3
                self.health = 1
                self.hitbox = HitBox(self.x + 17, self.y + 2, 31, 57).rectangle
                self.alive = True

        def animate(self, window):
                if self.alive: 
                        self.move() #move first, then update animation
                        if self.walkCount + 1 >= 55:
                                self.walkCount = 0

                        if self.vel > 0: #walking right
                                window.blit(self.walkRight[self.walkCount//5], (self.x, self.y))
                                self.walkCount +=1
                        else: #walking left
                                window.blit(self.walkLeft[self.walkCount//5], (self.x, self.y))
                                self.walkCount +=1

                        self.hitbox = HitBox(self.x + 17, self.y + 2, 31, 57).rectangle
                        pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2) #draw hitbox


        def move(self):
                if self.vel > 0:
                        if self.x + self.vel < self.path[1]: 
                                self.x += self.vel
                        else: #reach path end - switch direction
                                self.vel = self.vel * -1
                                self.walkCount = 0
                else:
                        if self.x - self.vel > self.path [0]:
                                self.x += self.vel
                        else: #reach path start - switch direction
                                self.vel = self.vel * -1
                                self.walkCount = 0

        def hit(self):
                print("hit")

                if(self.health > 1):
                        self.health -= 1
                else:
                        self.kill()
        
        def kill(self):
                print("dead") 
                self.alive = False 
                pygame.display.update() 

class Goblin(Enemy):
        '''
        walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
        walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]
        '''
        def __init__(self):
                pass
