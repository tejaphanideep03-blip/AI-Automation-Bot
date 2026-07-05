import feedparser

from config.settings import (
    AI_NEWS_FEEDS,
    MODEL_KEYWORDS
)

from utils.models import NewsItem


def get_models():

    models = []

    for url in AI_NEWS_FEEDS:

        feed = feedparser.parse(url)

        for post in feed.entries:

            title = post.title.lower()

            if any(word in title for word in MODEL_KEYWORDS):

                models.append(
                    NewsItem(
                        category="Models",
                        title=post.title,
                        link=post.link,
                        source=url
                    )
                )

    return models