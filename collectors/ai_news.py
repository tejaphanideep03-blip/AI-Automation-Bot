import feedparser

from config.sources import AI_NEWS

from utils.models import NewsItem


def get_ai_news():

    news = []

    for source in AI_NEWS:

        feed = feedparser.parse(source["rss"])

        for entry in feed.entries[:5]:

            news.append(

                NewsItem(

                    category="AI News",

                    title=entry.title,

                    link=entry.link,

                    source=source["name"]

                )

            )

    return news