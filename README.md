# Fire Detection System Readme
This repository contains the code and resources for a fire detection system developed as a capstone project. The system aims to identify fires from images obtained from surveillance systems or other sources using deep learning techniques. Below is an overview of the project and instructions for setting up and using the system.

## Objective
The goal of this project is to create a fire detection system that accurately identifies fires, smoke, and non-fire scenarios from images. The system utilizes a Convolutional Neural Network (CNN) architecture implemented using the Keras framework.

## Dataset
The dataset used for training and testing the model comprises approximately 30,000 images with 10,000 images for each category: fire, non-fire, and smoke. The dataset is available for download here.

## Constraints
The project utilizes a deep learning neural network for classification.
Computational resources and hardware limitations may affect model training.
Preprocessing is required to handle high memory usage while loading the dataset.

##Performance Metrics
The performance of the model is evaluated using the following metrics:
Accuracy
F1 Score
Precision
Recall
AUC-ROC Score
Deep Learning Neurons
The CNN architecture used in the project includes:

Sequential Model
Convolutional Layers (Conv2D)
Activation Functions (ReLU)
Max Pooling Layers (MaxPool2D)
Flatten Layer
Dense Layers
Model Training
The model training process involves:

Preprocessing the dataset using data augmentation techniques.
Designing the CNN architecture.
Compiling the model with the Adam optimizer and accuracy metric.
Saving model checkpoints and employing EarlyStopping.
Visualizing training and validation metrics.
Saving the trained model in .h5 and protobuf formats.
Model Testing
Model testing involves:

Loading the trained model.
Predicting classes for the test dataset.
Plotting confusion matrices.
Generating a metrics report.
Deployment
The system is deployed using Flask for hosting the API and Ngrok for exposing the API endpoint. Additionally, a Kivy app serves as the frontend for requesting classification labels of images.

File Structure
MyDrive: Contains training logs and trained Keras models.
Graphs&tables: Contains images of graphs and tables visualized during training and observations.
Python-files: Contains flask_server.py and main.py, which are the Flask server and Kivy app Python files, respectively.
Conclusion
The capstone project successfully developed a fire detection system integrating a Keras model, Flask API, and Kivy frontend. Key achievements include model development, app development, API deployment, and component integration. Future directions include enhancing model performance, refining the user interface, optimizing deployment, and integrating with surveillance systems.

Resources
GitHub Repository
Dataset Download
For detailed instructions on setting up and running the system, please refer to the project documentation and code within the repository.
