#!/usr/bin/python
import sys

from commons import print_result

if __name__ == "__main__":
    max_key = None
    max_value = 0
    curr_key = None
    acc = 0
    for line in sys.stdin:
        data = line.strip().split("\t")
        new_key = data[0]
        new_value = float(data[1])
        if curr_key != new_key:
            if acc > max_value:
                max_key = curr_key
                max_value = acc
            curr_key = new_key
            acc = new_value
        else:
            acc += new_value
    print_result(max_key, max_value)
