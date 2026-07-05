import feedparser

SUBREDDITS = [
    "MachineLearning",
    "LocalLLaMA",
    "artificial"
]

def get_reddit():

    posts = []

    for sub in SUBREDDITS:

        feed = feedparser.parse(
            f"https://www.reddit.com/r/{sub}/new/.rss"
        )

        for item in feed.entries[:5]:

            posts.append({
                "title": item.title,
                "link": item.link
            })

    return posts