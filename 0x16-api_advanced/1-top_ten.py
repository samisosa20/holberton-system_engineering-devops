#!/usr/bin/python3
"""
Write a function that queries the Reddit API
and prints the titles of the first 10 hot
posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    header = {'User-Agent': 'APP-NAME by REDDIT-USERNAME'}
    top = requests.get("https://www.reddit.com/r/{}/hot.json".
                       format(subreddit), headers=header,
                       allow_redirects=False).json()
    list_data = top.get("data", {}).get("children", [])
    if not list_data:
        print(None)
    for topten in list_data[:10]:
        print(topten.get("data").get("title"))
