# Financial-News-and-Stock-Price-Integration-Analysis-Week-1

# Overview
The objective of this project is to analyze financial news data and stock price movements using sentiment analysis, technical analysis and correlation analysis to predict potential trends and trading signals that can be used in developing investment strategies.
The dataset used for this analysis includes financial news data and stock price data for the following companies:
- AAPL (Apple Inc.)
- AMZN (Amazon.com, Inc.)
- GOOG (Alphabet Inc.)
- MSFT (Microsoft Corporation)
- META (Meta Platforms, Inc.)
- TSLA (Tesla Inc.)

The following step-by-step methods were used to achieve the objective.
# Step1: Setup:
Instructions
1.	Clone the Repository git clone  https://github.com/hanaDemma/Financial-News-and-Stock-Price-Integration-Analysis-Week-1.git
2.	Create virtual environment python -m venv venv source venv/bin/activate # For Linux/Mac venv\Scripts\activate # For Windows
3.	Install Dependencies Make sure you have Python 3.8+ installed. Then install required libraries: pip install pandas, numpy, matplotlib, seaborn, TextBlob and TA-Lib
4.	Place Input dataset in the project directory.
# Step 2: Data Cleaning and Preparation:
At this stage, the news data was cleaned and pre-processed to remove noise, inconsistencies, and irrelevant information such as missing values. The stock price data was subsequently loaded into Pandas DataFrame for easy processing and analysis.
# Step 3: Sentiment Analysis:
Sentiment analysis of news headlines was conducted using TextBlob by calculating sentiment scores for each article, which reflect the overall emotional tone of the headline (positive, negative, or neutral).
# Step 4: Technical Analysis:
In this step, trends, patterns and potential trading signals of the input data were analyzed by applying various technical indicators (e.g. RSI – Relative Strength Index, SMA – Simple Moving Average, EMA – Exponential Moving Average, MACD – Moving Average Convergence/Divergence) to the stock price data and making buy/sell decisions based on the historical stock price data.
# Step 5: Correlation Analysis:
In this step, sentiment score aggregation by date was performed by matching each sentiment score with its corresponding publication date. Next, the correlation between the aggregated sentiment scores and daily stock returns was calculated to assess whether positive or negative sentiment correlated with price movements. The following libraries and tools were used in this step:
- Python
- Pandas
- TextBlob
- TA-Lib
- Matplotlib or Seaborn
