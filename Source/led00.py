# coding: UTF-8
# 押している間LEDがつくプログラム

import RPi.GPIO as GPIO
import time

# 変数宣言
i = 0
outPin = 14
sleepTime = 2

# GPIO初期化
GPIO.setmode(GPIO.BCM)          # ポート指定をGPIOのIDで行う
GPIO.setup(outPin, GPIO.OUT)    # 使用するGPIOを初期化する （今回は14番のGPIO）

    GPIO.output(outPin, True)       # GPIOを出力（LED点灯）
    time.sleep(sleepTime)           # 指定時間待機（今回は２秒）
    GPIO.output(outPin, False)      # GPIOを出力（LED消灯）

GPIO.cleanup()