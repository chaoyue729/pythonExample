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
    # 캠페인 종료 후 새로운 캠페인 시작날짜가 생성된 경우 외부 테이블 생성 (한달에 1번, 캠페인 종료시 실행)
    ef = executeFun()
    ss = ef.getSparkSession("create ta_common_keyword table", sys.argv[1])

    createTableSql = []
    createTableSql.append("CREATE EXTERNAL TABLE IF NOT EXISTS ta_common_keyword ")
    createTableSql.append("( ")
    createTableSql.append("user_id string, ")
    createTableSql.append("keyword string, ")
    createTableSql.append("tf int, ")
    createTableSql.append("call_id string, ")
    createTableSql.append("call_date string, ")
    createTableSql.append("brch_cd string ")
    createTableSql.append(") ")
    createTableSql.append("partitioned by (camp_start_dt string, insrcomp_cd string, brch_cd string, spk_cd string, call_type string) ")
    createTableSql.append("ROW FORMAT DELIMITED ")
    createTableSql.append("FIELDS TERMINATED BY '|' ")
    createTableSql.append("stored as textfile ")
    createTableSql.append("location '/dq/skm/common/keyword/daily' ")

    ss.sql(''.join(createTableSql))

    campStartDt = sys.argv[2]
    insrcompCdArray = ['51']
    brchCdArray = ['51', '54', '55']
    spkCdArray = ['f', 'c', 'a']
    callTypeArray = ['sb', 'nsb']

    for insrcompCd in insrcompCdArray:
        for brchCd in brchCdArray:
            for spkCd in spkCdArray:
                for callType in callTypeArray:
                    ss.sql("ALTER TABLE ta_common_keyword ADD PARTITION (camp_start_dt='{0}', insrcomp_cd='{1}', brch_cd='{2}', spk_cd='{3}', call_type='{4}') location '/dq/skm/common/keyword/daily/{0}/{1}/{2}/{3}/{4}'".format(campStartDt, insrcompCd, brchCd, spkCd, callType))

    ss.stop()

# spark-submit createHiveTable.py yarn 201710