import pymysql
connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
cursor = connection.cursor()
q1 = 'update employee set salary = 90000 where id=4'
cursor.execute(q1)
connection.commit()
connection.close()
print("Data updated successfully")