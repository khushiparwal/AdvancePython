import pymysql
connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
q1 = 'create table airport(airportId int, airportName varchar(100),city varchar(50), country varchar(50))'
cursor = connection.cursor()
cursor.execute(q1)
connection.commit()
connection.close()
print("Table created successfully")