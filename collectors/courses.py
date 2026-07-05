import feedparser

COURSE_FEEDS = [
    # Add course RSS feeds if available
]

KEYWORDS = [
    "free",
    "course",
    "certificate",
    "certification",
    "ai",
    "cybersecurity"
]

def get_courses():

    courses = []

    for url in COURSE_FEEDS:

        feed = feedparser.parse(url)

        for item in feed.entries:

            title = item.title.lower()

            if any(word in title for word in KEYWORDS):

                courses.append({
                    "title": item.title,
                    "link": item.link
                })

    return courses