import tweepy
client = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAC5X9AEAAAAA2z80v9epo09%2BzsNw%2FVJvVAFMczI%3DnfaX9mlAtANkxQz4OTojbVmrsShkiGS9lBbyLEVs6jFypuiJXm")
tweets = client.search_recent_tweets(query="AI", max_results=5)
for tweet in tweets.data:
    print(tweet.text)