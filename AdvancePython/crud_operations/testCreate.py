import pymysql
connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
cursor = connection.cursor()
q1 = 'create table manager(id int primary key, name varchar(50))'
cursor.execute(q1)
connection.commit()
connection.close()
print("Table created successfully")