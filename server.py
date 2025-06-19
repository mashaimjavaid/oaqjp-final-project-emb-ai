"""
Flask server for emotion detection web application.
Receives text input and returns predicted emotions using IBM Watson API.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the index page with the emotion detection input form."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detection():
    """
    Handles emotion detection request from the client.

    Returns:
        str: A message with emotion scores or error if input is invalid.
    """
    if request.method == 'POST':
        text_to_analyze = request.form['text']
    else:
        text_to_analyze = request.args.get('textToAnalyze')

    result = emotion_detector(text_to_analyze)

    if not result or result.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )
    return response

if __name__ == '__main__':
    app.run(debug=True)
