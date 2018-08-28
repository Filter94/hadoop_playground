#!/usr/bin/python
import sys

if __name__ == "__main__":
    curr_max_key = None
    total_count = 0
    amount = 0.

    for line in sys.stdin:
        total_count += 1
        data = line.strip().split("\t")
        new_value = float(data[1])
        amount += new_value
    print "Total count: {0} total amount: {1}".format(total_count, amount)
