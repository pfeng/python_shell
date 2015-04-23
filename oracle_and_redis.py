import sys
import redis
import cx_Oracle

type = sys.getfilesystemencoding()

# oracle demo
dbcon = cx_Oracle.connect('hs/hs123456@127.0.0.1/orcl')
cursor = dbcon.cursor()
cursor.execute('select * from hs_school')
rows = cursor.fetchall()
for row in rows:
    school = "%s,%s" % (row[0], row[1])
    print school.decode(type)

# redis demo
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.StrictRedis(connection_pool=pool)
r.set('one', 'first')
print r.get('one')