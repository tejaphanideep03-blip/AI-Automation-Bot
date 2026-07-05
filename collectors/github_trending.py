import requests

from bs4 import BeautifulSoup

from config.settings import GITHUB_TRENDING

from utils.models import NewsItem


def get_trending():

    html = requests.get(
        GITHUB_TRENDING,
        timeout=20
    ).text

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    repos = []

    for repo in soup.select("article.Box-row")[:10]:

        name = repo.h2.text.strip().replace("\n", "")

        repos.append(
            NewsItem(
                category="GitHub",
                title=name,
                link="https://github.com",
                source="GitHub"
            )
        )

    return repos