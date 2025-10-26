
import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
FPS = 60


class Player:
  X = 0
  Y = 0


p1 = Player()
p2 = Player()

p2.X = 100


def show_player(p):
  pygame.draw.rect(screen, (247, 0, 21), (p.X, p.Y + HEIGHT - 100, 100, 100))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
      
  keys = pygame.key.get_pressed()

  if keys[pygame.K_LEFT]: 
    p1.X -= 10
  if keys[pygame.K_RIGHT]: p1.X += 10
  if keys[pygame.K_UP]: p1.Y -= 10

  if keys[pygame.K_DOWN]: p1.Y += 10


  if keys[pygame.K_w]: p2.Y -= 10
  if keys[pygame.K_s]: p2.Y += 10
  if keys[pygame.K_a]: p2.X -= 10
  if keys[pygame.K_d]: p2.X += 10

  screen.fill((0, 0, 0))

  show_player(p1)
  show_player(p2)
  pygame.display.flip()
  clock.tick(FPS)



