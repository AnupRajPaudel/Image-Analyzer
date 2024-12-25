from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Replace this with the correct Gemini Vision API endpoint
GEMINI_API_URL = "https://vision.googleapis.com/v1/images:annotate"
GEMINI_API_KEY = "AIzaSyAQQHvhgFXkAlmSLdtiY7j4HDuQxoEuh5c"

@app.route("/")
def home():
    return render_template("upload.html")

@app.route("/process", methods=["POST"])
def process_image():
    # Get the uploaded image file
    image = request.files.get("image")
    if not image:
        return "No image uploaded!", 400

    # Convert the image to base64 (required for Google Vision API)
    import base64
    image_content = base64.b64encode(image.read()).decode('utf-8')

    # Prepare the request payload
    payload = {
        "requests": [
            {
                "image": {
                    "content": image_content
                },
                "features": [
                    {
                        "type": "LABEL_DETECTION",  # Use "LABEL_DETECTION" to describe images
                        "maxResults": 10
                    }
                ]
            }
        ]
    }

    # Send the request to Gemini Vision API
    response = requests.post(
        f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
        json=payload
    )

    # Debug: Log the response
    print("Response Status Code:", response.status_code)
    print("Response Content:", response.text)

    # Handle the API response
    if response.status_code == 200:
        # Extract labels from the API response
        labels = response.json().get("responses", [{}])[0].get("labelAnnotations", [])
        description = ", ".join([label["description"] for label in labels])
    else:
        description = f"Failed to analyze the image. Error: {response.text}"

    return render_template("result.html", description=description)

if __name__ == "__main__":
    app.run(debug=True)
