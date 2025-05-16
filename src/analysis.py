# Script for performing sentiment analysis
from pymongo import MongoClient
import textblob
from textblob import TextBlob
import pandas as pd

# MongoDB configuration
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "cs_sentiment"
PROCESSED_COLLECTION = "processed_feedback"
ANALYZED_COLLECTION = "analyzed_feedback"

def analyze_sentiments():
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]

    # Fetch preprocessed data
    processed_data = list(db[PROCESSED_COLLECTION].find())
    print(f"Fetched {len(processed_data)} entries for sentiment analysis.")

    analyzed_data = []
    for entry in processed_data:
        feedback = entry["cleaned_feedback"]
        blob = TextBlob(feedback)
        polarity = blob.sentiment.polarity

        # Classify sentiment based on polarity
        if polarity > 0:
            sentiment_label = "positive"
        elif polarity == 0:
            sentiment_label = "neutral"
        else:
            sentiment_label = "negative"

        analyzed_entry = {
            "subject_name": entry["subject_name"],
            "feedback": entry["cleaned_feedback"],
            "original_sentiment": entry["sentiment"],  # Original label for comparison
            "analyzed_sentiment": sentiment_label,
            "polarity": polarity,
            "user_id": entry["user_id"],
            "date": entry["date"],
        }
        analyzed_data.append(analyzed_entry)

    # Save analyzed data
    db[ANALYZED_COLLECTION].insert_many(analyzed_data)
    print(f"Inserted {len(analyzed_data)} analyzed entries into MongoDB.")
    analyzed_df = pd.DataFrame(analyzed_data)
    analyzed_df.to_csv("data/processed/analyzed_feedback.csv", index=False)
    print("Analyzed data saved to data/processed/analyzed_feedback.csv")
    

if __name__ == "__main__":
    analyze_sentiments()
