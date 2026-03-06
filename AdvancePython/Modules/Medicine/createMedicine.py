import pymysql
connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
cursor = connection.cursor()
q1 = 'create table medicine(medicineId int primary key, medicineName varchar(100), price int, expireDate date)'
cursor.execute(q1)
connection.commit()
connection.close()
print("Table created successfully")