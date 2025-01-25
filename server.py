''' Emotion Detector to be executed over the Flask channel and
    deployed on localhost:5000.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    ''' Receives the text from the HTML interface and runs
    sentiment analysis over it using emotion_detector()
    The output shows the label, its score and the dominat emotion
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']
    sresponse ="<b>Invalid text! Please try again!.</b>"
    if dominant_emotion is not None:
        sp1 = "For the given statement, the system response is "
        sp2 = f"'anger': {anger_score}, 'disgust': {disgust_score}, "
        sp3 = f"'fear': {fear_score}, 'joy': {joy_score} and "
        sp4 = f"'sadness': {sadness_score}. "
        sp5 = f"The dominant emotion is <b>{dominant_emotion}</b>."
        sresponse = sp1+sp2+sp3+sp4+sp5
    return sresponse

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main app page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
