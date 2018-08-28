#!/usr/bin/python
import sys

from commons import pair_template, parse_log_entry

if __name__ == "__main__":
    for line in sys.stdin:
        data = parse_log_entry(line)
        ip = data.group("ip")
        print pair_template.format(ip, 1)

