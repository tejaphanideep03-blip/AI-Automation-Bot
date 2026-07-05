CATEGORY_ORDER = [
    "AI News",
    "Models",
    "Research Papers",
    "Cybersecurity",
    "GitHub",
    "Reddit",
    "Internships",
    "Courses"
]

def sort_items(items):

    return sorted(
        items,
        key=lambda x: CATEGORY_ORDER.index(x.category)
        if x.category in CATEGORY_ORDER
        else 99
    )