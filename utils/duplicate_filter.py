def remove_duplicates(items):

    seen = set()

    unique = []

    for item in items:

        if item.link in seen:
            continue

        seen.add(item.link)

        unique.append(item)

    return unique