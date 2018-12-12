import pymysql

# conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='mysql')
conn = pymysql.connect(host='118.218.215.211', user='rtcdev', password='p@ssWord',
                       db='rtc', charset='utf8')

cur = conn.cursor()
cur.execute("select * from Persons")
for r in cur:
    print(r)
cur.close()
conn.close()
