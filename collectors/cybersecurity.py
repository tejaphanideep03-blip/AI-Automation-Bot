import feedparser

from config.settings import CYBER_FEEDS

from utils.models import NewsItem


def get_cyber():

    news = []

    for url in CYBER_FEEDS:

        feed = feedparser.parse(url)

        for item in feed.entries[:5]:

            news.append(
                NewsItem(
                    category="Cybersecurity",
                    title=item.title,
                    link=item.link,
                    source=url
                )
            )

    return news