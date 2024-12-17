import pandas as pd
import pandas as pd

def convert_and_align_dates(news_data, stock_data, date):
    """
    Convert date columns to datetime format and align datasets by dates.

    Parameters:
    news_df (pd.DataFrame): DataFrame containing news data.
    stock_df (pd.DataFrame): DataFrame containing stock price data.
    date_column (str): The name of the date column to be converted and aligned.

    Returns:
    pd.DataFrame: Aligned DataFrame based on the date column.
    
    """
    
    stock_data = stock_data.rename(columns={'Date': 'date'})
    
    news_data['date'] = pd.to_datetime(news_data['date'], errors='coerce', utc='True')


    # Convert date columns to datetime format, handling potential errors
    news_data['date'] = pd.to_datetime(news_data['date'], format='%Y-%m-%d').dt.date
    stock_data['date'] = pd.to_datetime(stock_data['date'], format='%Y-%m-%d').dt.date


    # Align the datasets by dates
    aligned_df = pd.merge(news_data, stock_data, on='date', how='inner')

    return aligned_df

def load_data(news_path, stock_path):

    # Load the news data
    news_data = pd.read_csv(news_path)

    # Load the stock price data
    stock_data = pd.read_csv(stock_path)

    aligned_data = convert_and_align_dates(news_data, stock_data, 'date')
        
    return aligned_data

# Usage example:
# news_data, stock_data = load_data('../Data/raw_analyst_ratings.csv', '../Data/AAPL_historical_data.csv')
