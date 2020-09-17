#!/usr/bin/python3
"""
Write a function that queries the Reddit API and
returns the number of subscribers (not active users,
total subscribers) for a given subreddit. If an
invalid subreddit is given, the function should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    header = {'User-Agent': 'APP-NAME by REDDIT-USERNAME'}
    number = requests.get("https://www.reddit.com/r/{}/about.json".
                          format(subreddit), headers=header).json()

    return (number.get("data", {}).get("subscribers", 0))
