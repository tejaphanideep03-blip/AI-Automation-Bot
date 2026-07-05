from datetime import datetime
from collections import defaultdict

EMOJIS = {
    "AI News": "📰",
    "Models": "🤖",
    "Research Papers": "📚",
    "Cybersecurity": "🔐",
    "GitHub": "💻",
    "Reddit": "👥",
    "Internships": "💼",
    "Courses": "🎓"
}

# Maximum number of items to display for each category
MAX_ITEMS_PER_CATEGORY = 5


def build_message(items):

    if not items:
        return "No updates available."

    # Group items by category
    grouped = defaultdict(list)

    for item in items:
        grouped[item.category].append(item)

    message = (
        "🚀 **AI INTELLIGENCE DAILY REPORT**\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📅 Generated: {datetime.now().strftime('%d-%m-%Y %H:%M')}\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
    )

    # Display each category
    for category, category_items in grouped.items():

        emoji = EMOJIS.get(category, "📌")

        message += f"{emoji} **{category.upper()}**\n"
        message += "──────────────────────────────\n"

        for index, item in enumerate(category_items[:MAX_ITEMS_PER_CATEGORY], start=1):

            message += (
                f"**{index}. {item.title}**\n"
                f"🔗 {item.link}\n\n"
            )

        # Show how many more items exist
        if len(category_items) > MAX_ITEMS_PER_CATEGORY:

            remaining = len(category_items) - MAX_ITEMS_PER_CATEGORY

            message += (
                f"➕ *{remaining} more {category.lower()} updates...*\n\n"
            )

    message += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    message += f"📊 **Total Updates:** {len(items)}\n"
    message += "🤖 AI Intelligence System"

    return message