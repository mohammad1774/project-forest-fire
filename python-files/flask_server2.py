from flask import Flask, jsonify, request
#from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow import argmax
from tensorflow.keras.models import load_model
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load the pre-trained TensorFlow model
model_path = 'D:\\project-forest\\MyDrive\\capstone-project\\training_log_custom\\trained_model\\hdf5_model\\trained_model_custom.h5'
model = load_model(model_path)


def preprocess_image(img_path):
    # Load and preprocess the image
    img = image.load_img(img_path, target_size=(224, 224))  # Adjust target size based on your model's input size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize the pixel values
    return img_array

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the image file from the request
        print('connected')
        img_file = request.files['image']
        
        # Save the image to a temporary file
        img_path = "temp_image.jpg"
        img_file.save(img_path)
        
        # Preprocess the image
        input_data = preprocess_image(img_path)
        
        # Make predictions
        predictions = model.predict(input_data)
        
        # Get the predicted class (assuming single-class output)
        predicted_class = np.argmax(predictions, axis=1)
        
        # Return predictions as JSON
        return jsonify({'predicted_class': int(predicted_class), 'predictions': predictions.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
