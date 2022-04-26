#!/usr/bin/python3
""" redit api check
"""

n = 0


def recurse(subreddit, hot_list=[], after=None, count=0):
    """ return number of subcribers
        * subreddit - get subreddit account
    """
    import requests

    req = requests.get('https://www.reddit.com/r/{}/hot.json'
                       .format(subreddit),
                       params={'count': count, 'after': after},
                       headers={'User-agent': 'fitsum'},
                       allow_redirects=False)
    if req.status_code >= 400:
        return None

    if req.json()['data']['after']:
        data = req.json()['data']
        children = data['children']
        new_list = [x['data']['title'] for x in children]
        hot_list.append(new_list)

        recurse(subreddit, hot_list, data['after'], data.get('count'))
    else:
        return hot_list
