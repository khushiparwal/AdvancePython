import pymysql
connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
cursor = connection.cursor()
q1 = "insert into employee values(4,'seema','capgemini',80000,'2')"
cursor.execute(q1)
connection.commit()
connection.close()
print("Data inserted successfully")