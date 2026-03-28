import praw
import os
import time
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger(__name__)

# Configuration
REDDIT_CLIENT_ID = os.environ.get("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.environ.get("REDDIT_CLIENT_SECRET")
REDDIT_USERNAME = os.environ.get("REDDIT_USERNAME")
REDDIT_PASSWORD = os.environ.get("REDDIT_PASSWORD")
REDDIT_USER_AGENT = "FluffleMerchandiseBot/1.0 by u/AnimePlushieCollector"

# Subreddits to monitor
TARGET_SUBREDDITS = [
    "AnimeMerchandise",
    "Wishlist",
    "JujutsuKaisen",
    "OnePiece",
    "Animefigures",
    "sanrio",
]

# Keywords that indicate someone is looking to buy plushies
BUY_KEYWORDS = [
    "where to buy",
    "where can i find",
    "looking for",
    "recommend",
    "plushie",
    "plush",
    "stuffed animal",
    "merch",
    "merchandise",
]

STORE_URL = "https://flufflestore.com"

def get_reddit_instance():
    return praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        username=REDDIT_USERNAME,
        password=REDDIT_PASSWORD,
        user_agent=REDDIT_USER_AGENT,
    )

def find_buy_intent_posts(reddit, subreddit_name, limit=25):
    """Find posts where users are asking about buying anime merchandise."""
    subreddit = reddit.subreddit(subreddit_name)
    matches = []

    for post in subreddit.new(limit=limit):
        text = (post.title + " " + (post.selftext or "")).lower()
        if any(keyword in text for keyword in BUY_KEYWORDS):
            matches.append(post)
            logger.info(f"Found potential post: {post.title[:60]} in r/{subreddit_name}")

    return matches

def monitor_subreddits():
    """Main monitoring loop - finds relevant posts and logs them for review."""
    reddit = get_reddit_instance()
    logger.info(f"Starting FluffleMerchandiseBot at {datetime.now()}")

    all_matches = []
    for subreddit_name in TARGET_SUBREDDITS:
        try:
            matches = find_buy_intent_posts(reddit, subreddit_name)
            all_matches.extend(matches)
            logger.info(f"r/{subreddit_name}: found {len(matches)} relevant posts")
            time.sleep(2)  # Rate limiting
        except Exception as e:
            logger.error(f"Error in r/{subreddit_name}: {e}")

    logger.info(f"\nTotal posts found: {len(all_matches)}")
    for post in all_matches:
        logger.info(f"  - [{post.subreddit}] {post.title[:80]}")
        logger.info(f"    URL: {post.url}")

    return all_matches

if __name__ == "__main__":
    monitor_subreddits()