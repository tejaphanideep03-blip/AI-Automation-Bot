import feedparser

from config.settings import REDDIT_SUBREDDITS

from utils.models import NewsItem


def get_reddit():

    posts = []

    for sub in REDDIT_SUBREDDITS:

        feed = feedparser.parse(
            f"https://www.reddit.com/r/{sub}/new/.rss"
        )

        for item in feed.entries[:5]:

            posts.append(
                NewsItem(
                    category="Reddit",
                    title=item.title,
                    link=item.link,
                    source=sub
                )
            )

    return posts