import pygame

class Player:
        walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
        walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
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

        def animatePlayer(self, window):
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
                                        
class Enemy:
        walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
        walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

        def __init__(self, x, y, width, height, end):
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.end = end
                self.path = [self.x, self.end] #start and end of path
                self.walkCount = 0
                self.vel = 3

        def animateEnemy(self, window):
                self.moveEnemy()
                
                if self.walkCount + 1 >= 55:
                        self.walkCount = 0

                if self.vel > 0: #walking right
                        window.blit(self.walkRight[self.walkCount//5], (self.x, self.y))
                        self.walkCount +=1
                else: #walking left
                        window.blit(self.walkLeft[self.walkCount//5], (self.x, self.y))
                        self.walkCount +=1
                

        def moveEnemy(self):
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
        shuriken = pygame.image.load('shuriken.png')

        def __init__(self, x, y, direction):
                self.x = x
                self.y = y
                self.direction = direction
                self.vel = 8 * direction

        def animateProjectile(self, window):
                #pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)
                window.blit(self.shuriken, (self.x, self.y))
                
class Window:
        bg = pygame.image.load('bg.jpg')
        
        def __init__(self, windowHeight, windowWidth, player, enemy):
                self.windowHeight = windowHeight
                self.windowWidth = windowWidth
                self.window = pygame.display.set_mode((self.windowHeight, self.windowWidth))
                self.player = player
                self.enemy = enemy
                pygame.display.set_caption("Spaghetti User Interface")

        def updateWindow(self):
                self.window.blit(self.bg, (0,0)) 
                self.player.animatePlayer(self.window)
                self.enemy.animateEnemy(self.window)
                for projectile in self.player.projectiles:
                        projectile.animateProjectile(self.window)
                pygame.display.update()
                
class Game:
        def __init__(self):
                self.windowHeight = 500
                self.windowWidth = 500
                self.fps = 54
                self.run = True
                self.clock = pygame.time.Clock()
                self.player = Player(250, 410, 64, 64)
                self.enemy = Enemy(100, 417, 64, 64, 400)
                self.window = Window(self.windowHeight, self.windowWidth, self.player, self.enemy)
                
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
                                if self.player.left:
                                        self.player.direction = -1
                                elif self.player.right:
                                        self.player.direction = 1
                                else: #upon spawn - right
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
                                self.player.right = True
                                self.player.left = False
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
        
                
