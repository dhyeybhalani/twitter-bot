import tweepy

auth = tweepy.OAuthHandler('',
                           '')
auth.set_access_token('',
                      '')

api = tweepy.API(auth)

# for follower in tweepy.Cursor(api.followers).items():
#    if follower.name == 'Thakkar Nihal':
#        follower.follow()
search_string = 'cars'
numberoftweets = 2
for tweet in tweepy.Cursor(api.search, search_string).items(numberoftweets):
    try:
        tweet.retweet()
        print('I like that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
