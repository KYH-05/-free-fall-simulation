import pygame
import time
import sympy as sy
import numpy as np
#5.681030804
#----------------------------------------------------
pygame.init()
screen_width = 500
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("P")
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 1)
#----------------------------------------------------
m=float(input("물체의 무게(kg):"))
h=float(input("물체의 높이(m):"))
h_p=700/h
g=9.80665
t=0
ft=0#처음시간
#----------------------------------------------------
h_displayer_H=800
h_displayer_W=10
h_displayer_X=0
h_displayer_Y=0
h_displayer= pygame.Rect(h_displayer_X, h_displayer_Y, h_displayer_W, h_displayer_H)
def draw_h_displayer():
  pygame.draw.rect(screen, (0, 100,200), h_displayer)
#----------------------------------------------------
b_x=250
b_y=100
def drawBall():
    pygame.draw.circle(screen, (0, 100,200), (b_x, b_y), 7)
def draw():
  screen.fill((0,0,0))
  drawBall()
#----------------------------------------------------
running = True
ft=time.time()
while running:
  # ----------------------------------------------------
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  # ----------------------------------------------------
  t=time.time()-ft
  md=(1/2)*g*(t)**2#moving distance
  l=100+md*h_p#location
  b_y=l
  draw()
  draw_h_displayer()
  drawBall()
  if b_y>800:
    print('시간',t)
    print('속도',g*t)
    time.sleep(100000)
  # ----------------------------------------------------
  pygame.display.update()
  clock.tick(60)
#----------------------------------------------------