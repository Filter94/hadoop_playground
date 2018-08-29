#!/usr/bin/python
import sys

from commons import pair_template
from datetime import datetime

if __name__ == "__main__":
    for line in sys.stdin:
        data = line.strip().split("\t")
        date = data[0]
        weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
        if len(data) == 6:
            print pair_template.format(weekday, data[4])
