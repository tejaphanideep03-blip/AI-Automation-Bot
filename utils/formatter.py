def build_message(items):
    text = ""
    current = ""

    for item in items:

        if item.category != current:
            current = item.category
            text += f"\n## {current}\n\n"

        text += f"• {item.title}\n"
        text += f"{item.link}\n\n"

    return text