#! /usr/bin/sh

hadoop fs -rm -r /00lifeng/HJF/output/

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
       -input /00lifeng/HJF/stocks.txt \
       -output /00lifeng/HJF/output/ \
       -file "stock_day_avg.R" \
       -mapper "/usr/bin/cat" \
       -reducer "./stock_day_avg.R" \
       -numReduceTasks 1

hadoop fs -cat /00lifeng/HJF/output/*