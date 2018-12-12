import pymysql

conn = pymysql.connect(host='211.177.149.29', user='diquest', password='ek2znptm2',
                       db='ta_ics', charset='utf8')

curs = conn.cursor()
# sql = """INSERT INTO trace(service_id,user_id,status) VALUES(%s, %s, %s)"""
sql = """INSERT INTO Persions(PersionId, LastName, FirstName) VALUES(%s, %s, %s)"""

curs.execute(sql, ('1', 'user1', '1'))
curs.execute(sql, ('2', 'user2', '2'))
conn.commit()

conn.close()
