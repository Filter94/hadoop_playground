#!/usr/bin/python
import sys

from commons import print_result


def print_count_and_amount(key, count, amount):
    mean = 0 if count == 0 else amount / count
    print_result(key, "count: {0}, amount: {1}, mean: {2}".format(count, amount, mean))


if __name__ == "__main__":
    curr_key = None
    total_count = 0
    amount = 0.
    for line in sys.stdin:
        data = line.strip().split("\t")
        new_value = float(data[1])
        new_key = data[0]
        if curr_key != new_key:
            print_count_and_amount(curr_key, total_count, amount)
            curr_key = new_key
            amount = new_value
            total_count = 1
        else:
            amount += new_value
            total_count += 1
    print_count_and_amount(curr_key, total_count, amount)
