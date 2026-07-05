import feedparser

from config.settings import AI_NEWS_FEEDS
from utils.models import NewsItem


def get_ai_news():

    news = []

    for url in AI_NEWS_FEEDS:

        feed = feedparser.parse(url)

        for entry in feed.entries[:5]:

            news.append(
                NewsItem(
                    category="AI News",
                    title=entry.title,
                    link=entry.link,
                    source=url
                )
            )

    return news