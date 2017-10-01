# coding: UTF-8
# 押している間LEDがつくプログラム

import RPi.GPIO as GPIO
import time
from time import sleep
# 変数宣言
i = 0
outPin = 14
inPin = 15
sleepTime = 2

# GPIO初期化処理
GPIO.setmode(GPIO.BCM)
GPIO.setup(outPin, GPIO.OUT)
GPIO.setup(inPin, GPIO.IN)

try:
    # メインループ
    while True:
        print(GPIO.input(inPin))
        if GPIO.input(inPin) == GPIO.HIGH:
            GPIO.output(outPin, GPIO.HIGH)
        else:
            GPIO.output(outPin, GPIO.LOW)
        sleep(0.01)

# ユーザーが割り込み処理（プログラム停止など）を行った場合こっちに飛ぶ
except KeyboardInterrupt:
    pass


GPIO.cleanup()