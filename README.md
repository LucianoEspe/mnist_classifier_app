# Gradio MNIST Classifier App

This project is a simple application built using Gradio, a Python library for creating customizable UI components around machine learning models. The application allows users to interactively test classification models on the popular MNIST dataset, which consists of handwritten digit images.

## Features:

- **Interactive Testing**: Users can draw on the canvas to test the pre-trained or self-made classification models.
- **Multiple Models**: The application comes pre-loaded with two classification models trained on the MNIST dataset, providing users with options to compare model performance.
- **Ease of Use**: With a user-friendly interface provided by Gradio, users can easily understand and interact with the classification models without any prior coding knowledge.

## Usage:

1. Clone the repository to your local machine.
2. Install the necessary dependencies using `pip install -r requirements.txt`.
3. Run the `app.py` script to start the application.
4. Access the application through your web browser at the provided URL.

## Models Included:

1. **Simple Dense Model**: This model consists of a single dense layer with 10 output nodes, each representing a digit class. It provides a basic approach to digit classification. Accuracy: 41.71%.

2. **Multi-layer Perceptron (MLP) Model**: This model incorporates multiple hidden layers with ReLU activation functions for added complexity. The additional hidden layers allow for more intricate feature extraction, potentially improving classification accuracy. Accuracy: 97.35%.

## Model Recommendations:

Please note that the models included in this project are trained using dense layers, which may not be ideal for certain tasks such as digit recognition. Models trained solely with dense layers lack flexibility in detecting numbers across various positions or sizes, potentially impacting their performance. For more accurate and robust digit recognition, it is recommended to use models trained with convolutional neural networks (CNNs). However, these models are provided here for educational and demonstration purposes. Users are encouraged to explore and experiment with different model architectures for their specific use cases.

## Requirements:

- Python 3.11
- Gradio 3.50.2
- Tensorflow-cpu