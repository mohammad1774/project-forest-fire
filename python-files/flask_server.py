# Example: Flask app for image data in a file named app.py
from flask import Flask, jsonify, request
from flask_ngrok import run_with_ngrok
from tensorflow import argmax
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

img_size = [255,255]
app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run

# Load the trained model
model_path = 'D:\\project-forest\\MyDrive\\capstone-project\\training_log_custom\\trained_model\\hdf5_model\\trained_model_custom.h5'

def preprocess_image(img_path):
    # Load and preprocess the image
    img = image.load_img(img_path, target_size=img_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize the pixel values
    return img_array

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the image file from the request
        img_file = request.files['image']
        # Save the image to a temporary file
        img_path = "/tmp/temp_image.jpg"
        img_file.save(img_path)
        # Preprocess the image
        input_data = preprocess_image(img_path)
        # Make predictions
        predictions = model.predict(input_data)
        
        predictions = argmax(predictions)

        # Return predictions as JSON
        return jsonify(predictions.tolist())
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run()
