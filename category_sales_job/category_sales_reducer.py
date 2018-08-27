#!/usr/bin/python
import sys

from commons import pair_template

if __name__ == "__main__":
    curr_key = None
    acc = 0.

    def print_result():
        if curr_key is not None:
            print pair_template.format(curr_key, acc)
    for line in sys.stdin:
        data = line.strip().split("\t")
        new_key = data[0]
        new_value = float(data[1])
        if curr_key != new_key:
            print_result()
            curr_key = new_key
            acc = new_value
        else:
            acc += new_value
    print_result()
