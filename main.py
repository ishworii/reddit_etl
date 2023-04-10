import os

import praw
from dotenv import load_dotenv
from nltk import download
from nltk.sentiment import SentimentIntensityAnalyzer

download('vader_lexicon')  # Download the VADER lexicon for sentiment analysis

# Load environment variables from .env file
load_dotenv()

# Set up the PRAW and SentimentIntensityAnalyzer instances
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

sia = SentimentIntensityAnalyzer()


def analyze_subreddit(subreddit_name, num_posts=10):
    subreddit = reddit.subreddit(subreddit_name)
    top_posts = subreddit.top(limit=num_posts)

    post_sentiments = []
    for post in top_posts:
        if not post.is_self:
            continue  # Skip posts without text (e.g., image, video, or link posts)

        sentiment = sia.polarity_scores(post.selftext)
        post_sentiments.append({
            'title': post.title,
            'text': post.selftext,
            'score': post.score,
            'sentiment': sentiment
        })

    return post_sentiments


subreddit_name = "Upwork"
post_sentiments = analyze_subreddit(subreddit_name)

for post in post_sentiments:
    print(post)
