import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from textblob import TextBlob

def numberOfArticlesWithSentimentAnalysis(news_data):
    # Check for missing values or invalid categories
    if 'sentiment_score_word' not in news_data.columns:
        print("Error: 'sentiment_score_word' column not found.")
        return
    
    # Handle missing values
    news_data = news_data.dropna(subset=['sentiment_score_word'])

    # Count sentiment categories
    sentiment_counts = news_data['sentiment_score_word'].value_counts().sort_index()

    # Define colors for each category
    colors = {'positive': 'green', 'negative': 'red', 'neutral': 'blue'}

    # Create the bar plot with specified colors
    sentiment_counts.plot(kind="bar", figsize=(10, 4), title='Sentiment Analysis',
                        xlabel='Sentiment categories', ylabel='Number of Published Articles',
                        color=[colors.get(category, 'gray') for category in sentiment_counts.index])

    # Display the plot
    plt.show()

 