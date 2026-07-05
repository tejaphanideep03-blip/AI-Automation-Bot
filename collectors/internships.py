import feedparser

INTERNSHIP_FEEDS = [
    # Add RSS-capable internship sources here as you expand
]

KEYWORDS = [
    "intern",
    "internship",
    "machine learning",
    "artificial intelligence",
    "cybersecurity",
    "ai"
]

def get_internships():

    internships = []

    for url in INTERNSHIP_FEEDS:

        feed = feedparser.parse(url)

        for item in feed.entries:

            title = item.title.lower()

            if any(word in title for word in KEYWORDS):

                internships.append({
                    "title": item.title,
                    "link": item.link
                })

    return internships