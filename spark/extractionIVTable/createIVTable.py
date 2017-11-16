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
    # reload(sys)
    # sys.setdefaultencoding('utf-8')

    ef = executeFun()
    ss = ef.getSparkSession("insert ta_keyword_iv", sys.argv[1])

    campStartDt = '201709'
    insrcompCdArray = ['51']
    brchCdArray = ['51', '54', '55']
    spkCdArray = ['f', 'c', 'a']
    # callTypeArray = ['sb', 'nsb']

    createTableSql = []
    createTableSql.append("CREATE TABLE IF NOT EXISTS ta_keyword_iv ")
    createTableSql.append("( ")
    createTableSql.append("keyword string, ")
    createTableSql.append("iv int, ")
    createTableSql.append("user_count int ")
    createTableSql.append(") ")
    createTableSql.append("partitioned by (camp_start_dt string, insrcomp_cd string, brch_cd string, spk_cd string) ")
    createTableSql.append("ROW FORMAT DELIMITED ")
    ss.sql(''.join(createTableSql))

    keyword = ''
    sbcpMax = 10
    nonsbcpMax = 300
    eventY = 0
    eventN = 0
    nonEventY = 0
    nonEventN = 0
    woeY = 0
    woeN = 0
    ivY = 0
    ivN = 0

    sf1 = StructField("keyword", StringType(), False)
    sf2 = StructField("iv", DoubleType(), False)
    sf3 = StructField("user_count", IntegerType(), False)
    sf4 = StructField("camp_start_dt", StringType(), False)
    sf5 = StructField("insrcomp_cd", StringType(), False)
    sf6 = StructField("brch_cd", StringType(), False)
    sf7 = StructField("spk_cd", StringType(), False)

    schema = StructType([sf1, sf2, sf3, sf4, sf5, sf6, sf7])

    for insrcompCd in insrcompCdArray:
        for brchCd in brchCdArray:
            for spkCd in spkCdArray:
                selectQuery = "select keyword, count(user_id) as user_count from ta_common_keyword where camp_start_dt='{0}' and insrcomp_cd='{1}' and brch_cd='{2}' and spk_cd='{3}' and call_type='{4}' group by keyword".format(
                    campStartDt, insrcompCd, brchCd, spkCd, 'sb')
                # print('selectQuery : ' + selectQuery)
                sbDf = ss.sql(selectQuery)

                selectQuery = "select keyword, count(user_id) as user_count from ta_common_keyword where camp_start_dt='{0}' and insrcomp_cd='{1}' and brch_cd='{2}' and spk_cd='{3}' and call_type='{4}' group by keyword".format(
                    campStartDt, insrcompCd, brchCd, spkCd, 'nsb')
                # print('selectQuery : ' + selectQuery)
                nsbDf = ss.sql(selectQuery)

                if sbDf.count() > 0 and nsbDf.count() > 0 :
                    # print(sbDf.count())
                    # print(nsbDf.count())
                    print('-----------------------------------')
                    print('{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}|{10}|{11}|{12}|{13}|{14}|{15}'.format('keyword', 'campStartDt', 'insrcompCd', 'brchCd', 'spkCd', 'sbUserCount', 'nsbUserCount', 'Event(Y)', 'Event(N)', 'Non-Event(Y)', 'Non-Event(N)', 'WOE(=Y)', 'WOE(=N)', 'IV(=Y)', 'IV(=N)', 'IV Sum'))
                    resultDf = sbDf.join(nsbDf, 'keyword', 'inner')
                    insertRows = [];
                    for t in resultDf.collect():
                        keyword = t[0]
                        eventY = float(t[1]) / float(sbcpMax)
                        eventN = float(float(sbcpMax) - float(t[1])) / float(sbcpMax)
                        nonEventY = float(t[2]) / float(nonsbcpMax)
                        nonEventN = float(float(nonsbcpMax) - float(t[2])) / float(nonsbcpMax)
                        woeY = math.log(eventY / nonEventY)
                        woeN = math.log(eventN / nonEventN)
                        ivY = woeY - (eventY - nonEventY)
                        ivN = woeN - (eventN - nonEventN)
                        # print('{0}, {1}, {2}, {3}, {4}'.format(keyword, campStartDt, insrcompCd, brchCd, spkCd))
                        # print('{0}, {1}'.format(ivY + ivN, t[1] + t[2]))
                        print('{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}|{10}|{11}|{12}|{13}|{14}|{15}'.format(keyword.encode('utf-8'), campStartDt, insrcompCd, brchCd, spkCd, t[1], t[2], eventY, eventN, nonEventY, nonEventN, woeY, woeN, ivY, ivN, ivY + ivN))
                        insertRows.append([keyword, ivY + ivN, t[2], campStartDt, insrcompCd, brchCd, spkCd])

                    insertDf = ss.createDataFrame(insertRows, schema)
                    insertDf.write.mode("overwrite").partitionBy("camp_start_dt", "insrcomp_cd", "brch_cd", "spk_cd").format("orc").saveAsTable("ta_keyword_iv")
                    # ss.sql("show tables").show()

    ss.stop()



# spark-submit createIVTable.py yarn