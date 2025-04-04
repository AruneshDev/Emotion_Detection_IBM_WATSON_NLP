import requests
import json
def emotion_detector(text_to_analyze):
    if not text_to_analyze:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myjob = {"raw_document": {"text": text_to_analyze}}
    try:
        response = requests.post(url, json=myjob, headers=headers)

        # Handle server response error (status code 400)
        if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

        # Convert response text to dictionary
        response_dict = json.loads(response.text)

        # Extract emotions and scores correctly
        emotions = response_dict.get('emotionPredictions', [])[0].get('emotion', {})

        # Initialize emotion scores
        emotion_scores = {
            'anger': emotions.get('anger', 0.0),
            'disgust': emotions.get('disgust', 0.0),
            'fear': emotions.get('fear', 0.0),
            'joy': emotions.get('joy', 0.0),
            'sadness': emotions.get('sadness', 0.0),
        }

        # Find the dominant emotion
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Add the dominant emotion to the result
        emotion_scores['dominant_emotion'] = dominant_emotion

        return emotion_scores

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    