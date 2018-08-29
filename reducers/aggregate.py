#!/usr/bin/python
import sys

from commons import print_result


def print_count_and_words(key, words):
    print_result(key, "count: {0}, {1}".format(len(words), str(words)))


if __name__ == "__main__":
    curr_key = None
    acc = []
    for line in sys.stdin:
        data = line.strip().split("\t")
        new_key = data[0]
        new_value = int(data[1])
        if curr_key != new_key:
            print_count_and_words(curr_key, acc)
            curr_key = new_key
            acc = [new_value]
        else:
            acc.append(new_value)
    print_count_and_words(curr_key, acc)
