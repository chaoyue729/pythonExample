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
    # sf1 = StructField("call_id", StringType(), True)
    # sf2 = StructField("user_id", StringType(), True)
    # sf3 = StructField("word", StringType(), True)
    # sf4 = StructField("tf", IntegerType(), True)
    # schema = StructType([sf1, sf2, sf3, sf4])

    # df.createOrReplaceTempView("table1")

    df = ss.sql("select word, sum(tf) as tf, count(call_id) as idf, count(distinct user_id) as user_count from meta_stt_word_tf group by word")
    print(df.collect())
    # wtf = df.collect()
    # wtf = df.collect()
    # wtf2 = wtf.map()


    # metaRDD = ef.loadHdfsRDD(sc, sys.argv[3])
    # hiveRows = []
    # for s in metaRDD.collect():
    #     sa = s.split('^')
    #     print('meta sa : %s' % sa[0])
    #     print('meta sa : %s' % sa[1])
    #     print('meta sa : %s' % sa[9])
    #     print('meta sa : %s' % sa[10])
    #     print('meta sa : %s' % sa[11])
    #     print('meta sa : %s' % sa[30])
    #     print('meta a : %s' % sa[31])
    #     hiveRows.append([str(sa[0])[0:10], sa[1], sa[9], sa[10], str(sa[11]), int(sa[30]), int(sa[31]), 1])
    #
    # df = ss.createDataFrame(hiveRows, schema)
    #
    # ss.sql("CREATE TABLE IF NOT EXISTS InternalData_day_spark_orc (REGDATE string, dq_id string, product_cat_id string, voc_cat_id string, channel string, prod1_count int, prod2_count int, cnt int)")

    # select word, sum(tf) from meta_stt_word_tf group by word order by 1;
    # select word, count(call_id) from (select word, call_id from meta_stt_word_tf) group by word
    ss.stop()



# spark-submit --master yarn \
# --deploy-mode client \
# --executor-memory 2g \
# --name HdfsToHive \
# --conf "spark.app.id=HdfsToHive" \
# createTFIDFTable.py \
# yarn