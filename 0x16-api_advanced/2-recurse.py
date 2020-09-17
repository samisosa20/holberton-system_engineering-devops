#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles
for a given subreddit. If no results are found for the
given subreddit, the function should return None
"""

import requests


def recurse(subreddit, hot_list=[], after=''):
    """Prints the titles of the first 10 hot posts listed"""
    headers = {
        'User-agent': 'Holberton',
    }
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    req = requests.get(url, headers=headers)

    if (req.status_code != 200):
        return

    childrens = req.json().get('data').get('children')
    for children in childrens:
        hot_list.append(children.get('data').get('title'))

    after = req.json().get('data').get('after')
    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
