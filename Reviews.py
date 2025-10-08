# Fake Review Detection Project - Flipkart (Python)
# Created for College Project Demonstration
# ---------------------------------------------------

import re
import joblib
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from nltk.corpus import stopwords

# Download stopwords (only first time)
nltk.download('stopwords')

# ---------------------------------------------------
# 1. TRAINING THE MODEL
# ---------------------------------------------------

def train_model():
    # Example training data
    # 1 = real review, 0 = fake review
    reviews = [
        "The battery backup is very good, lasts for 2 days easily",  # real
        "Camera quality is nice and worth the price",                # real
        "Very poor performance, not recommended",                    # real
        "Amazing product must buy super cool awesome",               # fake
        "Best best best product love it amazing awesome",            # fake
        "Excellent nice super quality perfect great",                # fake
        "Display is sharp and bright, very happy with the product",  # real
        "Worst item ever, waste of money",                           # real
    ]
    labels = [1, 1, 1, 0, 0, 0, 1, 1]

    vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'))
    X = vectorizer.fit_transform(reviews)

    model = LogisticRegression()
    model.fit(X, labels)

    # Save model for later use
    joblib.dump((model, vectorizer), "review_model.pkl")
    print("✅ Model trained and saved successfully.\n")


# ---------------------------------------------------
# 2. LOAD MODEL
# ---------------------------------------------------
def load_model():
    return joblib.load("review_model.pkl")


# ---------------------------------------------------
# 3. REVIEW ANALYSIS FUNCTION
# ---------------------------------------------------
def analyze_reviews(reviews):
    model, vectorizer = load_model()
    X = vectorizer.transform(reviews)
    predictions = model.predict(X)

    print("🔍 Review Analysis Result:\n")
    for r, p in zip(reviews, predictions):
        label = "✅ Real Review" if p == 1 else "⚠️ Fake Review"
        print(f"Review: {r}\n→ {label}\n")


# ---------------------------------------------------
# 4. DEMO / USER INPUT
# ---------------------------------------------------
if __name__ == "__main__":
    try:
        load_model()
        print("📁 Loaded existing model.\n")
    except:
        print("⚙️ Training model for the first time...\n")
        train_model()

    # Example input: you can replace this with scraped data
    user_reviews = [
        "Excellent product very good quality best price awesome love it",
        "Battery performance is average but display is nice",
        "Great product value for money",
        "Superb awesome great wow nice product",
    ]

    analyze_reviews(user_reviews)
