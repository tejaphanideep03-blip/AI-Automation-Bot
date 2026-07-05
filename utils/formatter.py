def build_message(items):

    if not items:
        return "No updates available."

    text = ""

    current = ""

    for item in items:

        if current != item.category:

            current = item.category

            text += f"\n# {current}\n\n"

        text += (
            f"• {item.title}\n"
            f"{item.link}\n\n"
        )

    return text