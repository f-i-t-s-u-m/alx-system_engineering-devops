#!/usr/bin/python3
""" redit api check
"""


def number_of_subscribers(subreddit):
    """ return number of subcribers
        * subreddit - get subreddit account
    """
    import requests

    req = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit),
                       headers={'User-agent': 'fitsum'},
                       allow_redirects=False)
    if req.status_code >= 300:
        return 0

    return req.json()['data']['subscribers']
