# Script to generate and insert random data into MongoDB
import random
import datetime
from pymongo import MongoClient

# MongoDB configuration
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "cs_sentiment"
COLLECTION_NAME = "feedback"

# Data options
subjects = ["Artificial Intelligence", "Machine Learning", "DBMS", "Data Structures", "Computer Networks"]
positive_feedback = ["This is an amazing subject!", "I love learning about this.", "Very interesting and engaging!"]
neutral_feedback = ["This subject is okay.", "Not too bad, not too great.", "I feel indifferent about this."]
negative_feedback = ["I don't like this subject.", "It's too difficult.", "Not engaging at all."]
sentiments = ["positive", "neutral", "negative"]

# Function to generate feedback based on sentiment
def generate_feedback(sentiment):
    if sentiment == "positive":
        return random.choice(positive_feedback)
    elif sentiment == "neutral":
        return random.choice(neutral_feedback)
    elif sentiment == "negative":
        return random.choice(negative_feedback)

# Function to generate random dates
def random_date(start, end):
    start_date = datetime.datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end, "%Y-%m-%d")
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return (start_date + datetime.timedelta(days=random_days)).strftime("%Y-%m-%d")

# Function to generate random data
def generate_data(num_entries=200):
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]

    data = []
    for _ in range(num_entries):
        subject = random.choice(subjects)
        sentiment = random.choice(sentiments)
        feedback = generate_feedback(sentiment)
        user_id = f"user{random.randint(100, 999)}"
        date = random_date("2023-01-01", "2024-11-18")
        
        document = {
            "subject_name": subject,
            "feedback": feedback,
            "sentiment": sentiment,
            "user_id": user_id,
            "date": date
        }
        data.append(document)
    
    # Insert into MongoDB
    collection.insert_many(data)
    print(f"{num_entries} random entries inserted into MongoDB!")

# Run the function
if __name__ == "__main__":
    generate_data()
    