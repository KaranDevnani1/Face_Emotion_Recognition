# Facial Emotion Detection

## 📌 Overview
This project detects facial emotions in real-time using a pre-trained deep learning model. The model is trained using `trainmodel.ipynb` and can be used for live emotion recognition through `realtimedetection.py`.

## ✨ Features
- Detects emotions from real-time webcam input
- Pre-trained deep learning model for emotion classification
- Seven emotion categories: `Angry`, `Disgust`, `Fear`, `Happy`, `Neutral`, `Sad`, `Surprise`

## 🛠 Installation

1. **Clone the repository:**  
   ```bash
   git clone <your-repo-link>
   cd <your-repo-folder>
   ```

2. **Install dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure the following files are present:**  
   - `Emotiondetection.json` (Model architecture)  
   - `Emotiondetection.h5` (Pre-trained model weights)

## 🏋️ Training the Model
To train the model, open and run the `trainmodel.ipynb` notebook. This will train the model on the dataset and generate the necessary `.json` and `.h5` files.

## 🚀 Running Real-Time Emotion Detection
Execute the following command to start real-time emotion detection:
```bash
python realtimedetection.py
```
This will open the webcam and display real-time emotion predictions. Press `ESC` to exit.

## 📦 Dependencies
Ensure you have the following installed:
- Python 3.x  
- OpenCV  
- TensorFlow/Keras  
- NumPy  

To install them manually:
```bash
pip install opencv-python tensorflow numpy
```

## 📊 Output
The program will display a video feed with detected faces and predicted emotions labeled on the screen.

## 🔧 Troubleshooting
- If the model fails to load, ensure `Emotiondetection.json` and `Emotiondetection.h5` are correctly generated and present in the project directory.
- If the webcam doesn't start, check that your camera is working and accessible.

## 📜 License
This project is for educational purposes. Feel free to modify and use it as needed.

