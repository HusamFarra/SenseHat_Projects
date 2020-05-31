from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

o=(255,255,255)
b=(0,0,0)

one_img= [o,o,o,o,o,o,o,o,
          o,o,o,o,o,o,o,o,
          o,o,o,o,o,o,o,o,
          o,o,o,b,b,o,o,o,
          o,o,o,b,b,o,o,o,
          o,o,o,o,o,o,o,o,
          o,o,o,o,o,o,o,o,
          o,o,o,o,o,o,o,o]
          
two_img = [o,o,o,o,o,o,o,o,
          o,b,b,o,o,o,o,o,
          o,b,b,o,o,o,o,o,
          o,o,o,o,o,o,o,o,
          o,o,o,o,o,o,o,o,
          o,o,o,o,o,b,b,o,
          o,o,o,o,o,b,b,o,
          o,o,o,o,o,o,o,o]
          
three_img = [o,o,o,o,o,o,o,o,
            o,b,b,o,o,o,o,o,
            o,b,b,o,o,o,o,o,
            o,o,o,b,b,o,o,o,
            o,o,o,b,b,o,o,o,
            o,o,o,o,o,b,b,o,
            o,o,o,o,o,b,b,o,
            o,o,o,o,o,o,o,o]
            
            
four_img = [o,o,o,o,o,o,o,o,
            o,b,b,o,o,b,b,o,
            o,b,b,o,o,b,b,o,
            o,o,o,o,o,o,o,o,
            o,o,o,o,o,o,o,o,
            o,b,b,o,o,b,b,o,
            o,b,b,o,o,b,b,o,
            o,o,o,o,o,o,o,o]
            
five_img = [o,o,o,o,o,o,o,o,
            o,b,b,o,o,b,b,o,
            o,b,b,o,o,b,b,o,
            o,o,o,b,b,o,o,o,
            o,o,o,b,b,o,o,o,
            o,b,b,o,o,b,b,o,
            o,b,b,o,o,b,b,o,
            o,o,o,o,o,o,o,o]
            
six_img = [o,o,o,o,o,o,o,o,
            o,b,b,o,o,b,b,o,
            o,b,b,o,o,b,b,o,
            o,b,b,o,o,b,b,o,
            o,b,b,o,o,b,b,o,
            o,b,b,o,o,b,b,o,
            o,b,b,o,o,b,b,o,
            o,o,o,o,o,o,o,o]
            
dice = [one_img,two_img,three_img,four_img,five_img,six_img]
            

def roll():
  for i in range(5):
    sense.set_pixels(dice[randint(1,6)-1])
    sleep(0.1)
    sense.clear()

            
def number_gen(event):
  for event in sense.stick.get_events():
    if event.action == "pressed":
      val = randint(1,6)
      roll()
      print(val)
      sense.set_pixels(dice[val-1])
      sleep(2)
      sense.clear()
      
while True:
  number_gen(sense.stick.direction_any)
