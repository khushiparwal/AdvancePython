import pymysql
connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
cursor = connection.cursor()
q1 = 'select * from employee'
cursor.execute(q1)
result = cursor.fetchall()
print(result)
connection.commit()
connection.close()
print("data printed successfully")