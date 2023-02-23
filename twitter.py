import snscrape.modules.twitter as sntwitter
import pandas as pd

query = ["#Nethanyahu","#Joe Biden","#NarendraModi"]
tweets = []
limit = 10000
i=0

df_tweet=pd.DataFrame(columns=['Name','Date', 'id','Tweet'])

for name in query :

    for tweet in sntwitter.TwitterSearchScraper(name).get_items():
        try :

            i=i+1

            print(i+1)

            if len(tweets) == limit:
                break
            else:
                tweets.append([tweet.date, tweet.username, tweet.content])
        except :

            pass
                
    df = pd.DataFrame(tweets, columns=['Date', 'id','Tweet'])

    df['Name']= name

    df_tweet=pd.concat([df_tweet,df],axis=0)

df_tweet.to_csv('tweets.csv')