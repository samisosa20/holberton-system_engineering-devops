#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles
for a given subreddit. If no results are found for the
given subreddit, the function should return None
"""

import requests


def recurse(subreddit, hot_list=[]):
    header = {'User-Agent': 'APP-NAME by REDDIT-USERNAME'}
    top = requests.get("https://www.reddit.com/r/{}/hot.json".
                       format(subreddit), headers=header,
                       allow_redirects=False).json()
    list_data = top.get("data", {}).get("children", [])
    if not list_data:
        print(None)
    else:
        return(list_data)
