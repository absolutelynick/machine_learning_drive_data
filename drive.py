#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""
Author:  Nick Hughes
Company: Rigstore

Created: 2019

(C) 2019 >

Using Flask & Socket.io to establish bi-directional client-server communication.

This is done to connect our model to the simulation.

"""

import socketio
import eventlet
import numpy as np
from flask import Flask
from keras.models import load_model
import base64
from io import BytesIO
from PIL import Image
import cv2

sio = socketio.Server()
app = Flask(__name__)
speed_limit = 20

def process_image(img):
    """ Setting our image as we did in the machine model training mode. """
    img = img[60:135,:,:]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img,  (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img/255
    return img

def get_image(data):
    """ Taking the image from the scene and getting it ready for processing. """
    image = Image.open(BytesIO(base64.b64decode(data['image'])))
    image = np.asarray(image)
    image = process_image(image)
    image = np.array([image])
    return image

@sio.on('telemetry')
def telemetry(sid, data):
    """ As soon as a connection is made then this function will be kicked off """
    speed = round(float(data['speed']), 2)

    image = get_image(data)

    angle = round(float(model.predict(image)), 2)

    throttle = round((1.0 - speed/speed_limit), 2)

    direction = "L: " if angle < 0 else "R: " if angle == 0 else "S: "

    print('Angle: %s %s | Throttle: %s | Speed: %s' % (direction, angle, throttle, speed ))

    send_control(angle, throttle)

def get_speed(angle, speed):
    """ Set a variable speed depending on the angle passed.

        Faster for straighter parts of the road

        Slower for harsher angles
    """

    if (angle > 0.5) or (angle < -0.5):
        speed -= speed*0.1

    elif (angle < 0.5) or (angle > -0.5):
        speed += speed*0.1

    return speed

def user_feedback(data): ## TODO
    """ Pass the user feedback for the drive and the angles that were given. """

    # Get the image name

    # Get the image angle

    # Save out our image

    pass

@sio.on('connect')
def connect(sid, environ):
    """ The very first and initial connection """
    print('Connected')
    send_control(0, 0)

def send_control(steering_angle, throttle):
    """ Telling the car what actions to take. """
    sio.emit('steer', data = {
        'steering_angle': steering_angle.__str__(),
        'throttle': throttle.__str__()
    })

if __name__ == '__main__':
    model = load_model('model.h5')
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)
