from services.collector_engine import CollectorEngine
from services.notification_service import NotificationService

from utils.aggregator import merge_collectors
from utils.duplicate_filter import remove_duplicates
from utils.sorter import sort_items
from utils.formatter import build_message


def main():

    engine = CollectorEngine()

    items = engine.collect_all()

    items = remove_duplicates(items)

    items = sort_items(items)

    message = build_message(items)

    NotificationService.send(
        "🚀 AI Intelligence Daily Report",
        message[:4000]
    )


if __name__ == "__main__":
    main()