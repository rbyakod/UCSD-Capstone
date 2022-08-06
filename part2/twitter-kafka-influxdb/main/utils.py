import re

def process_tweet(tweet):

    tweet2 = re.sub(r'^RT[\s]+','', tweet)
   
    #remove hyperlinks
    tweet2 = re.sub(r'https?://[^\s\n\r]+', '', tweet2)
    
    #remove hashtag by removing the hast #sign from the word
    tweet2 = re.sub(r'#','',tweet2)
    
    
    # remove stock market tickers like $GE
    tweet = re.sub(r'\$\w*', '', tweet)
    
    #convert into lower case
    tweets_clean = tweet.lower()

    return tweets_clean

