import pygame
import os

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
                self.ammo = 1
                self.hitbox = (self.x + 18, self.y + 12, 26, 52) #rectangular hitbox

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
                                
                self.hitbox = (self.x + 18, self.y + 12, 26, 52)
                pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2) #draw hitbox     
                                      
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
                self.hitbox = (self.x + 17, self.y + 2, 31, 57)

        def animate(self, window):
                self.move() #move first, then update animation
                
                if self.walkCount + 1 >= 55:
                        self.walkCount = 0

                if self.vel > 0: #walking right
                        window.blit(self.walkRight[self.walkCount//5], (self.x, self.y))
                        self.walkCount +=1
                else: #walking left
                        window.blit(self.walkLeft[self.walkCount//5], (self.x, self.y))
                        self.walkCount +=1

                self.hitbox = (self.x + 17, self.y + 2, 31, 57)
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

        
                
'''class Goblin(Enemy):
        walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
        walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]
'''
class Projectile:
        shuriken = pygame.image.load(os.path.join('sprites', 'shuriken.png'))

        def __init__(self, x, y, direction):
                self.x = x
                self.y = y
                self.direction = direction
                self.vel = 8 * direction

        def animate(self, window):
                window.blit(self.shuriken, (self.x, self.y))
                
class Window:
        bg = pygame.image.load(os.path.join('sprites', 'bg.jpg'))
        
        def __init__(self, windowHeight, windowWidth, player, enemies):
                self.windowHeight = windowHeight
                self.windowWidth = windowWidth
                self.window = pygame.display.set_mode((self.windowHeight, self.windowWidth))
                self.player = player
                self.enemies = enemies
                pygame.display.set_caption("Spaghetti User Interface")

        def updateWindow(self):
                self.window.blit(self.bg, (0,0)) 
                self.player.animate(self.window)
                for enemy in self.enemies:
                        enemy.animate(self.window)
                for projectile in self.player.projectiles:
                        projectile.animate(self.window)
                pygame.display.update()
                
class Game:
        def __init__(self):
                self.windowHeight = 500
                self.windowWidth = 500
                self.fps = 54
                self.run = True
                self.clock = pygame.time.Clock()
                self.player = Player(250, 410, 64, 64)
                self.enemy1 = Enemy(100, 417, 64, 64, 400)
                self.enemy2 = Enemy(50, 417, 64, 64, 300)
                self.enemies = [self.enemy1, self.enemy2]
                self.window = Window(self.windowHeight, self.windowWidth, self.player, self.enemies)
                
        def startGame(self):
                pygame.init()
                
                while self.run:
                        self.clock.tick(self.fps) # 54 fps
                        
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        run = False

                        for projectile in self.player.projectiles:
                                if projectile.x < self.windowWidth and projectile.x > 0: #projectile onscreen
                                        projectile.x += projectile.vel
                                else: #projectile offscreen
                                        self.player.projectiles.pop(self.player.projectiles.index(projectile))
                                        
                                
                        keys = pygame.key.get_pressed() #array of keyboard keys

                        if keys[pygame.K_ESCAPE]:
                                self.run = False
                                
                        if keys[pygame.K_SPACE]:
                                if self.player.left: #facing left then jump
                                        self.player.direction = -1
                                else: #facing right then jump or upon spawn
                                        self.player.direction = 1
         
                                if len(self.player.projectiles) <= self.player.ammo:
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

                        self.window.updateWindow()
                        
                self.stopGame()
                
        def stopGame(self):
                pygame.quit()
                     
def main():
        game = Game()
        game.startGame()
 
if __name__ == "__main__":
        main()
        
                
