from collectors.ai_news import get_ai_news
from collectors.ai_models import get_models
from collectors.reddit import get_reddit
from collectors.github_trending import get_trending
from collectors.cybersecurity import get_cyber
from collectors.arxiv import get_arxiv

from utils.logger import logger


class CollectorEngine:

    def __init__(self):
        self.collectors = [
            get_ai_news,
            get_models,
            get_reddit,
            get_trending,
            get_cyber,
            get_arxiv
        ]

    def collect_all(self):

        results = []

        print("\n========== Collector Results ==========\n")

        for collector in self.collectors:

            try:

                items = collector()

                print(f"{collector.__name__:<20} : {len(items)} items")

                logger.info(
                    f"{collector.__name__}: {len(items)} items"
                )

                results.extend(items)

            except Exception as e:

                print(f"{collector.__name__:<20} : FAILED")

                logger.exception(e)

        print(f"\nTOTAL : {len(results)} items\n")

        return results