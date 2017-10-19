from operator import add
from pyspark import SparkContext, SparkConf
import sys


class WordCount:
    def getSparkContext(self, appName, master):
        conf = SparkConf().setAppName(appName).setMaster(master)
        return SparkContext(conf=conf)

    def getInputRDD(self, sc, input):
        return sc.textFile(input)

    def process(self, inputRDD):
        words = inputRDD.flatMap(lambda s: s.split(" "))
        wcPair = words.map(lambda s: (s, 1))
        return wcPair.reduceByKey(add)

if __name__ == "__main__":

    wc = WordCount()
    sc = wc.getSparkContext("WordCount", sys.argv[1])
    inputRDD = wc.getInputRDD(sc, sys.argv[2])
    resultRDD = wc.process(inputRDD)
    result = resultRDD.collect()
    # print('resultRDD : {0}'.format(result))

    cid = sys.argv[4]
    uid = sys.argv[5]
    farray=[]
    for v in result:
        # farray.append( ('', ''.join( [cid, '|', uid, '|', v[0], '|', str(v[1])] )) )
        farray.append(''.join([cid, '|', uid, '|', v[0], '|', str(v[1])]))

    # resultRDD.saveAsTextFile(sys.argv[3])


    # outputFormatClass = "org.apache.hadoop.mapreduce.lib.output.SequenceFileOutputFormat"
    # inputFormatClass = "org.apache.hadoop.mapreduce.lib.input.SequenceFileInputFormat"
    # keyClass = "org.apache.hadoop.io.Text"
    # # valueClass = "org.apache.hadoop.io.IntWritable"
    # valueClass = "org.apache.hadoop.io.Text"
    # conf = "org.apache.hadoop.conf.Configuration"
    # rdd1 = sc.parallelize(farray)
    # # rdd2 = rdd1.map(lambda x: (x, 1))
    #
    # # save
    # rdd1.saveAsNewAPIHadoopFile(sys.argv[3], outputFormatClass, keyClass, valueClass)
    # # load
    # rdd3 = sc.newAPIHadoopFile(sys.argv[3], inputFormatClass, keyClass, valueClass)
    # for k, v in rdd3.collect():
    #     print(k, v)
    #
    #
    # sc.stop()


    createFile = open("/Users/whitexozu/dev/pycharm_workspace/pythonExample/example/createCSVFile/", 'w')
    for i in range(farray):
        createFile.write(i)

    createFile.close()

# spark-submit --master yarn \
# --deploy-mode client \
# --executor-memory 2g \
# --name HdfsToHive \
# --conf "spark.app.id=HdfsToHive" \
# CreateCsvFileExample.py \
# yarn \
# hdfs://localhost:8020/dq/skm/common/word/temp/callsentenceText1.txt \
# hdfs://localhost:8020/dq/skm/common/word/daily/201710/51/51/a/nsb \
# 69684547 \
# user1

# spark-submit --master yarn \
# --deploy-mode client \
# --executor-memory 2g \
# --name HdfsToHive \
# --conf "spark.app.id=HdfsToHive" \
# CreateCsvFileExample.py \
# yarn \
# hdfs://localhost:8020/dq/skm/common/word/temp/callsentenceText1.txt \
# /Users/whitexozu/dev/pycharm_workspace/pythonExample/example/createCSVFile/callWordCsv1.txt \
# 69684547 \
# user1