from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "hello this is Immanuels website. Enjoy"

@app.route('whereami'):
def whereami():
	return "k.t.u lab 1"

if __name__== '__main__':
	app.run(host="0.0.0.0")
