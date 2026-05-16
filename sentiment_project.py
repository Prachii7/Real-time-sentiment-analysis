import pandas as pd
import matplotlib.pyplot as plt
# Load dataset
data = pd.read_csv("Twitter_Data.csv")

# Convert labels into text sentiment
def convert_label(x):
    if x == 1.0:
        return "Positive"
    elif x == 0.0:
        return "Neutral"
    else:
        return "Negative"

# Create new sentiment column
data['sentiment'] = data['category'].apply(convert_label)

# Count sentiments
counts = data['sentiment'].value_counts()

# Create graph
plt.bar(counts.index, counts.values)

# Labels and title
plt.title("Sentiment Analysis Result")
plt.xlabel("Sentiment")
plt.ylabel("Number of Tweets")

data.to_csv("final_output.csv", index=False)

from textblob import TextBlob

# User input
user_text = input("Enter your text: ")

# Analyze sentiment
analysis = TextBlob(user_text)

# Check polarity
if analysis.sentiment.polarity > 0:
    print("Sentiment: Positive 😊")

elif analysis.sentiment.polarity == 0:
    print("Sentiment: Neutral 😐")

else:
    print("Sentiment: Negative 😡")

plt.show()
