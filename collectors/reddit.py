import feedparser

from config.sources import REDDIT

from utils.models import NewsItem


def get_reddit():

    posts = []

    for subreddit in REDDIT:

        feed = feedparser.parse(

            f"https://www.reddit.com/r/{subreddit}/new/.rss"

        )

        for item in feed.entries[:5]:

            posts.append(

                NewsItem(

                    category="Reddit",

                    title=item.title,

                    link=item.link,

                    source=subreddit

                )

            )

    return posts