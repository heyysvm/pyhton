import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Collector")

clock = pygame.time.Clock()

player_size = 40
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

coin_size = 30
coin_x = random.randint(0, WIDTH - coin_size)
coin_y = random.randint(0, HEIGHT - coin_size)

score = 0

print("Game Started! Catch the yellow coin!")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    coin_rect = pygame.Rect(coin_x, coin_y, coin_size, coin_size)

    if player_rect.colliderect(coin_rect):
        score += 1
        print(f"Score: {score}") 
        coin_x = random.randint(0, WIDTH - coin_size)
        coin_y = random.randint(0, HEIGHT - coin_size)

    screen.fill((30, 30, 30))

    pygame.draw.rect(screen, (0, 255, 0), player_rect)
    pygame.draw.rect(screen, (255, 255, 0), coin_rect)

    pygame.display.update()
    clock.tick(100)