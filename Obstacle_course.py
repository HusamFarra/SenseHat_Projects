from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()
w = (0,0,0)

game_space = [w,w,w,w,w,w,w,w,
              w,w,w,w,w,w,w,w,
              w,w,w,w,w,w,w,w,
              w,w,w,w,w,w,w,w,
              w,w,w,w,w,w,w,w,
              w,w,w,w,w,w,w,w,
              w,w,w,w,w,w,w,w,
              w,w,w,w,w,w,w,w]

def rand_col():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  return (r,g,b)
x = random.randint(0,7)
y = random.randint(0,7)

def update_space(x,y,col):
  p = 8*x + y
  game_space[p] = col
  
count = 0
while True:
  count += 1
  x = random.randint(0,7)
  y = random.randint(0,7)
  update_space(x,y,rand_col())
  if count % 2 == 0:
    update_space(x,y,(0,0,0))
  sense.set_pixels(game_space)
  sleep(0.5)
  #SPARKLE
