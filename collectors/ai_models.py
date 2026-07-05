import feedparser

MODEL_FEEDS = [
    "https://huggingface.co/blog/feed.xml",
    "https://openai.com/news/rss.xml"
]

KEYWORDS = [
    "model",
    "gpt",
    "gemini",
    "claude",
    "llama",
    "mistral",
    "release"
]

def get_models():

    models = []

    for url in MODEL_FEEDS:

        feed = feedparser.parse(url)

        for post in feed.entries:

            title = post.title.lower()

            if any(word in title for word in KEYWORDS):

                models.append({
                    "title": post.title,
                    "link": post.link
                })

    return models