import os, time, urllib.request, operator, tweepy


class TwitterScrapper:

    def Scrape_Twitter(self, consumerKey, consumerSecret, accessToken, accessTokenSecret, tag, limit=20, lang='en',path="/"):

        print("Starting Scrapping Twitter")

        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)

        tweets = tweepy.Cursor(api.search, q=tag, lang=lang).items(limit)

        hashtags = {}
        lst = []
        Reviewer_data = {'Reviewer Name': [], 'Reviewer Profile URL': [], 'Review': [],'Time': []}
        for tweet in tweets:
            Reviewer_data['Reviewer Name'].append(tweet.user.name)
            Reviewer_data['Reviewer Profile URL'].append('https://www.twitter.com/'+tweet.user.screen_name)
            text1 = tweet.text.lower()
            text=re.sub(r"rt\s@\w+:", " ", text1)
            #if(text not in lst):
                #lst.append(text)
            Reviewer_data['Review'].append(text)
            Reviewer_data['Time'].append(tweet.user.created_at)

            for tag in text.split():
                if tag.startswith("#"):
                    if tag[1:] not in hashtags:
                        hashtags[tag[1:]] = 1
                    elif tag[1:] in hashtags:
                        hashtags[tag[1:]] = hashtags[tag[1:]] + 1
                else:
                    pass

        hashtags = sorted(hashtags.items(), key=operator.itemgetter(1), reverse=True)
        hastag_data = {'hastag': [], 'frequency': []}
        for tag in hashtags:
            hastag_data['hastag'].append(tag[0])
            hastag_data['frequency'].append(tag[1])

        time.sleep(1)

        print("Closing Twitter")    
        pd.DataFrame(hastag_data).to_csv(path+'/Scrapped Reviews/Trending_hastag.csv', index=0)
        pd.DataFrame(Reviewer_data).to_csv(path+'/Scrapped Reviews/twitterdata.csv', index=0)

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
