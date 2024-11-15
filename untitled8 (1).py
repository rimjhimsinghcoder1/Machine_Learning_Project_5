# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nTma4Rd5Nh7iQ-xn067lsD5SZ3VN6wGc
"""

import pandas as pd
import numpy as np
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Sample dataset: SMS Spam Collection (Indianized content)
data = {
    'text': [
        'Congratulations! You have won a ₹10,000 Amazon gift voucher. Text WIN to claim your prize now!',
        'Reminder: Your appointment at the local salon is at 3 PM today. Don’t forget!',
        'Free entry to win 1000s of prizes! Text PRIZE to 56789 to try your luck.',
        'Hey! How are you? Can we meet at the local shop tomorrow evening?',
        'Get a free smartphone with no-cost EMI! Click here to claim your offer today.',
        'The meeting is rescheduled to 2 PM tomorrow at the office. Please be on time.'
    ],
    'label': ['spam', 'ham', 'spam', 'ham', 'spam', 'ham']
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Preprocess the text data
def preprocess_text(text):
    # Remove any non-alphanumeric characters (keeping spaces)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # Convert to lower case
    text = text.lower()
    return text

df['text'] = df['text'].apply(preprocess_text)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.33, random_state=42)

# Convert text to numeric using TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=5000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Build and train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test_tfidf)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))

import pandas as pd
import numpy as np
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Sample dataset: SMS Spam Collection (Indianized content)
data = {
    'text': [
        'Congratulations! You have won a ₹10,000 Amazon gift voucher. Text WIN to claim your prize now!',
        'Reminder: Your appointment at the local doctor’s clinic is at 3 PM today. Don’t forget!',
        'Free entry to win 1000s of prizes! Text PRIZE to 56789 to try your luck.',
        'Hey! How are you? Can we meet at the local chaiwala tomorrow evening?',
        'Get a free smartphone with no-cost EMI! Click here to claim your offer today.',
        'The meeting is rescheduled to 2 PM tomorrow at the office. Please be on time.'
    ],
    'label': ['spam', 'ham', 'spam', 'ham', 'spam', 'ham']
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Preprocess the text data
def preprocess_text(text):
    # Remove any non-alphanumeric characters (keeping spaces)
    text = re.sub(r'[^a-zA0-9\s]', '', text)
    # Convert to lower case
    text = text.lower()
    return text

df['text'] = df['text'].apply(preprocess_text)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.33, random_state=42)

# Convert text to numeric using TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=5000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Build and train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test_tfidf)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Additional print statements for test samples, true labels, and predicted labels
print("\nTest Samples with True Labels and Predictions:")
for text, true_label, pred_label in zip(X_test, y_test, y_pred):
    print(f"Text: {text}")
    print(f"True Label: {true_label}, Predicted Label: {pred_label}")
    print('-' * 80)



