#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 17:22:24 2020

@author: pushkara
"""
from flask import Flask,request, render_template
from werkzeug.utils import secure_filename
import os
from image_processing import print_to_image
import cv2

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        output = print_to_image(file_path)
        if(type(output)==str):
            return 'error.png'
        else:
            cv2.imwrite('static/outputs/'+f.filename, output)
            return f.filename

           
    return None



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
