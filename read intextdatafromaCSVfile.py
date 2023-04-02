# Python code to perform sentiment analysis on text data

import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Read in the data
data = pd.read_csv('text_data.csv')

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Calculate sentiment scores for each row of text
sentiment_scores = data['text'].apply(lambda x: sia.polarity_scores(x))

# Extract the compound score from each sentiment dictionary
compound_scores = sentiment_scores.apply(lambda x: x['compound'])

# Add the compound score to the data as a new column
data['compound_score'] = compound_scores

# Calculate the average compound score for each category
category_scores = data.groupby('category')['compound_score'].mean()

# Print the category scores
print(category_scores)
