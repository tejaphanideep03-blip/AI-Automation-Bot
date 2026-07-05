def make_section(title, items):

    if not items:
        return ""

    text = f"## {title}\n\n"

    for item in items[:5]:
        text += f"• {item['title']}\n{item['link']}\n\n"

    return text