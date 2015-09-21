import pymssql
import sys

server = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]
db_name = sys.argv[4]

conn = pymssql.connect(server, user, password, db_name)
cursor = conn.cursor()

cursor.execute('SELECT TOP 100 * FROM orders')
row = cursor.fetchone()
while row:
    print("OrderItem=%s" % (row[2]))
    row = cursor.fetchone()

conn.close()
