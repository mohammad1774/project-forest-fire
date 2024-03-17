from flask import Flask, jsonify, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import subprocess
import requests
import time


app = Flask(__name__)

# Load the pre-trained TensorFlow model
model_path = 'C:\\Users\\Mohammad\\Documents\\GitHub\\project-forest-fire\\MyDrive\\capstone-project\\training_log_custom\\trained_model\\hdf5_model\\trained_model_custom.h5'

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
    ngrok_api = subprocess.Popen(['C:\\Users\\Mohammad\\Documents\\GitHub\\project-forest-fire\\ngrok.exe','http','5000'])

    time.sleep(5)
    ngrok_api_url = requests.get('http://localhost:4040/api/tunnels').json()['tunnels'][0]['public_url']

    print("Ngrok URL:", ngrok_api_url)

    with open('C:\\Users\\Mohammad\\Documents\\GitHub\\project-forest-fire\\python-files\\url.txt','w') as file:
        file.writelines(ngrok_api_url)

    app.run()
