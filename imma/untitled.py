try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges. You can achieve this by using 'sudo' to run your script")
# get ready to use gpio from pi
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
# use channel 15, i.e., P22
channel = 16
# gpio is used for output
GPIO.setup(channel, GPIO.OUT)

def LED_on():
    GPIO.output(channel,GPIO.HIGH)
def LED_off():
    GPIO.output(channel,GPIO.LOW)

# -----------------------

from MichaelMorse import MichaelMorse

m = MichaelMorse(15,on=LED_on,off=LED_off)
m.send("hello world de kc7dbu")
