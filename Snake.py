from sense_hat import SenseHat
from time import sleep
from random import randint
import random


sense = SenseHat()

speed = 0.4
score = 0
u = 1
d = 2
l = 3
r = 4
length = 2
dir = 1

snake = [[4,7],[3,7]]
apple = []

w = (0,0,0)
a = (255,0,0)
b = (0,200,0)
o = (255,255,255)
game_space = [w,w,w,w,w,w,w,w,
              w,w,w,w,w,w,w,w,
              w,w,w,w,w,w,w,w,
              w,w,w,w,w,w,w,w,
              w,w,w,w,w,w,w,w,
              w,w,w,w,w,w,w,w,
              w,w,w,w,w,w,w,w,
              w,w,w,b,b,w,w,w]
              
def update_space(x, y, colour):
  #index element from coordinate
  p = 8 * y + x
  game_space[p] = colour
  sense.set_pixels(game_space)


def collision(x,y) :
  if x>7 or x<0 or y>7 or y<0:
    return True
  else:
    for segment in snake:
      if segment[0] == x and segment[1] == y:
        return True
      else:
        return False

def createApple():
  badApple = True
  while badApple:
    x = randint(0, 7)
    y = randint(0, 7)
    badApple = collision(x, y)
  global apple
  apple = [x, y]
  sense.set_pixel(x, y, a)
        
def addSegment(x, y):
  global snake
  sense.set_pixel(x, y, b)
  snake.insert(0, [x, y])

  if len(snake) > length:
    lastSegment = snake[-1]
    sense.set_pixel(lastSegment[0], lastSegment[1], w)
    snake.pop()

def move(event):
  global score
  global length
  global dir
  newSegment = [snake[0][0], snake[0][1]]
  if event.action == "pressed":
    if event.direction == "up":
      if dir != d:
        dir = u
        newSegment[1] -= 1
    elif event.direction == "down":
      if dir != u:
        dir = d
        newSegment[1] += 1
    elif event.direction == "left":
      if dir != r:
        dir = l
        newSegment[0] -= 1
    elif event.direction == "right":
      if dir != l:
        dir = r
        newSegment[0] += 1

    if collision(newSegment[0], newSegment[1]):
      snakehead = snake[0]
      for flashHead in range (0, 5):
        sense.set_pixel(snakehead[0], snakehead[1], b)
        sleep(0.1)
        sense.set_pixel(snakehead[0], snakehead[1], w)
        sleep(0.1)
      sense.show_message("GAME OVER!", scroll_speed=0.05)
      sense.show_message("Score " + str(score), scroll_speed=0.05)

    else:
      addSegment(newSegment[0], newSegment[1])
      if newSegment[0] == apple[0] and newSegment[1] == apple[1]:
        length += 1
        print (length)
        score += 1
        createApple()
    
      return True
  

sense.clear()
sense.set_pixels(game_space)
createApple()

print("Press Joystick to start")

running = True

while running:
  playing = True
  while playing:
    sleep(0.5)
    for event in sense.stick.get_events():
      playing = move(event)
      print (dir)
      #print (length)
