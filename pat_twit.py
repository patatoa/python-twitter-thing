#!/usr/bin/python
""" common functions for my python twitter piddlin"""

import os
import json
import twitter

def create_twitter_api():
    """ Sets up Twitter api caller """
    CONSUMER_KEY = 'qd35nCDinA4DLRpspdvPtMdmH'
    OAUTH_TOKEN = '101673271-XTZn6oQlFkBmpCj7mX5zGNHtrfoNctBO4sz0cuVv'
    try:
        CONSUMER_SECRET = os.environ['ConsumerSecret']
        OAUTH_TOKEN_SECRET = os.environ['OauthSecret']
    except KeyError as e:
        print(type(e))

    # WORLD_WOE_ID = 1
    # US_WOE_ID = 23424977

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)

    # world_trends = twitter_api.trends.place(_id = WORLD_WOE_ID)

    # us_trends = twitter_api.trends.place(_id = US_WOE_ID)

    # world_trends_set = set([trend['name'] for trend in world_trends[0]['trends']])
    # us_trends_set = set([trend['name'] for trend in us_trends[0]['trends']])

    # common_trends = world_trends_set.intersection(us_trends_set)

    # print(common_trends)
    return twitter_api
