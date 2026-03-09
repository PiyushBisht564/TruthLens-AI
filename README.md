TruthLens-AI 🧠🔍

AI-Powered Fake Image Detection System

TruthLens-AI is a deep learning–based web application that detects whether an image is Real or Fake using a trained AI model. The system provides instant predictions along with confidence scores through a clean and simple web interface.

🚀 Features

📤 Upload any image

🤖 AI-based real vs fake classification

📊 Confidence score display

🌐 Clean and responsive web interface

⚡ Fast prediction using optimized model loading

Slide — Technologies Used
Frontend

HTML – Structure of the web pages

CSS – Styling and layout of the website

JavaScript – Handles user interactions and image upload

Backend

Python – Main programming language

Flask – Lightweight web framework used to handle requests and connect frontend with the AI model

AI / Machine Learning

PyTorch – Deep learning framework used to run the trained model

Pretrained Image Classification Model – Used to detect fake or manipulated images

Tools

VS Code – Development environment

GitHub – Version control and project collaboration

📁 Project Structure
TruthLens-AI/
│
├── app.py              # Main Flask application
├── model.py            # Model loading & prediction logic
├── requirements.txt    # Project dependencies
├── .gitignore          # Ignored files
│
├── static/             # CSS, JS, images
├── templates/          # HTML templates
├── testimages/         # Sample images for testing

🧠 How It Works

User uploads an image.

The image is preprocessed using OpenCV.

The trained deep learning model analyzes it.

The model outputs:

Real / Fake classification

Confidence percentage

User Uploads Image
        ↓
Frontend sends request
        ↓
Flask Backend receives image
        ↓
Image Preprocessing
        ↓
AI Model Prediction
        ↓
Result returned to frontend

Future Implementation

Video Deepfake Detection
Extend the system to detect fake or manipulated videos, not just images.

Training on Larger Datasets
Improve model accuracy by training on more diverse and modern AI-generated images.

Real-Time Detection
Implement real-time image analysis for faster results.

Cloud Deployment
Deploy the system on cloud platforms so users can access it online.

Improved User Interface
Enhance the website with better design and user experience.

website : https://huggingface.co/spaces/Piyush871397/TruthLens-AI
model : https://www.kaggle.com/code/dima806deepfake-vs-real-faces-detection-vit

