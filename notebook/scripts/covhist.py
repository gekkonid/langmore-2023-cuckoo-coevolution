#!/usr/bin/env python
import sys
from collections import Counter

counts = Counter()
for line in open(sys.argv[1]):
    contig, pos, cov = line.strip().split()
    counts[int(float(cov))] += 1

print("coverage\tbases_covered")
for k, v in sorted(counts.most_common()):
    print(k, v, sep="\t")
