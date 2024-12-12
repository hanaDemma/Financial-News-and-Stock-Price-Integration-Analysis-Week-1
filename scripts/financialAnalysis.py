import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from textblob import TextBlob


def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

