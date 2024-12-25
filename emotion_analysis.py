from transformers import pipeline

# Load the emotion analysis model
emotion_classifier = pipeline('sentiment-analysis', model='j-hartmann/emotion-english-distilroberta-base')

# Map model emotions to your predefined emotion categories
emotion_mapping = {
    "joy": "happy",
    "sadness": "sad",
    "anger": "angry",
    "fear": "sad",  # Map fear to sad
    "surprise": "happy",  # Map surprise to happy
    "love": "happy",  # Map love to happy
    "Exited": "Happy",
    "neutral": "bored",  # Map neutral to bored
    "bore": "bored",
    "disintrested": "bored"
}


def detect_emotion(user_input):
    result = emotion_classifier(user_input)[0]
    detected_emotion = result['label'].lower()  # Get the predicted emotion (e.g., "joy", "sadness")

    # Map the detected emotion to predefined categories
    mapped_emotion = emotion_mapping.get(detected_emotion, "happy")  # Default to "happy" if not mapped

    return mapped_emotion
