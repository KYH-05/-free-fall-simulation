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
p=1.293
C=0.47#공기저항 계수-구일때
A=float(input("공기 받는 면적(m^2):"))
x=sy.symbols('x')
v_end = ((2 * m * g) / (p * C * A))**(1/2)
v_t = v_end * sy.tanh(g * x / v_end)
x_t=sy.integrate(v_t)
#print("v_end",v_end)
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
  l=100+x_t.subs({x:t})*h_p
  #l=float(l)
  b_y=float(l)
  #print(b_y)
  # ----------------------------------------------------
  draw()
  draw_h_displayer()
  drawBall()
  # ----------------------------------------------------
  if b_y>800:
    print('시간',t)
    v_t=v_t.subs({x:t})
    print('속력',v_t)
    #print('이동 거리',l/h_p)
    #print(v_end)
    #print('종단속도v',v_t)
    time.sleep(100000)
  # ----------------------------------------------------
  pygame.display.update()
  clock.tick(60)
#----------------------------------------------------