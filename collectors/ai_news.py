import feedparser

RSS_FEEDS = [
    "https://openai.com/news/rss.xml",
    "https://huggingface.co/blog/feed.xml",
    "https://www.marktechpost.com/feed/",
    "https://venturebeat.com/category/ai/feed/"
]


def get_ai_news():

    news = []

    for url in RSS_FEEDS:

        feed = feedparser.parse(url)

        for entry in feed.entries[:5]:

            news.append({
                "title": entry.title,
                "link": entry.link
            })

    return news