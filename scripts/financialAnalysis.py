import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from textblob import TextBlob


def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

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

def getSentimentAnalysisOfPublisher(news_data, target_publisher):
        colors = {'positive': 'green', 'negative': 'red', 'neutral': 'blue'}
    # Filter data for the target publisher
        publisher_data = news_data[news_data['publisher'] == target_publisher]
        sentiment_counts = publisher_data['sentiment_score_word'].value_counts().sort_index()

        sentiment_counts.plot(kind="bar", figsize=(10, 4), title=f'Sentiment Analysis of {target_publisher}',
                      xlabel='Sentiment categories', ylabel='Number of Published Articles',
                      color=[colors[category] for category in sentiment_counts.index])
        



def checkMissingValueOfHistoricalDataset(data_aapl,data_amzn,data_goog,data_meta,data_msft,data_nvda,data_tsla):
    combined_df = pd.concat([data_aapl.isnull().sum(),
                             data_goog.isnull().sum(),
                             data_amzn.isnull().sum(),
                             data_msft.isnull().sum(),
                             data_meta.isnull().sum(),
                             data_nvda.isnull().sum(),
                            data_tsla.isnull().sum()],
                            axis=0)
    combined_df.head()

def calculateDescriptiveStatisticsOfHistoricalData(data_aapl,data_amzn,data_goog,data_meta,data_msft,data_nvda,data_tsla):
    aapl_stats = data_aapl['Close'].describe().to_frame('AAPL')
    goog_stats = data_goog['Close'].describe().to_frame('GOOG')
    amzn_stats = data_amzn['Close'].describe().to_frame('AMZN')
    msft_stats = data_msft['Close'].describe().to_frame('MSFT')
    meta_stats = data_meta['Close'].describe().to_frame('META')
    nvda_stats = data_nvda['Close'].describe().to_frame('NVDA')
    tsla_stats = data_tsla['Close'].describe().to_frame('TSLA')
    combined_stats = pd.concat([aapl_stats, goog_stats,amzn_stats,msft_stats,meta_stats,nvda_stats,tsla_stats], axis=1)
    return combined_stats

 

