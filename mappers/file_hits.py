#!/usr/bin/python
import sys
import re

from commons import pair_template, parse_log_entry

if __name__ == "__main__":
    for line in sys.stdin:
        data = parse_log_entry(line)
        request = data.group("request")
        file_path = re.match(".+ (.*) .*", request).group(1)
        if len(file_path.strip()) > 1:
            print pair_template.format(file_path, 1)

