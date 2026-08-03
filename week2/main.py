import os

from splitter import split_file
from mapper import map_data
from partitioner import partition
from sorter import sort_partitions
from reducer import reduce_partition

NUM_MAPPERS = 2
NUM_REDUCERS = 2

os.makedirs("output", exist_ok=True)

# Clear old partition files
os.makedirs("partitions", exist_ok=True)
for f in os.listdir("partitions"):
    os.remove(os.path.join("partitions", f))

chunks = split_file("input.txt", NUM_MAPPERS)

for chunk in chunks:
    mapped = map_data(chunk)
    partition(mapped, NUM_REDUCERS)

sort_partitions()

for i in range(NUM_REDUCERS):
    reduce_partition(
        f"partitions/partition_{i}.txt",
        f"output/result_{i}.txt"
    )

print("Flipkart category analysis completed.")