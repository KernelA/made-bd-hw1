#!/bin/bash

OUT_FILE=/mnt/output/computed_stat.txt

pushd /mnt/scripts

python ./standard_stat.py --file /mnt/input/AB_NYC_2019.csv.gz > "${OUT_FILE}"

hdfs dfs -rm -r /data/out


mapred streaming -files mapper.py,reducer.py -input /data/AB_NYC_2019.csv -output /data/out -mapper mapper.py -reducer reducer.py

hdfs dfs -cat /data/out/part-00000 >> "${OUT_FILE}"

popd