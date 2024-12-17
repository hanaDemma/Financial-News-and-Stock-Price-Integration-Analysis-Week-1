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
3.	Install Dependencies Make sure you have Python 3.8+ installed. Then install required libraries: pip install pandas, numpy, matplotlib, seaborn, TextBlob and TA-Lib
4.	Download and prepare the data:
 Place Input dataset  'Data/' in the project directory.
# Step 2: Data Cleaning and Preparation:
At this stage, the news data was cleaned and pre-processed to remove noise, inconsistencies, and irrelevant information such as missing values. The stock price data was subsequently loaded into Pandas DataFrame for easy processing and analysis.
# Step 3: Sentiment Analysis:
Sentiment analysis of news headlines was conducted using TextBlob by calculating sentiment scores for each article, which reflect the overall emotional tone of the headline (positive, negative, or neutral).
# Step 4: Technical Analysis:
In this step, trends, patterns and potential trading signals of the input data were analyzed by applying various technical indicators (e.g. RSI – Relative Strength Index, SMA – Simple Moving Average, EMA – Exponential Moving Average, MACD – Moving Average Convergence/Divergence) to the stock price data and making buy/sell decisions based on the historical stock price data.
# Step 5: Correlation Analysis:
In this step, sentiment score aggregation by date was performed by matching each sentiment score with its corresponding publication date. Next, the correlation between the aggregated sentiment scores and daily stock returns was calculated to assess whether positive or negative sentiment correlated with price movements. 



## KEY Libraries Used
- **Python:** The programming language used for scripting and data analysis.
- **Pandas:** Used for data manipulation and analysis.
- **TextBlob:** For natural language processing (NLP).Extracts sentiment scores from news headlines.
- **TA-Lib:** for calculating technical indicator
- **yfinance:** Used for calculating technical indicators (e.g., Moving Averages, RSI, etc.) to analyze stock trends.
- **Matplotlib or Seaborn:** Libraries for data visualization.
Used to plot scatter plots, heatmaps, and other graphical insights.

# Contact
For any questions, contact:
Name: Hana Demma
Email: hana.demma@gmail.com

**Contributing**
Feel free to fork this repository, make improvements, and submit a pull request. Contributions are welcome!