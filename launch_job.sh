#!/usr/bin/env bash
# example: $ . launch_job.sh category_sales $(pwd)/purchases.txt
JOB_NAME=$1
INPUT_FILE=$2
chmod +x $(pwd)/${JOB_NAME}_job/*.py
# hadoop
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-mapper $(pwd)/${JOB_NAME}_job/${JOB_NAME}_mapper.py \
-reducer $(pwd)/${JOB_NAME}_job/${JOB_NAME}_reducer.py \
-input file://${INPUT_FILE} -output output \
-cmdenv PYTHONPATH="${PYTHONPATH}:$(pwd)" # to make commons.py available
hadoop fs -cat output/part-00000
# debug
# cat ${INPUT_FILE} | python $(pwd)/${JOB_NAME}_job/${JOB_NAME}_mapper.py | sort | python $(pwd)/${JOB_NAME}_job/${JOB_NAME}_reducer.py

