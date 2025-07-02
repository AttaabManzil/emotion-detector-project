"""
Flask application for emotion detection using Watson NLP API.
This module provides a web interface for analyzing emotions in text.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")


@app.route('/emotionDetector')
def emotion_analysis():
    """
    Analyze emotions in the provided text.
    
    Returns:
        str: Formatted emotion analysis results or error message
    """
    text_to_analyse = request.args.get('textToAnalyze')

    if not text_to_analyse:
        return "Invalid text"

    response = emotion_detector(text_to_analyse)

    if response.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return (f"For the given statement, the system response is "
            f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
            f"'joy': {joy} and 'sadness': {sadness}. "
            f"The dominant emotion is {dominant_emotion}.")


@app.route('/')
def render_index_page():
    """
    Render the main index page.
    
    Returns:
        str: Rendered HTML template
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)