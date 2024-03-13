from flask import Flask, jsonify, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import subprocess
import requests
import time


app = Flask(__name__)

# Load the pre-trained TensorFlow model
model_path = 'https://github.com/mohammad1774/project-forest-fire/blob/master/trained_model_custom_2.h5'

model = load_model(model_path)

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(255, 255))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

@app.route('/predict', methods=['POST'])
def predict():
    try:
        img_file = request.files['image']
        img_path = "temp_image.jpg"
        img_file.save(img_path)
        input_data = preprocess_image(img_path)
        predictions = model.predict(input_data)
        predicted_class = np.argmax(predictions, axis=1)
        return jsonify({'predicted_class': int(predicted_class), 'predictions': predictions.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    
    app.run(host='0.0.0.0',port=5000)
