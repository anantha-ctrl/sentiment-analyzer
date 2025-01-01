from flask import Flask, render_template, request
from sentiment_analysis import SentimentAnalyzer

app = Flask(__name__)
analyzer = SentimentAnalyzer()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        user_input = request.form['text']
        sentiment = analyzer.analyze_sentiment(user_input)
        return render_template('result.html', sentiment=sentiment, text=user_input)

if __name__ == "__main__":
    app.run(debug=True)
