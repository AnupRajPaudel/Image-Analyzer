# Image Analysis Web App

This is a Flask-based web application that allows users to upload images, analyze them using the Google Cloud Vision API, and display descriptive labels for the uploaded images.

## Features
- Upload images via a user-friendly web interface.
- Analyze images using the Google Cloud Vision API.
- Display descriptive labels based on the image content.

## Prerequisites
- Python 3.7 or higher
- Google Cloud Vision API enabled
- A valid API key for Google Cloud Vision API

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
2. **Create a Virtual Environment**
   - Use the following command to create a virtual environment:
     ```bash
     python3 -m venv venv
     ```
   - Activate the virtual environment:
     ```bash
     source venv/bin/activate
     ```
   - You should see `(venv)` at the beginning of your terminal prompt, indicating the environment is active.
3. **Install Dependencies**
   - Install the required Python packages:
     ```bash
     pip install -r requirements.txt
     ```
4. **Set Up API Key**
   - Enable the [Google Cloud Vision API](https://console.developers.google.com/apis/api/vision.googleapis.com/overview).
   - Open the `app.py` file in a text editor.
   - Replace the `GEMINI_API_KEY` value with your valid API key.

5. **Run the Application**
   - Start the Flask application:
     ```bash
     python app.py
     ```

6. **Access the Application**
   - Open your browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000).
   - Upload an image in JPEG or PNG format to analyze.

7. **View Results**
   - After uploading an image, the app will display descriptive labels based on the image content.
