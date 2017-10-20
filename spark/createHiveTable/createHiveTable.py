import collections
from operator import add
from pyspark import SparkContext, SparkConf
from pyspark.sql import Row
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql import functions
from pyspark.sql.types import *
from pyspark.sql.window import Window
import sys

class executeFun():
    def getSparkSession(self, appName, master):
        ss = SparkSession \
            .builder \
            .appName(appName) \
            .master(master) \
            .config("spark.sql.warehouse.dir", "file:///tmp/spark/Temp") \
            .enableHiveSupport() \
            .getOrCreate()
        return ss

if __name__ == "__main__":
    ef = executeFun()
    ss = ef.getSparkSession("HdfsToHive", sys.argv[1])
    ss.sql("CREATE EXTERNAL TABLE IF NOT EXISTS meta_stt_word_tf(call_id string, user_id string, word string, tf int) ROW FORMAT DELIMITED FIELDS TERMINATED BY '|' stored as textfile location '/dq/skm/common/word/daily/201710/51/51/a/nsb'")
    # ss.sql("CREATE TABLE IF NOT EXISTS InternalData_day_spark_orc (REGDATE string, dq_id string, product_cat_id string, voc_cat_id string, channel string, prod1_count int, prod2_count int, cnt int)")
    ss.stop()



# spark-submit --master yarn \
# --deploy-mode client \
# --executor-memory 2g \
# --name HdfsToHive \
# --conf "spark.app.id=HdfsToHive" \
# DqdocToHiveExample.py \
# yarn \
# hdfs://localhost:8020/dq/av/fs/input/voc/small/InternalData.small.UTF-8 \
# hdfs://localhost:8020/dq/av/fs/py/output

# spark-submit --master yarn \
# --deploy-mode client \
# --executor-memory 2g \
# --name HdfsToHive \
# --conf "spark.app.id=HdfsToHive" \
# createHiveTable.py \
# yarn