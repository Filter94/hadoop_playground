#!/usr/bin/python
import sys

from commons import print_result

if __name__ == "__main__":
    curr_max_key = None
    max_value = 0.
    for line in sys.stdin:
        data = line.strip().split("\t")
        new_key = data[0]
        new_value = float(data[1])
        if curr_max_key != new_key:
            print_result(curr_max_key, max_value)
            curr_max_key = new_key
            max_value = new_value
        else:
            if new_value > max_value:
                max_value = new_value
    print_result(curr_max_key, max_value)
