import pygame
import random

# Initialize the game
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")

# Player
playerImg = pygame.image.load('player.png')
playerImg = pygame.transform.scale(playerImg, (64, 64))
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyImg = pygame.transform.scale(enemyImg, (64, 64))
enemyX = random.randint(0,736)
enemyY = random.randint(50,150)
enemyX_change = 0.3
enemyY_change = 40

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletImg = pygame.transform.scale(bulletImg, (10, 10))
bulletX = 0
bulletY = 480
bulletY_change = 0.8
# Ready - No bullet on screen
# Fire - Bullet is on screen
bullet_state = "ready"


def player(x,y):
    screen.blit(playerImg, (x, y))


def enemy(x,y):
    screen.blit(enemyImg, (x, y))

def fire(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# Game loop
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Event listeners
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire(bulletX, bulletY)
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    # Player Movement
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >=736:
        playerX = 736


    # Enemy Movement
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >=736:
        enemyX_change = -0.3
        enemyY += enemyY_change

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire(bulletX,bulletY)
        bulletY -= bulletY_change
        

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()