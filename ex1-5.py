import os
import json
import twitter
import pat_twit

twitter_api = pat_twit.create_twitter_api()
q = '#SundayMorning'

count = 50

search_results = twitter_api.search.tweets(q=q, count=count)
statuses = search_results['statuses']

print(json.dumps(statuses, indent=1))

for _ in range(5):
    print("Length: ", len(statuses))
    try:
        next_results = search_results['search_metadata']['next_results']
    except KeyError:
        break

    kwargs = dict([kv.split('=') for kv in next_results[1:].split("&")])

    search_results = twitter_api.search.tweets(**kwargs)

    statuses += search_results['statuses']

print(json.dumps(statuses[0], indent=1))
