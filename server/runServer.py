from flask import Flask, render_template, request, redirect
import socket

# for keyboard interaction
import Quartz
from pykeyboard import PyKeyboard #https://github.com/SavinaRoja/PyUserInput
from time import sleep
from flask_sslify import SSLify


app = Flask(__name__)
sslify = SSLify(app)

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print('Actual IP address: ' + local_ip)
print('Actual hostname: ' + hostname)

#initialize the keyboard simulator
keyboard = PyKeyboard()

# @app.before_request
# def before_request():
#     if not request.is_secure and app.env != "development":
#         url = request.url.replace("http://", "https://", 1)
#         code = 301
#         return redirect(url, code=code)

@app.route("/")
def homepage():
    return render_template('homepage.html', hostname=hostname, local_ip=local_ip)

@app.route("/gamepad")
def gamepad():
    return render_template('gamepad.html', hostname=hostname, local_ip=local_ip)

@app.route("/button/x")
def hello():
    #presses the key
    keyboard.tap_key('x')

    return "Key was pressed"


if __name__ == "__main__":
    app.run(debug=True, host= local_ip, ssl_context=('cert.pem', 'key.pem'))