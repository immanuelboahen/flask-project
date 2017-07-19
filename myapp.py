from flask import Flask, render_template, send_from_directory
import os
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect ("moorhouseassociates.com", 1883, 60)

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html", to="Sam Moorhouse")

@app.route('/btn')
def btn():
	return ("button clicked")
	client.publish ("test/all", "this is my message to you")

@app.route('/whereami')
def whereami():
	return "Kdua"

"app.route ('/linux')
def linux():
	return render_template('linux.html')

@app.route('/hello/<name>')
def foo(name):
    return render_template('index.html', to=name)
