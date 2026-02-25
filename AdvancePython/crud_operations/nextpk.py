import pymysql
connection = pymysql.connect(host='localhost',port=3306,user='root',password='root',db='rays')
cursor = connection.cursor()
pk = 0
q1 = 'select max(id) from employee'
cursor.execute(q1)
result = cursor.fetchall()
print(result)
for data in result:
    pk = data[0]
connection.commit()
connection.close()
print(pk+1)