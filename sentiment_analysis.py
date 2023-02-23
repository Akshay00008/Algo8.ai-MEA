import pandas as pd
from scipy.special import softmax
from transformers import AutoTokenizer, AutoModelForSequenceClassification

df_tweet = pd.read_csv('final_tweets.csv')
tweets = df_tweet['Tweet']

roberta = "cardiffnlp/twitter-roberta-base-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)
labels = ['Negative', 'Neutral', 'Positive']
i=0
df_senti = pd.DataFrame(columns=['Tweet', 'Sentiment', 'Score'])
for tweet in tweets:
    i=i+1
    print(i)
    # Preprocess tweet
    tweet_words = []
    for word in tweet.split(' '):

        try:

            if word.startswith('@') and len(word) > 1:
                word = '@user'
            elif word.startswith('http'):
                word = "http"
            tweet_words.append(word)

            tweet_proc = " ".join(tweet_words)

            # Sentiment analysis
            encoded_tweet = tokenizer(tweet_proc, return_tensors='pt')
            output = model(**encoded_tweet)
            scores = softmax(output[0][0].detach().numpy())

            sentiment = labels[scores.argmax()]
            score = scores.max()

            df_senti = df_senti.append({'Tweet': tweet, 'Sentiment': sentiment, 'Score': score}, ignore_index=True)
        except :
            pass

df_senti.to_csv('Senti__.csv')
