#!/usr/bin/python
import sys

from commons import pair_template

if __name__ == "__main__":
    curr_max_key = None
    max_value = 0.

    def print_result():
        if curr_max_key is not None:
            print pair_template.format(curr_max_key, max_value)
    for line in sys.stdin:
        data = line.strip().split("\t")
        new_key = data[0]
        new_value = float(data[1])
        if curr_max_key != new_key:
            print_result()
            curr_max_key = new_key
            max_value = new_value
        else:
            if new_value > max_value:
                max_value = new_value
    print_result()

