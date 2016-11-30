# coding: UTF-8
# 一度押したらLEDをがついてもう一度押すと消えるプログラム

import RPi.GPIO as GPIO
import time
from time import sleep

# 変数宣言
i = 0
outPin = 14
inPin = 15
sleepTime = 2
ledState = False 

# GPIO初期化処理
GPIO.setmode(GPIO.BCM)
GPIO.setup(outPin, GPIO.OUT)
GPIO.setup(inPin, GPIO.IN)

try:
   # メインループ
    while True:
        if ledState:
            GPIO.output(outPin, GPIO.HIGH)
        else:
            GPIO.output(outPin, GPIO.LOW)
        sleep(0.01)
        if GPIO.input(inPin) ==  GPIO.HIGH:
            ledState = not(ledState)

except KeyboardInterrupt:
    pass


GPIO.cleanup()