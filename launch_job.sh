#!/usr/bin/env bash
# example: $ . launch_job.sh category_sales $(pwd)/purchases.txt
JOB_NAME=$1
INPUT_FILE=$2
chmod +x $(pwd)/${JOB_NAME}_job/*.py
SCRIPT_PREFIX=$(pwd)/${JOB_NAME}_job/${JOB_NAME}
# hadoop
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-mapper ${SCRIPT_PREFIX}_mapper.py \
-reducer ${SCRIPT_PREFIX}_reducer.py \
-input file://${INPUT_FILE} \
-output ${JOB_NAME}_output \
-cmdenv PYTHONPATH="${PYTHONPATH}:$(pwd)" # to make commons.py available
hadoop fs -cat ${JOB_NAME}_output/part-00000
# debug
#export PYTHONPATH="${PYTHONPATH}:$(pwd)"
# cat ${INPUT_FILE} | python ${SCRIPT_PREFIX}_mapper.py | sort | python ${SCRIPT_PREFIX}_reducer.py

