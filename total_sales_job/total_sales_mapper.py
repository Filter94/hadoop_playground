#!/usr/bin/python
import sys

from commons import pair_template

if __name__ == "__main__":
    counter = 0
    for line in sys.stdin:
        counter += 1
        data = line.strip().split("\t")
        if len(data) == 6:
            print pair_template.format("sale", data[4])

