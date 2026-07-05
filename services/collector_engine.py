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
            get_arxiv      # <-- Added here
        ]

    def collect_all(self):

        results = []

        for collector in self.collectors:

            logger.info(f"Starting collection for {collector.__name__}")

            try:
                items = collector()
                results.extend(items)

                logger.info(
                    f"{collector.__name__} completed successfully "
                    f"({len(items)} items)"
                )

            except Exception as e:

                logger.exception(
                    f"{collector.__name__} failed with error: {e}"
                )

        logger.info(f"Total items collected: {len(results)}")

        return results