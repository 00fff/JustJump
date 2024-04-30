import pygame
import os
import random 

# Initialize pygame and universeal variables 
pygame.init()
clock = pygame.time.Clock()
FPS = 60
falling = True 
gravity = 0.25


# Change directory to "poketale" file in USB
path = "/Volumes/USB1/JustJump/" #E:/JustJump/
os.chdir(path)


# Set Screen Size and color white
screen_width = 400
screen_height = 600
White = (255, 255, 255)

# background and assests 
bg = pygame.image.load("img/bg.png")
mc1 = pygame.image.load("img/mc.png")
mc2 = pygame.transform.scale(mc1, (50, 50))
# Variables 
keys = pygame.key.get_pressed()
vel = 2
# Create game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('JustJump')

# Classes 
class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(mc1, (50, 50))
        self.flip = False
        self.width = 30
        self.height = 45
        self.vel = 0
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.clicked = False
        self.gravity = 0.25
        self.jump_force = -10

    def update(self, keys):
        # Check if the player is falling
        if self.rect.bottom < screen_height:
            # Apply gravity
            self.vel += self.gravity
            # Update player's position based on velocity
            self.rect.y += int(self.vel)
            
            # Check if the player has reached the ground
            if self.rect.bottom >= screen_height:
                # Reset velocity and adjust position slightly above the ground
                self.vel = 0
                self.rect.y -= 300
                

                    
                    
                    
                    
                    
                    
        if keys[pygame.K_LEFT]:
            pygame.transform.flip(self.image, True, False)
            self.flip = True
            self.rect.x -= vel
        if keys[pygame.K_RIGHT]:
            pygame.transform.flip(self.image, False, False)
            self.flip = False
            self.rect.x += vel


    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False),(self.rect.x - 12, self.rect.y - 3))
        pygame.draw.rect(screen, White, self.rect, 2)
    


# Instance of Classes 
mc = Player(screen_width // 2, screen_height - 150)


run = True
while run == True: 
    screen.blit(bg, (0, 0))
    keys = pygame.key.get_pressed()  # Move inside the game loop to update continuously
    mc.update(keys)
    # keyboard inputs 
    mc.draw()
    clock.tick(FPS) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit