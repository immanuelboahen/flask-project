from gpiozero import LED, Button
from signal import pause
from time import sleep
import paho.mqtt.client as mqtt

      
        
led = LED(17)

	
CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }
        
message = "incoming message"

def name():
	for char in " immanuel":
		letters[chr]

def on_message(client, userdata, message):
	print message.payload
	

def on_connect(client, userdata, flags, code):
	print "connected: " + str(code)
	client.subscribe("test/all")
	
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("moorhouseassociates.com", 1883, 60)

client.loop_forever()
