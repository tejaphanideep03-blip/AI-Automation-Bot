def merge_collectors(*collector_lists):

    merged = []

    for collector in collector_lists:
        merged.extend(collector)

    return merged