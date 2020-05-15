import pymysql.connections

db = pymysql.connect(
    host="127.0.0.1",
    user="python",
    password="1234",
    db="world"
)

cur = db.cursor()
cur.execute("select * from city")
print(cur.fetchall())
input()