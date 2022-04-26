#!/usr/bin/python3
""" redit api check
"""

import requests


def number_of_subscribers(subreddit):
    """ return number of subcribers
        * subreddit - get subreddit account
    """

    base_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    header = {'User-Agent': 'alx'}
    req = requests.get(base_url, headers=header, allow_redirects=False)
    if req.status_code == 200:
        data = req.json().get('data')
        if data:
            return data.get('subscribers', 0)

    return 0
