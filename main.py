import sys
import Adafruit_DHT
import time
import RPi.GPIO as GPIO

temp_sensor = 11
temp_pin = 4

led_pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

while True:
    temperature = Adafruit_DHT.read_retry(temp_sensor, temp_pin)[1]
    if temperature > 45 or temperature < 5:
        for i in range(0, 10):
            GPIO.output(led_pin, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(led_pin, GPIO.LOW)
            time.sleep(0.2)



