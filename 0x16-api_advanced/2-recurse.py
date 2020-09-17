#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles
for a given subreddit. If no results are found for the
given subreddit, the function should return None
"""

import requests


def recurse(subreddit, hot_list=[], after=''):
    header = {'User-Agent': 'APP-NAME by REDDIT-USERNAME'}
    top = requests.get("https://www.reddit.com/r/{}/hot.json?after={}".
                       format(subreddit, after), headers=header,
                       allow_redirects=False).json()
    after = top.get("data", {}).get("after", [])
    list_data = top.get("data", {}).get("children", [])
    if not list_data:
        return(None)
    else:
        list_title = []
        for topten in list_data:
            list_title.append(topten.get("data").get("title"))
        if list_title is None:
            return(None)
        else:
            return(recurse(subreddit, list_title, after))
