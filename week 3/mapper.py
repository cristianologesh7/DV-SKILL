def map_data(chunk_file):

    mapped = []

    with open(chunk_file, "r") as f:
        for line in f:
            key = line.strip()

            if key:
                mapped.append((key, 1))

    return mapped