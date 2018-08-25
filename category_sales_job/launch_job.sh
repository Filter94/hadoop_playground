#!/usr/bin/env bash
chmod +x *.py
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -mapper /jobs/category_sales_job/category_sales_mapper.py -reducer /jobs/category_sales_job/category_sales_reducer.py -input file:///jobs/category_sales_job/purchases.txt -output output
hadoop fs -cat output/part-00000
