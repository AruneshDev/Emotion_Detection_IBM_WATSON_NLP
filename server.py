"""
Emotion Detection Web App using Flask and Watson NLP.
This application detects emotions from a given text input
and returns the dominant emotion along with emotion scores.
"""

from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/')
def home():
    """
    Renders the home page.

    Returns:
        HTML page: The home page template.
    """
    return render_template('index.html')

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

    # Extract the emotions and their scores from the response
    anger = response.get("anger", None)
    disgust = response.get("disgust", None)
    fear = response.get("fear", None)
    joy = response.get("joy", None)
    sadness = response.get("sadness", None)
    dominant_emotion = response.get("dominant_emotion", "none")

    # Handle case when dominant_emotion is None
    if dominant_emotion == "none":
        return jsonify({"message": "Invalid text! Please try again!"})

    # Format the response as a readable message
    formatted_response = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, "
        f"and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

    return jsonify({"message": formatted_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
