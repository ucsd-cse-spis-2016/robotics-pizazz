# Pizazz Motor functions 
# Moves: Forward, Reverse, turn Right, turn Left, Stop 

import RPi.GPIO as GPIO, time

#use physical pin numbering
GPIO.setmode(GPIO.BOARD)

slowspeed =20
fastspeed = 100
avgspeed = 50
rightTop = 19
rightBottom = 21
leftTop = 24
leftBottom = 26
#use pwm on inputs so motors don't go too fast
# Pins 19, 21 Right Motor
# Pins 24, 26 Left Motor
GPIO.setup(rightTop, GPIO.OUT)
GPIO.setup(rightBottom, GPIO.OUT)
GPIO.setup(leftTop, GPIO.OUT)
GPIO.setup(leftBottom, GPIO.OUT)

rightTopPWM=GPIO.PWM(rightTop, 20)
rightTopPWM.start(0)

rightBottomPWM=GPIO.PWM(rightBottom, 20)
rightBottomPWM.start(0)

leftTopPWM = GPIO.PWM(leftTop,20)
leftTopPWM.start(0)

leftBottomPWM=GPIO.PWM(leftBottom,20)
leftBottomPWM.start(0)

def forward(speed=avgspeed):
   rightTopPWM.ChangeDutyCycle(speed)
   rightBottomPWM.ChangeDutyCycle(0)
   leftTopPWM.ChangeDutyCycle(speed)
   leftBottomPWM.ChangeDutyCycle(0)
   print('forward')

def reverse(speed=avgspeed):
   rightTopPWM.ChangeDutyCycle(0)
   rightBottomPWM.ChangeDutyCycle(speed)
   leftTopPWM.ChangeDutyCycle(0)
   leftBottomPWM.ChangeDutyCycle(speed)
   print('reverse')

def turnleft(rspeed=fastspeed,lspeed=slowspeed ):
   if rspeed < lspeed:
      print "Incorrect paramters: right motor speed should be greater than left motor speed"
      return
   rightTopPWM.ChangeDutyCycle(rspeed)
   rightBottomPWM.ChangeDutyCycle(0)
   leftTopPWM.ChangeDutyCycle(lspeed)
   leftBottomPWM.ChangeDutyCycle(0)
   print('left')

def turnright(rspeed=slowspeed, lspeed=fastspeed):
   if rspeed > lspeed:
      print "Incorrect paramters: right motor speed should be less than left motor speed"
      return
   rightTopPWM.ChangeDutyCycle(rspeed)
   rightBottomPWM.ChangeDutyCycle(0)
   leftTopPWM.ChangeDutyCycle(lspeed)
   leftBottomPWM.ChangeDutyCycle(0)
   print('right')

def stopall():
   rightTopPWM.ChangeDutyCycle(0)
   rightBottomPWM.ChangeDutyCycle(0)
   leftTopPWM.ChangeDutyCycle(0)
   leftBottomPWM.ChangeDutyCycle(0)
   print('stop')
