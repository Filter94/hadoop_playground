#!/usr/bin/python
import sys
import re
import csv

from commons import pair_template

if __name__ == "__main__":
    rd = csv.reader(sys.stdin, delimiter="\t", quotechar="\"")
    rd.next()   # skip header
    for row in rd:
        post_id = row[0]
        post = row[4]
        words = re.split("[.,!?:;\"\(\)<>[\]#$=\-/\s]", post)
        for word in words:
            if len(word.strip()) > 0:
                print pair_template.format(word.lower(), post_id)



