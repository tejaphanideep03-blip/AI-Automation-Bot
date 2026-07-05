import feedparser

FEEDS = [
    "https://feeds.feedburner.com/TheHackersNews"
]

def get_cyber():

    news = []

    for url in FEEDS:

        feed = feedparser.parse(url)

        for item in feed.entries[:5]:

            news.append({
                "title": item.title,
                "link": item.link
            })

    return news