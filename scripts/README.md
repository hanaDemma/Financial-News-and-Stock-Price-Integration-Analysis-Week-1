# Overview
This project integrates financial market data with news sentiment analysis to explore the relationship between market behavior and public sentiment. It leverages Python for data manipulation, analysis, and visualization, combining historical stock data with natural language processing for insights into price movements, sentiment trends, and portfolio performance.
The workflow involves
1. Data Loading 
 Historical stock data and news articles are loaded
2. Sentiment Analysis: News articles' headlines or text are analyzed using TextBlob to extract sentiment polarity scores.
3. Stock Technical Analysis: Popular technical indicators such as SMA, RSI, EMA, and MACD are computed to analyze stock performance over time.
4. Portfolio Optimization: Stock price data is used to calculate portfolio weights, analyze returns, and compare stock indicators.

# Key Functions Overview
1. Data Loading and Sentiment Analysis
# loadHistoricalData(ticker)
Loads historical stock data for a given ticker symbol from a CSV file.

# get_sentiment(text)
Analyzes sentiment of text (news headlines) using TextBlob and returns a polarity score.

# numberOfArticlesWithSentimentAnalysis(news_data)
Analyzes the sentiment distribution of news articles and creates a bar chart showing the count of positive, neutral, and negative sentiments.

# getSentimentAnalysisOfPublisher(news_data, target_publisher)
Analyzes sentiment specifically for a target news publisher and visualizes the results in a bar chart.

2. Data Quality and Descriptive Analysis
# checkMissingValueOfHistoricalDataset(stock_data_aapl, stock_data_amzn, ..., stock_data_tsla)
Checks for missing values in historical datasets for multiple stocks and summarizes the results.

# calculateDescriptiveStatisticsOfHistoricalData(stock_data_aapl, stock_data_amzn, ..., stock_data_tsla)
Computes descriptive statistics (mean, std dev, min, max) for closing prices across multiple stocks and displays them in a tabular format.

3. Time Series and Stock Analysis
# analysisClosingPriceWithDate(stock_data_aapl, stock_data_amzn, ..., stock_data_nvda)
Creates time series plots for closing prices of multiple stocks to observe trends over time.

# calculateTechnicalIndicator(stock_data)
Computes essential technical indicators for a stock, including:

    - Simple Moving Average (SMA)
    - Relative Strength Index (RSI)
    - Exponential Moving Average (EMA)
    - Moving Average Convergence Divergence (MACD)
    - Adds them as new columns to the stock dataset.
- technicalIndicatorsVsClosingPrice(stock_data_aapl, stock_data_amzn, ..., stock_data_nvda, ticker)
Compares stock closing prices with chosen technical indicators over time using line plots.

- closingPriceRelativeStrengthIndex(stock_data_aapl, stock_data_amzn, ..., stock_data_nvda)
Visualizes RSI alongside closing prices, identifying overbought/oversold conditions.
- closingPriceMovingAverageConvergenceDivergence(stock_data_aapl, stock_data_amzn, ..., stock_data_nvda)
Creates time series plots for closing prices with the MACD indicator to analyze price momentum and trends.

4. Portfolio Analysis
- calculatePortfolioWeightAndPerformance()
Optimizes portfolio weights using historical stock returns and analyzes the portfolio's risk and return performance.

# Tools and Libraries Used
- Pandas: Data loading, preprocessing, and analysis.
- TextBlob: Sentiment analysis of textual data.
- TA-Lib: Calculation of technical indicators such as RSI, SMA, EMA, and MACD.
- yfinance: Fetching historical market data for stocks.
- Matplotlib/Seaborn: Data visualization, including time series, bar charts, and scatter plots.