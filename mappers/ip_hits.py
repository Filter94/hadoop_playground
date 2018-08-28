#!/usr/bin/python
import sys

from commons import pair_template

if __name__ == "__main__":
    for line in sys.stdin:
        ip_end_idx = line.find(" ")
        ip = line[:ip_end_idx]
        print pair_template.format(ip, 1)

