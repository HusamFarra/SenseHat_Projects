from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

while True:
  t = sense.get_temperature()
  p = sense.get_pressure() 
  h = sense.get_humidity()
  t = round(t, 1)  
  p = round(p, 1)  
  h = round(h, 1)    
  message = "Temperature: " + str(t) + " C" + "Pressure: " + str(p)+"hPa"+ " Humidity: " + str(h)+ "%"
  print(message)
  sleep(1)
  
  p0 = 1012.25
  h = 44331 *(1- pow( (p/p0),(1/5.2558) ) )
  print("Current altitude is: ",h, " meters")
  sleep(2)
  
  o = sense.get_orientation()
  acceleration = sense.get_accelerometer_raw()
  pitch = o["pitch"]
  roll = o["roll"]
  yaw = o["yaw"]
  
  x = acceleration['x']
  y = acceleration['y']
  z = acceleration['z']
  x=round(x, 0)
  y=round(y, 0)
  z=round(z, 0)
  
  print("pitch: ", pitch, " roll: ", roll, " yaw: ", yaw)
  print("x: ", x, " y: ", y, " z: ", z)
  sleep(2)
  
