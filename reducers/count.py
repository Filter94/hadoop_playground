#!/usr/bin/python
import sys

from commons import print_result

if __name__ == "__main__":
    curr_key = None
    acc = 0.
    for line in sys.stdin:
        data = line.strip().split("\t")
        new_key = data[0]
        new_value = float(data[1])
        if curr_key != new_key:
            print_result(curr_key, acc)
            curr_key = new_key
            acc = new_value
        else:
            acc += new_value
    print_result(curr_key, acc)
