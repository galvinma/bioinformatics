import glob
import os
import gzip

target_dir = "/path/to/run/RUN_ID/"
read_counts = {}
spent = []

for i, fgz in enumerate(glob.glob(f"{target_dir}/*.gz")):
    if "fastq" in fgz and fgz not in spent:
        print(f"Found fastq at {fgz}")
        spl = fgz.split("/")[4]
        sample = spl.split("_")[1]
        print(f"processing {sample}")
        counts = 0
        with gzip.open(fgz, 'r') as f:
            for line in f:
                counts = counts + 1

            # Assume 4 lines per read (metadata, sequence, +, scores)
            counts = round(counts / 4, 0)
            if sample in read_counts:
                read_counts[sample] = read_counts[sample] + counts
            else:
                read_counts[sample] = counts
        print(f"Done reading lines for {sample}. Found {counts} reads.")   
        print(f"Total reads for {sample} is {read_counts[sample]}.")        
        spent.append(fgz)

print(read_counts)
for sample in read_counts:
    reads = read_counts[sample]
    print(f"{sample} has {reads} reads")
