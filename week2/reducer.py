from collections import defaultdict
import os

def reduce_partition(partition_file, output_file):

    counts = defaultdict(int)

    with open(partition_file, "r") as f:
        for line in f:
            key, value = line.strip().split("\t")
            counts[key] += int(value)

    with open(output_file, "w") as out:
        for key in sorted(counts):
            out.write(f"{key}\t{counts[key]}\n")