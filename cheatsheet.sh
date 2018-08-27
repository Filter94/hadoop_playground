#!/usr/bin/env bash
docker exec -ti %container_name% /bin/bash
docker run --hostname=quickstart.cloudera --privileged=true -ti %image_id% /usr/bin/docker-quickstart
docker cp category_sales_job %container name%:/jobs
cat purchases.txt | python category_sales_mapper.py | sort | python category_sales_reducer.py
