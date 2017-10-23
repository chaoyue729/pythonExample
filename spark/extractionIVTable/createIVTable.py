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
    ss = ef.getSparkSession("insert ta_word_tfidf", sys.argv[1])

    campStartDt = '201710'
    insrcompCdArray = ['51']
    brchCdArray = ['51', '54', '55']
    spkCdArray = ['f', 'c', 'a']
    callTypeArray = ['sb', 'nsb']

    keyword = ''
    sbcpMax = 1
    nonsbcpMax = 3
    eventY = 0
    eventN = 0
    nonEventY = 0
    nonEventN = 0
    woeY = 0
    woeN = 0
    ivY = 0
    ivN = 0
    # sbDf = []
    # nsbDf = []

    for insrcompCd in insrcompCdArray:
        for brchCd in brchCdArray:
            for spkCd in spkCdArray:
                for callType in callTypeArray:
                    selectQuery = "select keyword, count(user_id) as user_count from ta_common_keyword where camp_start_dt='{0}' and insrcomp_cd='{1}' and brch_cd='{2}' and spk_cd='{3}' and call_type='{4}' group by keyword".format(campStartDt, insrcompCd, brchCd, spkCd, callType)
                    print('selectQuery : ' + selectQuery)
                    if callType == 'sb':
                        sbDf = ss.sql(selectQuery)
                        print('>>>>>>>>')
                        print(sbDf.count())
                        print(sbDf.count() > 0)
                        print('<<<<<<<<')
                        if sbDf.count() > 0:
                            sbRows = sbDf.rdd.map(lambda x: [x.keyword, x.user_count])
                            for x in sbRows:
                                print(x[0], x[1])
                    # elif callType == 'nsb':
                    #     nsbDf = ss.sql(selectQuery)


                    # print(sbDf);
                    # print(nsbDf);
                    print('-----------------------------------')

    ss.stop()



# spark-submit createIVTable.py yarn