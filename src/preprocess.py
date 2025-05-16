# Script to preprocess data for sentiment analysis
import re
import pandas as pd
from pymongo import MongoClient
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords

# MongoDB configuration
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "cs_sentiment"
RAW_COLLECTION = "feedback"
PROCESSED_COLLECTION = "processed_feedback"

# Text cleaning function
def clean_text(text):
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove non-alphanumeric characters
    text = text.lower()  # Convert to lowercase
    text = " ".join([word for word in text.split() if word not in stopwords.words("english")])  # Remove stopwords
    return text

def preprocess_data():
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]

    # Fetch raw data
    raw_data = list(db[RAW_COLLECTION].find())
    print(f"Fetched {len(raw_data)} raw entries.")

    # Process data
    processed_data = []
    for entry in raw_data:
        if "feedback" in entry:
            processed_entry = {
                "subject_name": entry["subject_name"],
                "cleaned_feedback": clean_text(entry["feedback"]),
                "sentiment": entry["sentiment"],
                "user_id": entry["user_id"],
                "date": entry["date"],
            }
            processed_data.append(processed_entry)

    # Insert processed data
    db[PROCESSED_COLLECTION].insert_many(processed_data)
    print(f"Inserted {len(processed_data)} processed entries into MongoDB.")
    processed_df = pd.DataFrame(processed_data)
    processed_df.to_csv("data/processed/processed_feedback.csv", index=False)
    print("Processed data saved to data/processed/processed_feedback.csv")

if __name__ == "__main__":
    preprocess_data()
