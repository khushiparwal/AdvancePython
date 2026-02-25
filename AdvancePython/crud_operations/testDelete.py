import pymysql
connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
cursor = connection.cursor()
q1 = 'delete from employee where id=4'
cursor.execute(q1)
connection.commit()
connection.close()
print("Data deleted successfully")