from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
import json

app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def emotion_analysis():
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    dominant_response = response['dominant_emotion']
    formatted_output = (
         f"For the given statement, the system response is {response}. "
         f"The dominant emotion is {dominant_response}"
    )
    return formatted_output


@app.route('/')
def index_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
