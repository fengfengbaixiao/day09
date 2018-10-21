import pymysql

con = pymysql.connect(host="192.168.1.253", user="root",password="root",
                database="User",port=3306,charset="utf8")
cur = con.cursor()

# read_sql="select * from User_like_book "

# cur.execute(read_sql)
# print(cur.fetchall())
# print(cur.fetchmany(2))
# print(cur.fetchone())

write_sql = "update User_like_book set book_product='搞笑' where user_name='lop'"

cur.execute(write_sql)
con.commit()
con.rollback()


cur.close()
con.close()
