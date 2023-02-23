import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import pandas as pd

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
stop_words.add('https://')

stemmer = SnowballStemmer('english')

df= pd.read_csv('tweets.csv')

twet=df['Tweet'].unique()

df1=pd.DataFrame(columns=['Tweet'])


def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Remove stop words
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    text = ' '.join(filtered_words)
    
    # Stem words
    words = text.split()
    stemmed_words = [stemmer.stem(word) for word in words]
    text = ' '.join(stemmed_words)



    
    
    return text
for tweet in twet :

    y=preprocess_text(tweet)

    df1 = df1.append({'Tweet': y}, ignore_index=True)

df_tweets=pd.read_csv('tweets.csv')

df_tweets['Tweet']=df1['Tweet']

df_tweets.to_csv('final_tweets.csv')