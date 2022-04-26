#!/usr/bin/python3
""" redit api check
"""

n = 0


def recurse(subreddit, hot_list=[], after=None):
    """ return number of subcribers
        * subreddit - get subreddit account
    """
    import requests

    req = requests.get('https://www.reddit.com/r/{}/hot.json'
                       .format(subreddit),
                       params={'limit':1, 'after':after},
                       headers={'User-agent': 'fitsum'},
                       allow_redirects=False)
    if req.status_code >= 300:
        return None

    if req.json()['data']['after']:
        data = req.json()['data']['children'][0]
        hot_list.append(data['data']['title'])
        print(hot_list)
        recurse(subreddit, hot_list, req.json()['data']['after'])
    else:
        return hot_list

