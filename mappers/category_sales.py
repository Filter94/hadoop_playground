#!/usr/bin/python
import sys

from commons import pair_template

if __name__ == "__main__":
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) == 6:
            print pair_template.format(data[3], data[4])
