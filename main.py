from services.collector_engine import CollectorEngine
from services.notification_service import NotificationService

from utils.duplicate_filter import remove_duplicates
from utils.sorter import sort_items
from utils.formatter import build_message


MAX_DISCORD_LENGTH = 3900


def split_message(message, limit=MAX_DISCORD_LENGTH):
    """Split a long message into chunks for Discord."""

    chunks = []

    while len(message) > limit:

        split_at = message.rfind("\n", 0, limit)

        if split_at == -1:
            split_at = limit

        chunks.append(message[:split_at])

        message = message[split_at:]

    chunks.append(message)

    return chunks


def main():

    engine = CollectorEngine()

    items = engine.collect_all()

    items = remove_duplicates(items)

    items = sort_items(items)

    message = build_message(items)

    parts = split_message(message)

    for index, part in enumerate(parts, start=1):

        if len(parts) == 1:
            title = "🚀 AI Intelligence Daily Report"
        else:
            title = f"🚀 AI Intelligence Daily Report ({index}/{len(parts)})"

        NotificationService.send(
            title,
            part
        )


if __name__ == "__main__":
    main()