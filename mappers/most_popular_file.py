#!/usr/bin/python
import sys

from commons import pair_template, parse_file_path

if __name__ == "__main__":
    for line in sys.stdin:
        file_path = parse_file_path(line)
        prefix = "http://www.the-associates.co.uk"
        if file_path[:len(prefix)] == prefix:
            file_path = file_path[len(prefix):]
        if len(file_path.strip()) > 1:
            print pair_template.format(file_path, 1)

