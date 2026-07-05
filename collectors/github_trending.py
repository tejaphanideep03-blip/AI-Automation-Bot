import requests
from bs4 import BeautifulSoup

def get_trending():

    url = "https://github.com/trending"

    html = requests.get(url, timeout=20).text

    soup = BeautifulSoup(html, "html.parser")

    repos = []

    for repo in soup.select("article.Box-row")[:10]:

        name = repo.h2.text.strip().replace("\n", "")

        repos.append({
            "title": name,
            "link": "https://github.com"
        })

    return repos