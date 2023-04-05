import requests
from bs4 import BeautifulSoup
import praw
import dotenv
import os

def scrape():
    dotenv.load_dotenv()

    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
    CLIENT_USER_AGENT = os.environ.get("CLIENT_USER_AGENT")

    reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=CLIENT_USER_AGENT)


    top_post = reddit.subreddit('Showerthoughts').top(time_filter="day",limit=1)

    for post in top_post:
        post = post.title
        print(post.title)
    
    return post
