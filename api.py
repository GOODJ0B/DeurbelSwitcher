import flask
from flask_cors import CORS
import RPi.GPIO as GPIO

app = flask.Flask(__name__)
CORS(app)

doorbellGPIO = 21

@app.route('/', methods=['GET'])
def home():
    return 'Online.'


@app.route('/on', methods=['GET'])
def doorbellOn():
    GPIO.cleanup()
    return True

@app.route('/off', methods=['GET'])
def doorbellOff():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(doorbellGPIO, GPIO.OUT)
    return True

app.run(host='0.0.0.0')