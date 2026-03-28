# fluffle-reddit-bot
 ## needs to be public for  Reddit API approval

A Reddit monitoring bot that helps anime merchandise communities discover relevant products. The bot monitors anime subreddits for posts where users are asking about plushies and merchandise, surfacing helpful product recommendations.

## What it does

- Monitors anime-related subreddits for posts with buy intent keywords
- Identifies users looking for anime plushies and merchandise
- Logs relevant posts for community engagement
- Strictly follows subreddit rules — only engages in communities that allow merchandise discussion

## Subreddits monitored

- r/AnimeMerchandise
- r/Wishlist
- r/JujutsuKaisen
- r/OnePiece
- r/Animefigures
- r/sanrio

## Setup

1. Clone the repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and fill in your Reddit API credentials:
   ```bash
   cp .env.example .env
   ```
4. Get Reddit API credentials at [reddit.com/prefs/apps](https://reddit.com/prefs/apps)
5. Run the bot:
   ```bash
   python src/bot.py
   ```

## Reddit API Usage

This bot uses the [PRAW](https://praw.readthedocs.io/) (Python Reddit API Wrapper) library. It accesses Reddit's API in read mode to monitor posts, and only engages with content where community rules explicitly permit merchandise discussion.

Rate limiting is built in — the bot waits 2 seconds between subreddit requests to stay well within Reddit's API limits.

## License

MIT