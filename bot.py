import tweepy
import random
from secrets import *

#create an OAuthHandler instance
# Twitter requires all requests to use OAuth for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

auth.set_access_token(access_token, access_secret)

 #Construct the API instance
api = tweepy.API(auth) # create an API object
def getFollowers(username): 
	followers = api.followers(username)
	followers = random.sample(followers, len(followers))

	final = []

	for follower in followers:
		final.append("@" + follower.screen_name)
	
	return final[:5]

#print (getFollowers("jajoosam"))


def followers(username, status_id):
	#api.update_status(" ".join(getFollowers(username)), in_reply_to_status_id=status_id)
	api.update_status(status='@{0}'.format(username) + " Here are some of your f00ll0wers - " + " ".join(getFollowers(username)), in_reply_to_status_id=status_id)
# create a class inheriting from the tweepy  StreamListener
class BotStreamer(tweepy.StreamListener):
    # Called when a new status arrives which is passed down from the on_data method of the StreamListener
    def on_status(self, status):
        username = status.user.screen_name
        status_id = status.id
        print(username)
        print (status_id)
        followers(username, status_id)

        # entities provide structured data from Tweets including resolved URLs, media, hashtags and mentions without having to parse the text to extract that information
        #if 'user_mentions' in status.entities:
          #  for person in status.entities['user_mentions']:
            #    followers(person['id'], status_id)

myStreamListener = BotStreamer()
# Construct the Stream instance
stream = tweepy.Stream(auth, myStreamListener)
stream.filter(track=['@f00l0wers'])