from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
sense.clear()

o = (0,0,0)

screen = [o,o,o,o,o,o,o,o,
          o,o,o,o,o,o,o,o,
          o,o,o,o,o,o,o,o,
          o,o,o,o,o,o,o,o,
          o,o,o,o,o,o,o,o,
          o,o,o,o,o,o,o,o,
          o,o,o,o,o,o,o,o,
          o,o,o,o,o,o,o,o]

sparkles = []
max = 8

def rand_col():
  r = randint(0,255)
  g = randint(0,255)
  b = randint(0,255)        
  return(r,g,b)        
          
def update_space(x,y,col):
  p = x + 8*y
  screen[p] = col

while True:  
  x = randint(0,7)
  y = randint(0,7)
  pos = [x,y]
  sparkles.append(pos)
  if len(sparkles)==max:
    clr = sparkles.pop(0)
    update_space(clr[0],clr[1],o)
  update_space(x,y,rand_col())
  sense.set_pixels(screen)
  sleep(0.01)
  
  #SPARKLES
