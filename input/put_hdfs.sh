#!/bin/bash

hdfs dfs -mkdir -p /data
cat /mnt/input/AB_NYC_2019.csv.gz | gzip -d | hdfs dfs -put - /data/AB_NYC_2019.csv
