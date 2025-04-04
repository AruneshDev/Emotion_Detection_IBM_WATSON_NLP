from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import os
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Load environment variables from .env file
load_dotenv()

# Fetch API key and URL for IBM Watson NLP from environment variables
api_key = os.getenv("WATSON_API_KEY")
url = os.getenv("WATSON_URL")

# Authenticate with IBM Watson API
authenticator = IAMAuthenticator(api_key)
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2021-08-01',
    authenticator=authenticator
)
natural_language_understanding.set_service_url(url)

# Function to detect emotions from the text using Watson NLP
def emotion_detector(text_to_analyze):
    """
    Calls IBM Watson NLU to detect emotions.
    
    Args:
        text_to_analyze (str): The text to be analyzed.
    
    Returns:
        dict: A dictionary with emotion scores and the dominant emotion.
    """
    try:
        response = natural_language_understanding.analyze(
            text=text_to_analyze,
            features=Features(emotion=EmotionOptions())
        ).get_result()

        # Extract emotions from Watson's response
        emotions = response['emotion']['document']['emotion']
        dominant_emotion = max(emotions, key=emotions.get)

        # Return the emotions and the dominant emotion
        return {
            "anger": emotions.get("anger", 0),
            "disgust": emotions.get("disgust", 0),
            "fear": emotions.get("fear", 0),
            "joy": emotions.get("joy", 0),
            "sadness": emotions.get("sadness", 0),
            "dominant_emotion": dominant_emotion
        }
    except Exception as e:
        return {"error": str(e)}

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """
    Endpoint to detect emotion from a given text.
    
    Returns:
        JSON response: Contains emotion scores and the dominant emotion.
    """
    # Get the text from the URL query parameter
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    # Get the emotion analysis result
    response = emotion_detector(text_to_analyze)

    if "error" in response:
        return jsonify({"message": "Error during analysis: " + response["error"]}), 500

    # Extract the emotions and their scores
    anger = response.get("anger", 0)
    disgust = response.get("disgust", 0)
    fear = response.get("fear", 0)
    joy = response.get("joy", 0)
    sadness = response.get("sadness", 0)
    dominant_emotion = response.get("dominant_emotion", "none")

    # Prepare the response in the new format
    formatted_response = (
        f"The dominant emotion is: {dominant_emotion}\n"
        f"The scores for all emotions are:\n"
        f"Sadness: {sadness}\n"
        f"Joy: {joy}\n"
        f"Fear: {fear}\n"
        f"Disgust: {disgust}\n"
        f"Anger: {anger}\n"
    )

    return jsonify({"message": formatted_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 8080)), debug=True)
