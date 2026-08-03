def split_file(input_file, num_mappers):
    with open(input_file, "r") as f:
        lines = f.readlines()

    chunk_size = (len(lines) + num_mappers - 1) // num_mappers

    chunks = []

    for i in range(num_mappers):
        chunk = lines[i * chunk_size:(i + 1) * chunk_size]
        filename = f"chunk_{i}.txt"

        with open(filename, "w") as cf:
            cf.writelines(chunk)

        chunks.append(filename)

    return chunks