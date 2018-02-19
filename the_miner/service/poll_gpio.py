# Imports
import RPi.GPIO as GPIO
import time

# WebApp Imports
from the_miner.webapp import counter, SensorGPIO, SensorAvg, ChangeSense

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(5, GPIO.IN)
GPIO.setup(6, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(21, GPIO.IN)
GPIO.setup(20, GPIO.OUT)

# f = open('my_file.txt', 'r')
# print f.read()

# d (digital)             p (pwm)
# r (read)    w (write)   frequency
# pin number
# 1 or 0                  duty cycle
# eg) dw12 = digital write 12.


for i in range(0, 10):
    for i in range(0, 6):

        timeHigh1 = time.clock()
        GPIO.output(20, 0)

        while GPIO.input(SensorGPIO[i]) == 1:
            pass
        timeHigh = (time.clock() - timeHigh1) * 1000000
        GPIO.output(20, 1)

        SensorAvg[i] = (SensorAvg[i] * 30 + timeHigh) / 31
        ChangeSense[i] -= 1
        if(abs(timeHigh - SensorAvg[i]) > 100):
            ChangeSense[i] += 3
        if(ChangeSense[i] > 10):
            spaces = ""
            for j in range(0, i):
                spaces += " "
            print spaces + str(i)
        time.sleep(.002)

    time.sleep(0.1)

print SensorAvg

"""
  dataString = str(GPIO.input(5));
  GPIO.output(5, 0);
  time.sleep(1);
  dataString += str(GPIO.input(5));
  dataString += str(GPIO.input(6));
  dataString += str(GPIO.input(13));
  dataString += str(GPIO.input(19));
  dataString += str(GPIO.input(26));
  dataString += str(GPIO.input(21));
  print time.clock();
"""
