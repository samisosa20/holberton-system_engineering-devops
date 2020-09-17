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
                       format(subreddit), headers=header).json()
    list_data = top.get("data", {}).get("children", [])
    tasks = {}
    for post in list_data:
        tasks.update({post.get("data").
                      get("title"): post.get("data").get("ups")})
    sort_orders = sorted(tasks.items(), key=lambda x: x[1], reverse=True)
    for topten in sort_orders[:10]:
        print(topten[0])
