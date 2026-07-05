def merge_collectors(*lists):
    result = []

    for lst in lists:
        result.extend(lst)

    return result