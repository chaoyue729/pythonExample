import collections

from pyspark import SparkContext, SparkConf
from pyspark.sql import Row
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql import functions
from pyspark.sql.types import *
from pyspark.sql.window import Window
import sys
import tensorflow as tf
import numpy as np

class executeFun():
    def getSparkContext(self, appName, master):
        conf = SparkConf().setAppName(appName).setMaster(master)
        return SparkContext(conf=conf)

    def getSparkSession(self, appName, master):
        ss = SparkSession \
            .builder \
            .appName(appName) \
            .master(master) \
            .config("spark.sql.warehouse.dir", "file:///tmp/spark/Temp") \
            .enableHiveSupport() \
            .getOrCreate()
        return ss

    def loadHdfsRDD(self, sc, input):
        return sc.textFile(input)

    def saveHdfsRDD(self, sc, output, data):
        sc.parallelize(data).saveAsTextFile(output)

    def process(self, dqdocRDD):
        valueSb = []
        state = 0
        output = []

        for line in dqdocRDD.collect():
            if line == '(DQ_DOC':
                state = 1
            elif line == ')DQ_DOC':
                state = 2
            elif line.startswith('(') and line.find(')') == -1 and line != '(DQ_DOC':
                state = 3
            elif line.startswith(')') and line.find('(') == -1 and line != ')DQ_DOC':
                state = 4
                valueSb.append('^')

            if state == 3:
                if not (line.startswith('(')):
                    line = line.strip()
                    line = line.replace('^', '')
                    valueSb.append(line)
            elif state == 2:
                output.append(''.join(valueSb)[:-1])
                valueSb = []

        return output

if __name__ == "__main__":
    ef = executeFun()
    sc = ef.getSparkContext("HdfsToHive", sys.argv[1])
#    dqdocRDD = ef.loadHdfsRDD(sc, sys.argv[2])
#    print("---------------------------- load hdfs dqdoc end ----------------------------")
#    ef.saveHdfsRDD(sc, sys.argv[3], ef.process(dqdocRDD))
#    print("---------------------------- save hdfs meta end ----------------------------")
#    metaRDD = ef.loadHdfsRDD(sc, sys.argv[2])
    
#    xy=[]
#    xycnt=0
#    newxy=[]	
#    for s in metaRDD.collect():
#        cnt = cnt+1
        #print('meta s : %s' % s.split('^')[0])
#        print(type(s))
#        LineArray = s.split()
#        xy = np.asmatrix(LineArray, int)
#        newxy=np.append(newxy,xy, axis=0)
#        print(newxy)
		
#    print("---------------------------- load hdfs meta end ----------------------------")

    ss = ef.getSparkSession("HdfsToHive", sys.argv[1])
    sf1 = StructField("regdate", StringType(), True)
    sf2 = StructField("dq_id", StringType(), True)
    sf3 = StructField("product_cat_id", StringType(), True)
    sf4 = StructField("VOC_CAT_ID", StringType(), True)
    sf5 = StructField("channel", StringType(), True)
    sf6 = StructField("prod1_count", IntegerType(), True)
    sf7 = StructField("prod2_count", IntegerType(), True)
    sf8 = StructField("cnt", IntegerType(), True)
    schema = StructType([sf1, sf2, sf3, sf4, sf5, sf6, sf7, sf8])
   
    metaRDD = ef.loadHdfsRDD(sc, sys.argv[3])
    hiveRows = []
    for s in metaRDD.collect():
        sa = s.split('^')
        # print('meta sa : %s' % sa[0])
        # print('meta sa : %s' % sa[1])
        # print('meta sa : %s' % sa[9])
        # print('meta sa : %s' % sa[10])
        # print('meta sa : %s' % sa[11])
        # print('meta sa : %s' % sa[30])
        # print('meta sa : %s' % sa[31])
        hiveRows.append([str(sa[0])[0:10], sa[1], sa[9], sa[10], str(sa[11]), int(sa[30]), int(sa[31]), 1])
   
    df = ss.createDataFrame(hiveRows, schema)
    
    ss.sql("CREATE TABLE IF NOT EXISTS InternalData_day_spark_orc (REGDATE string, dq_id string, product_cat_id string, voc_cat_id string, channel string, prod1_count int, prod2_count int, cnt int)")
    
    df.write.mode("overwrite").format("orc").saveAsTable("InternalData_day_spark_orc")
    ss.sql("show tables").show()
    print("---------------------------- save hive meta end ----------------------------")

ss.stop()
sc.stop()


# spark-submit --master yarn \
# --deploy-mode client \
# --executor-memory 2g \
# --name HdfsToHive \
# --conf "spark.app.id=HdfsToHive" \
# DqdocToHiveExample.py \
# yarn \
# hdfs://localhost:8020/dq/av/fs/input/voc/small/InternalData.small.UTF-8 \
# hdfs://localhost:8020/dq/av/fs/py/output
