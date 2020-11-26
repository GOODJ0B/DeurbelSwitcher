import flask
from flask_cors import CORS
import RPi.GPIO as GPIO

app = flask.Flask(__name__)
CORS(app)

doorbellGPIO = 21
doorbellIsOn = True


@app.route('/', methods=['GET'])
def home():
    return 'Online.'


@app.route('/on', methods=['GET'])
def doorbellOn():
    GPIO.cleanup()
    global doorbellIsOn
    doorbellIsOn = True
    return doorbellIsOn


@app.route('/off', methods=['GET'])
def doorbellOff():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(doorbellGPIO, GPIO.OUT)
    global doorbellIsOn
    doorbellIsOn = False
    return doorbellIsOn


@app.route('/check', methods=['GET'])
def doorbellOff():
    global doorbellIsOn
    return doorbellIsOn


app.run(host='0.0.0.0')