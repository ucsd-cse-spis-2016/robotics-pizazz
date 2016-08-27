import RPi.GPIO as GPIO, time
from sonar import *

try:
   while True:
       dist = getDistance(echoPin=8, trigPin=8)
       print dist
       time.sleep(1)

except KeyboardInterrupt:
       GPIO.cleanup()

