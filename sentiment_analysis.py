import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the VADER lexicon
nltk.download('vader_lexicon')

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text):  # Fixed typo in method name
        scores = self.analyzer.polarity_scores(text)
        if scores['compound'] > 0.05:
            return "Positive"
        elif scores['compound'] < -0.05:
            return "Negative"
        else:
            return "Neutral"
