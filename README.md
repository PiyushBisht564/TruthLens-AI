TruthLens-AI 🧠🔍

AI-Powered Fake Image Detection System

TruthLens-AI is a deep learning–based web application that detects whether an image is Real or Fake using a trained AI model. The system provides instant predictions along with confidence scores through a clean and simple web interface.

🚀 Features

📤 Upload any image

🤖 AI-based real vs fake classification

📊 Confidence score display

🌐 Clean and responsive web interface

⚡ Fast prediction using optimized model loading

🛠️ Tech Stack

Python

Flask

PyTorch

timm

OpenCV

HTML / CSS

JavaScript

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
