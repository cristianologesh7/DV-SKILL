import os

def partition(mapped_data, reducers):

    os.makedirs("partitions", exist_ok=True)

    files = []

    for i in range(reducers):
        files.append(open(f"partitions/partition_{i}.txt", "a"))

    for key, value in mapped_data:
        r = hash(key) % reducers
        files[r].write(f"{key}\t{value}\n")

    for f in files:
        f.close()