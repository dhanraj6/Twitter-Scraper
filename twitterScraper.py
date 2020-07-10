import os, time, urllib.request, openpyxl, operator, tweepy
from openpyxl import Workbook

class TwitterScrapper:
 
    def Scrape_Twitter(self, Consumer_Key, Consumer_Secret, Access_Token, Access_Token_Secret, tag, limit=20, lang='en'):
       

        print("Starting Scrapping Twitter")

        consumerKey = Consumer_Key
        consumerSecret = Consumer_Secret
        accessToken = Access_Token
        accessTokenSecret = Access_Token_Secret

        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)

        tweets = tweepy.Cursor(api.search, q=tag, lang=lang).items(limit)

        hashtags = {}
        lst=[]
        for tweet in tweets:
            text = tweet.text.lower()
            lst.append(text)

            # stripping for urls and hashtags and their frequencies
            for tag in text.split():
                if tag.startswith("#"):
                    if tag[1:] not in hashtags:
                        hashtags[tag[1:]] = 1
                    elif tag[1:] in hashtags:
                        hashtags[tag[1:]] = hashtags[tag[1:]] + 1
                else:
                    pass


        hashtags = sorted(hashtags.items(), key=operator.itemgetter(1), reverse=True)

        for tag in hashtags:
           print(tag)

        time.sleep(5)


        print("Closing Twitter")

#Add your api related details below
consumerKey = ' enter your consumer key '
consumerSecret = 'enter your consumerSecret '
accessToken = 'enter your accessToken'
accessTokenSecret = 'enter your accessTokenSecret'

keyword = str(input("Enter keyword to search for: "))
twitter_limit = int(input("Enter how many posts to scrape from Twitter: "))
twitter = TwitterScrapper()
twitter.Scrape_Twitter(Consumer_Key=consumerKey,Consumer_Secret=consumerSecret,Access_Token=accessToken,Access_Token_Secret=accessTokenSecret,tag=keyword,limit=twitter_limit,lang='en')  
