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
# 
FINANCIAL-NEWS-AND-STOCK-PROJECT/ ├── .github/ # GitHub-specific configurations (e.g., workflows) ├── .week-1/ # virtual enviroment ├── Data/ # Directory for raw data files (CSV or JSON) ├── notebooks/ # Jupyter notebooks for exploration and analysis │  ├── newsandStockPrice.ipynb # Notebook for stock and news price exploration │ └── README.md # Notebook-specific documentation ├── scripts/ # Python scripts for data and sentiment analysis │    ├── src/ # Additional source code or reusable modules ├── tests/ # Unit and integration tests ├── .gitignore # Specifies files to be ignored by Git ├── README.md # Project overview and instructions └── requirements.txt # List of Python dependencies
The following step-by-step methods were used to achieve the objective.
# Step1: Setup Instructions:

1.	Clone the Repository git clone  https://github.com/hanaDemma/Financial-News-and-Stock-Price-Integration-Analysis-Week-1.git
2.	Create virtual environment python -m venv venv source venv/bin/activate # For Linux/Mac venv\Scripts\activate # For Windows
3.	Install Dependencies: Ensure you have Python 3.8+ installed. Then, install the required libraries:
     - pip install -r requirements.txt
4.	Download and prepare the data: Place Input dataset  'Data/' in the project directory.
# Step 2: Data Cleaning and Preparation:
Financial news data is cleaned to remove noise and inconsistencies (e.g., missing values, duplicate entries).
Stock price data is loaded into a Pandas DataFrame for processing and analysis.
# Step 3: Sentiment Analysis:
Sentiment analysis of news headlines was conducted using TextBlob by calculating sentiment scores for each article, which reflect the overall emotional tone of the headline (positive, negative, or neutral).
# Step 4: Technical Analysis:
We apply key technical indicators to stock price data to detect trends and generate trading signals:

- Relative Strength Index (RSI)
- Simple Moving Average (SMA)
- Exponential Moving Average (EMA)
- Moving Average Convergence/Divergence (MACD)
# Step 5: Correlation Analysis:
Sentiment score aggregation by date was performed by matching each sentiment score with its corresponding publication date. Next, the correlation between the aggregated sentiment scores and daily stock returns was calculated to assess whether positive or negative sentiment correlated with price movements. 



## KEY Libraries Used

- **Pandas:** Data manipulation and analysis
- **TextBlob:** For natural language processing (NLP).Extracts sentiment scores from news headlines.
- **TA-Lib:** Technical analysis library for calculating indicators (RSI, SMA, EMA, etc.).
- **yfinance:** Fetches historical stock data for analysis.
- **Matplotlib or Seaborn:** Libraries for data visualization (scatter plots, heatmaps, etc.)


# Visualization
Scatter plots, heatmaps, and other graphical methods are used to explore the relationship between sentiment scores and stock price trends.

# Contact
For any questions, contact:
Name: Hana Demma
Email: hana.demma@gmail.com

**Contributing**
Feel free to fork this repository, make improvements, and submit a pull request. Contributions are welcome!