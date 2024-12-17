import pandas as pd

def calculate_daily_returns(aligned_data):
    """
    Calculate daily stock returns based on the 'Close' prices in the DataFrame.

    Parameters:
    - aligned_data: DataFrame, the data containing 'Close' prices and 'date'

    Returns:
    - aligned_data: DataFrame, the original DataFrame with an added 'daily_return' column
    """
    # Calculate daily stock returns
    aligned_data['daily_return'] = aligned_data['Close'].pct_change()

    # Drop the first row with NaN values due to pct_change()
    aligned_data = aligned_data.dropna()

    return aligned_data

def calculate_daily_sentiment_and_merge(aligned_data):
    """
    Calculate the daily mean sentiment score and merge it with daily returns.

    Parameters:
    - aligned_data: DataFrame, the data containing 'date', 'sentiment', and 'daily_return' columns

    Returns:
    - final_data: DataFrame, the final dataset with 'date', 'sentiment', and 'daily_return' columns
    """
    # Group by date and calculate the mean sentiment score
    daily_sentiment = aligned_data.groupby('date')['sentiment'].mean().reset_index()

    # Merge with daily returns
    final_data = pd.merge(daily_sentiment, aligned_data[['date', 'daily_return']], on='date')

    return final_data
