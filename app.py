#Import necessary libraries
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import tensorflow as tf
import keras
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import os

# Create flask instance
app = Flask(__name__)

#Set maximum file size as 5MB.
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024


# Function to load and prepare the image in right shape
def read_image(filename):
    # Load the image
    img = load_img(filename, target_size=(200, 200))
    # Convert the image to array
    img = img_to_array(img)
    # Reshape the image into a sample of 1 channel
    img = img.reshape(1, 200, 200, 3)
    # Prepare it as pixel data
    
    img = img / 255.0
    return img

@app.route("/", methods=['GET', 'POST'])
def home():

    return render_template('index.html')

@app.route("/predict", methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        file_path = os.path.join('static/images', filename)
        file.save(file_path)
        img = read_image(file_path)
        # Predict the class of an image
                
        model1 = load_model('potato1.h5')
        result = model1.predict(img).round(3)
        pred = np.argmax(result)
           
        if pred==0:
            product='Tomato LeafMiner'
        else:
            product='Tomato LeafMiner'
            
    print(pred)
    
    return render_template('project.html', product = product,user_image = file_path)


#{% if class_prediction[0][0] > 0.50 %}
#<h1>I think its a horse</h1>
#{%else%}
#<h1><b> looks like a human </b></h1>
#{%endif%}
            
if __name__ == "__main__":
    app.run(debug=True)
