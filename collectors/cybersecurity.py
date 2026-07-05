import feedparser

from config.sources import CYBER_SECURITY

from utils.models import NewsItem


def get_cyber():

    news = []

    for source in CYBER_SECURITY:

        feed = feedparser.parse(source["rss"])

        for item in feed.entries[:5]:

            news.append(

                NewsItem(

                    category="Cybersecurity",

                    title=item.title,

                    link=item.link,

                    source=source["name"]

                )

            )

    return news