from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    # Get the text from the URL query parameter
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return jsonify({"message": "No text provided for emotion analysis"}), 400

    # Get the emotion analysis result
    response = emotion_detector(text_to_analyze)

    # Extract the emotions and their scores from the response
    anger = response.get("anger", 0.0)
    disgust = response.get("disgust", 0.0)
    fear = response.get("fear", 0.0)
    joy = response.get("joy", 0.0)
    sadness = response.get("sadness", 0.0)
    dominant_emotion = response.get("dominant_emotion", "none")

    # Format the response as a readable message
    formatted_response = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, "
        f"and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

    return jsonify({"message": formatted_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
