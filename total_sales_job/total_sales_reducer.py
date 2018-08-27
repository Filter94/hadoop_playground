#!/usr/bin/python
import sys

if __name__ == "__main__":
    curr_max_key = None
    total_sales = 0
    sales_amount = 0.

    for line in sys.stdin:
        total_sales += 1
        data = line.strip().split("\t")
        new_key = data[0]
        new_value = float(data[1])
        sales_amount += new_value
    print "Total sales: {0} total amount: {1}".format(total_sales, sales_amount)
