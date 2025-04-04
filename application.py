# """
# Emotion Detection Web App using Flask and Watson NLP.
# This application detects emotions from a given text input
# and returns the dominant emotion along with emotion scores.
# """

# from flask import Flask, request, render_template, jsonify
# from EmotionDetection.emotion_detection import emotion_detector
# from flask import Flask, request, jsonify
# import os
# from ibm_watson import NaturalLanguageUnderstandingV1
# from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# # Initialize Flask app
# app = Flask(__name__)
# # Set up IBM Watson NLU
# api_key = os.getenv("WATSON_API_KEY")
# url = os.getenv("WATSON_URL")

# authenticator = IAMAuthenticator(api_key)
# natural_language_understanding = NaturalLanguageUnderstandingV1(
#     version='2021-08-01',
#     authenticator=authenticator
# )
# natural_language_understanding.set_service_url(url)
# @app.route('/')
# def home():
#     """
#     Renders the home page.
    
#     Returns:
#         HTML page: The home page template.
#     """
#     return render_template('index.html')  # Ensure this template exists

# @app.route('/emotionDetector', methods=['GET'])
# def detect_emotion():
#     """
#     Endpoint to detect emotion from a given text.
    
#     Returns:
#         JSON response: Contains emotion scores and the dominant emotion.
#     """
#     # Get the text from the URL query parameter
#     text_to_analyze = request.args.get('textToAnalyze')

#     if not text_to_analyze:
#         return jsonify({"message": "Invalid text! Please try again!"}), 400

#     # Get the emotion analysis result
#     response = emotion_detector(text_to_analyze)

#     # Extract the emotions and their scores from the response (default to 0 if None)
#     anger = response.get("anger", 0)
#     disgust = response.get("disgust", 0)
#     fear = response.get("fear", 0)
#     joy = response.get("joy", 0)
#     sadness = response.get("sadness", 0)
#     dominant_emotion = response.get("dominant_emotion", "none")

#     # Handle case when dominant_emotion is None
#     if dominant_emotion == "none":
#         return jsonify({"message": "Invalid text! Please try again!"})

#     # Format the response as a readable message
#     formatted_response = (
#         f"For the given statement, the system response is 'anger': {anger}, "
#         f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, "
#         f"and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
#     )

#     return jsonify({"message": formatted_response})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080, debug=True)
#     # app.run(host='0.0.0.0', port=5000, debug=True)  # Use 'app.run' here
"""
Emotion Detection Web App using Flask and Watson NLP.
This application detects emotions from a given text input
and returns the dominant emotion along with emotion scores.
"""

from flask import Flask, request, render_template, jsonify
import os
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Initialize Flask app
app = Flask(__name__)

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("WATSON_API_KEY")
url = os.getenv("WATSON_URL")

authenticator = IAMAuthenticator(api_key)
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2021-08-01',
    authenticator=authenticator
)
natural_language_understanding.set_service_url(url)

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

        emotions = response['emotion']['document']['emotion']
        dominant_emotion = max(emotions, key=emotions.get)

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

@app.route('/')
def home():
    """
    Renders the home page.
    
    Returns:
        HTML page: The home page template.
    """
    return render_template('index.html')  # Ensure this template exists

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """
    Endpoint to detect emotion from a given text.
    
    Returns:
        JSON response: Contains emotion scores and the dominant emotion.
    """
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

    formatted_response = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, "
        f"and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

    return jsonify({"message": formatted_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 8080)), debug=True)

    # app.run(host='0.0.0.0', port=8080, debug=True)
