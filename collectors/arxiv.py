import feedparser

from config.sources import ARXIV
from utils.models import NewsItem


def get_arxiv():

    papers = []

    for source in ARXIV:

        feed = feedparser.parse(source["rss"])

        for paper in feed.entries[:5]:

            papers.append(
                NewsItem(
                    category="Research Papers",
                    title=paper.title,
                    link=paper.link,
                    source=source["name"]
                )
            )

    return papers