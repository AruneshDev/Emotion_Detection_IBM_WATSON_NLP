import requests
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def emotion_detector(text_to_analyze):
    if not text_to_analyze:
        return {
            'anger': 0.0,
            'disgust': 0.0,
            'fear': 0.0,
            'joy': 0.0,
            'sadness': 0.0,
            'dominant_emotion': 'none'
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myjob = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, json=myjob, headers=headers, timeout=10)

        # Check if the response was successful
        if response.status_code != 200:
            logging.error(f"Error with status code {response.status_code}")
            return {
                'anger': 0.0,
                'disgust': 0.0,
                'fear': 0.0,
                'joy': 0.0,
                'sadness': 0.0,
                'dominant_emotion': 'none'
            }

        # Log the response
        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Text: {response.text}")

        # Convert response text to dictionary
        response_dict = json.loads(response.text)

        # Extract emotions and their scores
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

    except requests.exceptions.RequestException as e:
        logging.error(f"Network error: {str(e)}")
        return {
            'anger': 0.0,
            'disgust': 0.0,
            'fear': 0.0,
            'joy': 0.0,
            'sadness': 0.0,
            'dominant_emotion': 'none'
        }

    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {
            'anger': 0.0,
            'disgust': 0.0,
            'fear': 0.0,
            'joy': 0.0,
            'sadness': 0.0,
            'dominant_emotion': 'none'
        }
