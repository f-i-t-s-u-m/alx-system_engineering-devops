#!/usr/bin/python3
""" redit api check
"""


def top_ten(subreddit):
    """ return number of subcribers
        * subreddit - get subreddit account
    """
    import requests

    req = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'
                       .format(subreddit),
                       headers={'User-agent': 'fitsum'},
                       allow_redirects=False)
    if req.status_code >= 300:
        print('None')
        return

    for p in req.json()['data']['children']:
        print(p['data']['title'])
