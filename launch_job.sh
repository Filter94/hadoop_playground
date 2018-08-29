#!/usr/bin/env bash
# example: $ . launch_job.sh week_day_sale.py total_count_and_amount.py $(pwd)/purchases.txt category_sales total_count_and_amount.py
MAPPER=$1
REDUCER=$2
INPUT_FILE=$3
JOB_NAME=$4
COMBINER=$5
MAPPER_PREFIX=$(pwd)/mappers
REDUCER_PREFIX=$(pwd)/reducers
chmod +x $(pwd)/mappers/*.py
chmod +x $(pwd)/reducers/*.py
# hadoop
if [ -z "$COMBINER" ]
then
    hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -mapper ${MAPPER_PREFIX}/${MAPPER} \
    -reducer ${REDUCER_PREFIX}/${REDUCER} \
    -input file://${INPUT_FILE} \
    -output ${JOB_NAME}_output \
    -cmdenv PYTHONPATH="${PYTHONPATH}:$(pwd)" # to make commons.py available
else
    hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -mapper ${MAPPER_PREFIX}/${MAPPER} \
        -combiner ${REDUCER_PREFIX}/${COMBINER}\
        -reducer ${REDUCER_PREFIX}/${REDUCER} \
        -input file://${INPUT_FILE} \
        -output ${JOB_NAME}_output \
        -cmdenv PYTHONPATH="${PYTHONPATH}:$(pwd)" # to make commons.py available
fi
hadoop fs -cat ${JOB_NAME}_output/part-00000
# debug
#export PYTHONPATH="${PYTHONPATH}:$(pwd)"
#cat ${INPUT_FILE} | python ${MAPPER_PREFIX}/${MAPPER} | sort | python ${REDUCER_PREFIX}/${REDUCER} > ${JOB_NAME}.txt