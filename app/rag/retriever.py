def retrieve(query, chunks):
    results = []

    for chunk in chunks:
        if query.lower() in chunk.lower():
            results.append(chunk)

    return results[:3]