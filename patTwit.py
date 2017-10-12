import twitter
import os

CONSUMER_KEY = 'qd35nCDinA4DLRpspdvPtMdmH'
OAUTH_TOKEN = '101673271-XTZn6oQlFkBmpCj7mX5zGNHtrfoNctBO4sz0cuVv'
try:
    CONSUMER_SECRET = os.environ['ConsumerSecret']
    OAUTH_TOKEN_SECRET = os.environ['OauthSecret']
except KeyError as e:
    print(type(e))

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

print(twitter_api)
