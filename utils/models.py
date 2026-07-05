from dataclasses import dataclass


@dataclass
class NewsItem:

    category: str

    title: str

    link: str

    source: str