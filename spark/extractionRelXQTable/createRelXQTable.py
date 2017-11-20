#-*- coding: utf-8 -*-

import collections
import math
from operator import add
from pyspark import SparkContext, SparkConf
from pyspark.sql import Row
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql import functions
from pyspark.sql.types import *
from pyspark.sql.window import Window
import sys
import operator
import time

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

if __name__ == "__main__":
    # reload(sys)
    # sys.setdefaultencoding('utf-8')

    ef = executeFun()
    sc = ef.getSparkContext("createRelXQTable_rdd", sys.argv[1])
    ss = ef.getSparkSession("insert ta_keyword_relxq", sys.argv[1])

    campStartDt = '201709'
    insrcompCdArray = ['51']
    # brchCdArray = ['51', '54', '55']
    brchCdArray = ['51']
    # spkCdArray = ['a', 'f', 'c']
    spkCdArray = ['a']

    # selectQuery = []

    for insrcompCd in insrcompCdArray:
        for brchCd in brchCdArray:
            for spkCd in spkCdArray:
                start_time = time.time()
                selectQuery = []
                selectQuery.append("select collect_list(keyword) as keywords ")
                selectQuery.append("from ( ")
                selectQuery.append("select user_id, keyword ")
                selectQuery.append("from ta_common_keyword ")
                selectQuery.append("where camp_start_dt='{0}' ")
                selectQuery.append("and insrcomp_cd='{1}' ")
                selectQuery.append("and brch_cd='{2}' ")
                selectQuery.append("and spk_cd='{3}' ")
                selectQuery.append("and call_type='{4}' ")
                selectQuery.append(") ")
                selectQuery.append("group by user_id")

                selectQuery = (''.join(selectQuery)).format(campStartDt, insrcompCd, brchCd, spkCd, 'sb')
                print('selectQuery : ' + selectQuery)
                collectListDf = ss.sql(selectQuery)
                rdd1 = collectListDf.rdd.map(lambda p: (p['keywords']))
                # print(rdd1.count());
                rdd2 = rdd1.filter(lambda k : k.index(unicode('다이퀘스트', 'utf-8')) > -1)
                for r in rdd2.collect():
                    print(r)





                # for t in collectListDf.collect():
                #     print(t[0].encode('utf-8'))

                print("--- %s seconds ---" % (time.time() - start_time))

    ss.stop()



# spark-submit createRelXQTable.py yarn
