import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pymongo import MongoClient
import os

# MongoDB configuration
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "cs_sentiment"
ANALYZED_COLLECTION = "analyzed_feedback"

# Ensure the output directory exists
output_dir = "outputs/graphs"
os.makedirs(output_dir, exist_ok=True)

# Fetch data from MongoDB
def fetch_data():
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    analyzed_data = list(db[ANALYZED_COLLECTION].find())
    return pd.DataFrame(analyzed_data)

# Plot sentiment distribution
def plot_sentiment_distribution(df):
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x="analyzed_sentiment", hue="analyzed_sentiment", palette="viridis", dodge=False)
    plt.title("Sentiment Distribution", fontsize=16)
    plt.xlabel("Sentiment", fontsize=12)
    plt.ylabel("Count", fontsize=12)
    plt.savefig(f"{output_dir}/sentiment_distribution.png")
    plt.show()



# Plot sentiments over time
def plot_sentiments_over_time(df):
    df["date"] = pd.to_datetime(df["date"])
    time_data = df.groupby(["date", "analyzed_sentiment"]).size().reset_index(name="count")
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=time_data, x="date", y="count", hue="analyzed_sentiment", palette="viridis")
    plt.title("Sentiments Over Time", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Count", fontsize=12)
    plt.savefig(f"{output_dir}/sentiments_over_time.png")
    plt.show()

# Plot sentiment by subject
def plot_sentiments_by_subject(df):
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x="subject_name", hue="analyzed_sentiment", palette="viridis")
    plt.title("Sentiment Distribution by Subject", fontsize=16)
    plt.xlabel("Subject", fontsize=12)
    plt.ylabel("Count", fontsize=12)
    plt.xticks(rotation=45)
    plt.savefig(f"{output_dir}/sentiments_by_subject.png")
    plt.show()

def create_visualizations():
    data = fetch_data()
    print("Generating sentiment distribution plot...")
    plot_sentiment_distribution(data)

    print("Generating sentiments over time plot...")
    plot_sentiments_over_time(data)

    print("Generating sentiments by subject plot...")
    plot_sentiments_by_subject(data)

    print("Visualizations created and saved successfully!")


if __name__ == "__main__":
    data = fetch_data()
    print("Data fetched successfully!")
    
    plot_sentiment_distribution(data)
    plot_sentiments_over_time(data)
    plot_sentiments_by_subject(data)
